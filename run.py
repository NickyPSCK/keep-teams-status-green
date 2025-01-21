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
       ____           _____ _____ ____
      / ___|         |_   _| ____/ ___|
     | |  _   _____    | | |  _|| |
     | |_| | |_____|   | | | |__| |___
      \\____|           |_| |_____\\____|

>>>>>>>>> :: Unleash Green Energy :: <<<<<<<<<
----------------------------------------------
|||||||||||| PRESS CTRL-C TO QUIT ||||||||||||
----------------------------------------------'''


class AlwaysGreen:
    '''
    A class to prevent inactivity by detecting user input and moving the mouse.

    Attributes:
        timeout_period (int): Timeout period in seconds
            before moving the mouse.
        exemped_periods (list): List of periods during
            which the application is exempted from action.
        modern_output (bool): Enables modern output with
            colored text and emojis.
        show_status (bool): Displays the user activity status.
    '''
    def __init__(
        self,
        timeout_period: int = 60,
        exemped_periods: list = None,
        modern_output: bool = False,
        show_status: bool = True
    ):
        '''
        Initializes the AlwaysGreen instance with user-configurable parameters.

        Args:
            timeout_period (int): Timeout period in seconds before
                inactivity action is triggered.
            exemped_periods (list): List of tuples with start and end
                times of exempted periods in HH:MM:SS format.
            modern_output (bool): Enables or disables colored
                and emoji status output.
            show_status (bool): Enables or disables the display
                of user activity status.
        '''

        self._time_format = '%H:%M:%S'
        self._mouse = mouse.Controller()
        self._move_distance = 100
        self._status_str = None

        self._timeout_period = timeout_period
        self._exemped_periods = self._process_exemped_periods(
            exemped_periods=exemped_periods
        )
        self._modern_output = modern_output
        self._show_status = show_status

        self._in_exemped_periods = self._check_exemped_periods()
        self._time_left = self._timeout_period

        if self._modern_output:
            self._reset_color = '\033[0m'
            self._green_color = '\033[32m'
            self._red_color = '\033[31m'
            self._user_active_status = 'Status:🟢'
            self._user_inactive_status = 'Status:🟡'
        else:
            self._reset_color = ''
            self._green_color = ''
            self._red_color = ''
            self._user_active_status = ' #ACTIVE '
            self._user_inactive_status = '#INACTIVE'

    @property
    def status_str(self):
        '''
        Returns the current status string.

        Returns:
            str: Current status string.

        '''
        return self._status_str

    @property
    def exemped_periods(self):
        '''
        Returns the list of exempted periods.

        Returns:
            list: Processed exempted periods as list of tuples
            with datetime objects.
        '''
        return self._exemped_periods

    def _process_exemped_periods(self, exemped_periods):
        '''
        Processes exempted periods and converts them
        into datetime.time objects.

        Args:
            exemped_periods (list): List of tuples with start and end times
            in HH:MM:SS format.

        Returns:
            list: List of tuples with datetime.time objects.
        '''
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

    def print_exemped_periods(self):
        '''
        Prints the exempted periods if any are set.

        Returns:
            bool: True if exempted periods exist, False otherwise.
        '''
        if len(self._exemped_periods) > 0:
            print('Exemped Periods:')
            for start_time, end_time in self._exemped_periods:
                print(
                    '    >> ',
                    start_time.strftime(self._time_format),
                    '-',
                    end_time.strftime(self._time_format),
                )
            return True
        else:
            return False

    def _set_active(self):
        '''
        Resets the inactive timer when user activity is detected.
        '''
        self._is_moved = True
        self._time_left = self._timeout_period
        self._in_exemped_periods = self._check_exemped_periods()
        self._report_status()

    def _on_move(self, x, y):
        '''
        Callback for mouse move events.
        '''
        self._set_active()

    def _on_click(self, x, y, button, pressed):
        '''
        Callback for mouse click  events.
        '''
        self._set_active()

    def _on_scroll(self, x, y, dx, dy):
        '''
        Callback for mouse scroll events.
        '''
        self._set_active()

    def _on_press(self, key):
        '''
        Callback for keyboard press events.
        '''
        self._set_active()

    def _on_release(self, key):
        '''
        Callback for keyboard release events.
        '''
        self._set_active()

    def _report_status(self):
        '''
        Displays the current user activity status.
        '''
        if self._show_status:
            if self._in_exemped_periods:
                app_status = f'{self._red_color}RELEASED{self._reset_color}'
            else:
                app_status = f'{self._green_color}ENFORCED{self._reset_color}'

            if self._is_moved:
                user_status = self._user_active_status
            else:
                user_status = self._user_inactive_status

            app_status_str = f'| {app_status}'
            countdown_str = f'| Inactive in {self._time_left:>6}s'
            user_status_str = f'| {user_status} |'

            self._status_str = ' '.join([
                app_status_str,
                countdown_str,
                user_status_str,
                f'{self._reset_color}'
            ])
            print(self._status_str, end='\r')

    def _wait(self):
        '''
        Waits for the timeout period while reporting status.
        '''
        while self._time_left >= 0:
            self._report_status()
            self._time_left -= 1
            time.sleep(1)

    def _check_exemped_periods(self):
        '''
        Checks if the current time is within any exempted period.

        Returns:
            bool: True if within an exempted period, False otherwise.
        '''
        exemped = False
        for start_time, end_time in self._exemped_periods:
            if start_time <= datetime.now().time() <= end_time:
                exemped = True
                break
        return exemped

    def _move_mouse(self):
        '''
        Moves the mouse to prevent inactivity.
        '''
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
        '''
        Main logic for detecting inactivity and moving the mouse.
        Continuously monitors user activity and takes actions
        based on timeout settings.
        '''
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

            self._in_exemped_periods = self._check_exemped_periods()
            self._move_mouse()
            self._is_moved = False


def input_argument():
    '''
    Parses command-line arguments for configuring the application.

    Returns:
        dict: Dictionary of parsed arguments.
    '''
    parser = argparse.ArgumentParser(
        description='G-TECH: Unleash Green Energy.'
    )
    parser.add_argument(
        '--time',
        type=int,
        default=5,
        help='Timeout period in seconds before inactivity action is taken.'
    )
    parser.add_argument(
        '--classic',
        action='store_false',
        default=True,
        help='Disable colored and emoji output.'
    )
    parser.add_argument(
        '--no-logo',
        action='store_false',
        default=True,
        help='Disable displayed logo.',
    )
    parser.add_argument(
        '--no-exemped-period',
        action='store_false',
        default=True,
        help='Disable displayed exemped period.',
    )
    parser.add_argument(
        '--no-status',
        action='store_false',
        default=True,
        help='Disable displayed staus'
    )

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
        modern_output=args_dict['classic'],
        show_status=args_dict['no_status'],
    )
    if args_dict['no_logo']:
        print(f'{logo}''')

    if args_dict['no_exemped_period']:
        if AW.print_exemped_periods():
            print('----------------------------------------------')

    try:
        AW.run()
    except KeyboardInterrupt:
        print('\n----------------- TERMINATED -----------------')
        sys.exit(0)
