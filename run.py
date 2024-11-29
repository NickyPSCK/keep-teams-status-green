# G-TECH: Unleash Green Energy
# Long lasting green technology.

import sys
import time
import argparse
from datetime import datetime
from pynput import mouse, keyboard

logo = '''----------------------------------------------
||||||||||||||||||||||||||||||||||||||||||||||
----------------------------------------------
    ____           _____ _____ ____ _   _
   / ___|         |_   _| ____/ ___| | | |
  | |  _   _____    | | |  _|| |   | |_| |
  | |_| | |_____|   | | | |__| |___|  _  |
   \\____|           |_| |_____\\____|_| |_|

>>>>>>>>> :: Unleash Green Energy :: <<<<<<<<<
----------------------------------------------
|||||||||||| PRESS CTRL-C TO QUIT ||||||||||||
----------------------------------------------'''


class AlwaysGreen:
    def __init__(
        self,
        timeout_period: int = 60,
        exemped_periods: list = None,
        color: bool = False,
        status: bool = True
    ):
        '''
        Prevents inactivity by detecting user input and moving the mouse.
        Args:
            timeout_period (int): Timeout period in seconds
                before moving the mouse.
            color (bool): Whether to use colored status output.
            status (bool): Whether to display the user activity status.
        '''

        self._time_format = '%H:%M:%S'
        self._mouse = mouse.Controller()
        self._move_distance = 100

        self._timeout_period = timeout_period
        self._exemped_periods = self._process_exemped_periods(
            exemped_periods=exemped_periods
        )
        self._color = color
        self._status = status

        self._in_exemped_periods = self._check_exemped_periods()
        self._time_left = self._timeout_period
        if self._color:
            self._reset_color = '\033[0m'
            self._green_color = '\033[32m'
            self._red_color = '\033[31m'
        else:
            self._reset_color = ''
            self._green_color = ''
            self._red_color = ''

    def _process_exemped_periods(self, exemped_periods):
        if exemped_periods is None:
            return list()
        else:
            processed_exemped_periods = list()
            for start_time_str, end_time_str in exemped_periods:
                start_time = datetime.strptime(
                    start_time_str,
                    self._time_format
                ).time()
                end_time = datetime.strptime(
                    end_time_str,
                    self._time_format
                ).time()
                processed_exemped_periods.append((start_time, end_time))
            return processed_exemped_periods

    def _set_active(self):
        '''Resets the inactive timer when user activity is detected.'''
        self._is_moved = True
        self._time_left = self._timeout_period
        self._report_status()

    def _on_move(self, x, y):
        self._set_active()

    def _on_click(self, x, y, button, pressed):
        self._set_active()

    def _on_scroll(self, x, y, dx, dy):
        self._set_active()

    def _on_press(self, key):
        self._set_active()

    def _on_release(self, key):
        self._set_active()

    def _report_status(self):
        '''Displays the current user activity status.'''
        if self._status:
            if self._in_exemped_periods:
                app_status = f'{self._red_color}EXEMPTED{self._reset_color}'
            else:
                app_status = f'{self._green_color}ENFORCED{self._reset_color}'

            if self._is_moved:
                user_status = '🟢'
            else:
                user_status = '🟡'

            app_status_str = f'| {app_status}'
            countdown_str = f'| Inactive in {self._time_left:>6}s'
            user_status_str = f'| Status:{user_status} |'

            print(
                app_status_str,
                countdown_str,
                user_status_str,
                f'{self._reset_color}',
                end='\r'
            )

    def _wait(self):
        '''Waits for the timeout period while reporting status.'''
        while self._time_left >= 0:
            self._report_status()
            self._time_left -= 1
            time.sleep(1)

    def _check_exemped_periods(self):
        exemped = False
        for start_time, end_time in self._exemped_periods:
            if start_time <= datetime.now().time() <= end_time:
                exemped = True
                break
        return exemped

    def _move_mouse(self):
        '''Moves the mouse to prevent inactivity.'''
        self._in_exemped_periods = self._check_exemped_periods()
        if not self._in_exemped_periods:
            if not self._is_moved:
                if self._mouse.position != (0, 0):
                    self._mouse.position = (0, 0)
                    self._mouse.press(mouse.Button.left)
                    self._mouse.release(mouse.Button.left)
                else:
                    self._mouse.move(
                        self._move_distance,
                        self._move_distance
                    )

    def run(self):
        '''Main logic for detecting inactivity and moving the mouse.'''
        self._is_moved = False

        while True:
            self._time_left = self._timeout_period

            mouse_listener = mouse.Listener(
                on_move=self._on_move,
                on_click=self._on_click,
                on_scroll=self._on_scroll
            )
            keyboard_listener = keyboard.Listener(
                on_press=self._on_press,
                on_release=self._on_release)

            mouse_listener.start()
            keyboard_listener.start()

            self._wait()

            mouse_listener.stop()
            keyboard_listener.stop()
            mouse_listener.join()
            keyboard_listener.join()

            self._move_mouse()

            self._is_moved = False


def input_argument():
    '''Parses command-line arguments.'''

    def add_bool_arg(
        parser,
        name,
        help='',
        default=True,

    ):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=name, action='store_true', help=help)
        group.add_argument('--no-' + name, dest=name, action='store_false', help=help)
        parser.set_defaults(**{name: default})

    parser = argparse.ArgumentParser(
        description='G-TECH: Unleash Green Energy.'
    )
    parser.add_argument(
        '--time',
        type=int,
        default=5,
        help='Timeout period in seconds before inactivity action is taken.')

    add_bool_arg(parser, 'color', help='Enable or disable colored output.')
    add_bool_arg(parser, 'status', help='Enable or disable staus.')
    add_bool_arg(parser, 'logo', help='Enable or disable displayed logo.')

    args_dict = vars(parser.parse_args())

    return args_dict


if __name__ == '__main__':
    args_dict = input_argument()

    exemped_periods = [
        ('12:00:00', '13:00:00'),
        ('17:00:00', '18:00:00'),
    ]

    AW = AlwaysGreen(
        timeout_period=args_dict['time'],
        exemped_periods=exemped_periods,
        color=args_dict['color'],
        status=args_dict['status'],
    )
    if args_dict['logo']:
        print(f'{logo}''')

    try:
        AW.run()
    except KeyboardInterrupt:
        print('\n----------------- TERMINATED -----------------')
        sys.exit(0)
