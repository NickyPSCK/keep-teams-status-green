# https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
# https://pypi.org/project/pynput/
# https://www.asciiart.eu/text-to-ascii-art
# https://www.geeksforgeeks.org/print-colors-python-terminal/

import time
import threading
import argparse
from pynput import mouse
from pynput import keyboard

logo = '''----------------------------------------------
||||||||||||||||||||||||||||||||||||||||||||||
----------------------------------------------
    ____           _____ _____ ____ _   _ 
   / ___|         |_   _| ____/ ___| | | |
  | |  _   _____    | | |  _|| |   | |_| |
  | |_| | |_____|   | | | |__| |___|  _  |
   \\____|           |_| |_____\\____|_| |_|
          
----------------------------------------------
||||||||||||||||||||||||||||||||||||||||||||||
----------------------------------------------
>>>>>>>>> :: Unleash Green Energy :: <<<<<<<<<
----------------------------------------------'''

class AlwaysGreen(threading.Thread):
    def __init__(
            self,
            window_period:int = 60
        ):
        self._window_period = window_period
        self._mouse = mouse.Controller()
        self._move_distance = 100
        self._time_left = self._window_period

    def _set_active(self):
        self._is_moved = True
        self._report_status()
        
    def _on_move(self, x, y):
        self._set_active()

    def _on_click(self,x, y, button, pressed):
        self._set_active()

    def _on_scroll(self, x, y, dx, dy):
        self._set_active()

    def _on_press(self, key):
        self._set_active()

    def _on_release(self, key):
        self._set_active()

    def _report_status(self):
        if self._is_moved:
            print(  
                f'\033[0m::Refresh in {self._time_left:>7}s,',
                '\033[0m::User Status:', 
                f'\033[32m  Active', 
                end='\r',
            )
        else:
            print(
                f'\033[0m::Refresh in {self._time_left:>7}s,',
                '\033[0m::User Status:', 
                f'\033[31mInactive', 
                end='\r'
            )


    def run(self):
        self._is_moved = False
        
        while True:
            self._report_status()
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

            for s in range(self._window_period, -1, -1):
                self._report_status()
                self._time_left = s
                time.sleep(1)
            
            mouse_listener.stop()
            keyboard_listener.stop()

            mouse_listener.join()
            keyboard_listener.join()
            
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

            self._is_moved = False
            

def input_argument():
    parser = argparse.ArgumentParser(
        description='G-TECH: Long lasting green technology.'
    )
    parser.add_argument(
        '--time',
        metavar='window_period',
        type=int,
        default=5,
        help='window period')
    args_dict = vars(parser.parse_args())

    return args_dict


if __name__ == '__main__':
    args_dict = input_argument()
    AW = AlwaysGreen(window_period=args_dict['time'])
    print(f'{logo}''')
    AW.run()
