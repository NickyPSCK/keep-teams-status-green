# G-TECH: Unleash Green Energy
# Long lasting green technology.

import sys
import time
import argparse
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
        self._timeout_period = timeout_period
        self._color = color
        self._status = status

        self._mouse = mouse.Controller()
        self._move_distance = 100
        self._time_left = self._timeout_period

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
            if self._color:
                reset_color = '\033[0m'
                active_color = '\033[32m'
                inactive_color = '\033[33m'
            else:
                reset_color = ''
                active_color = ''
                inactive_color = ''

            if self._is_moved:
                status = f'{active_color}  Active'
            else:
                status = f'{inactive_color}Inactive'

            print(
                f'{reset_color}::Inactive in{self._time_left:>7}s,',
                f'{reset_color}::User Status:',
                status,
                f'{reset_color}',
                end='\r'
            )

    def _wait(self):
        '''Waits for the timeout period while reporting status.'''
        while self._time_left >= 0:
            self._report_status()
            self._time_left -= 1
            time.sleep(1)

    def _move_mouse(self):
        '''Moves the mouse to prevent inactivity.'''
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
    parser = argparse.ArgumentParser(
        description='G-TECH: Unleash Green Energy.'
    )
    parser.add_argument(
        '--time',
        type=int,
        default=5,
        help='Timeout period in seconds before inactivity action is taken.')

    parser.add_argument(
        '--color',
        action=argparse.BooleanOptionalAction,
        default=True,
        help='Enable or disable colored output.')

    parser.add_argument(
        '--status',
        action=argparse.BooleanOptionalAction,
        default=True,
        help='Enable or disable staus.')

    parser.add_argument(
        '--logo',
        action=argparse.BooleanOptionalAction,
        default=True,
        help='Enable or disable displayed logo.')

    args_dict = vars(parser.parse_args())

    return args_dict


if __name__ == '__main__':
    args_dict = input_argument()
    AW = AlwaysGreen(
        timeout_period=args_dict['time'],
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
