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
    # https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
    # https://pypi.org/project/pynput/
    # https://www.asciiart.eu/text-to-ascii-art
    def __init__(
            self,
            window_period: int=60
        ):
        self._window_period = window_period
        self._mouse = mouse.Controller()
        self._move_distance = 100

    def _set_active(self):
        self._is_moved = True
        print('>> Status: Active     ', end='\r')

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

    def run(self):
        self._is_moved = False
        
        while True:
            print('>> Status: Inactive     ', end='\r')
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

            time.sleep(self._window_period)
            
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
    parser = argparse.ArgumentParser(description='G-TECH: Long lasting green technology.')
    parser.add_argument(
        '--time',
        metavar='window_period',
        type=int,
        default=2,
        help='window period')
    args_dict = vars(parser.parse_args())

    return args_dict


if __name__ == '__main__':
    args_dict = input_argument()
    AW = AlwaysGreen(window_period=args_dict['time'])
    print(f'''----------------------------------------------''')
    print(f''':: Refresh Every: {args_dict['time']} S''')
    print(f'{logo}''')
    AW.run()
