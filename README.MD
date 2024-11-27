
# AlwaysGreen: Prevent Inactivity and Stay Active!

## Overview

The **AlwaysGreen** Python script ensures your system remains active by detecting user input (mouse and keyboard activity) and automatically moving the mouse when inactivity is detected for a specified timeout period.

---

## Key Features

1. **Activity Detection**:
   - Monitors mouse and keyboard actions using the `pynput` library.

2. **Inactivity Prevention**:
   - Moves the mouse or performs a click to prevent system inactivity after a timeout.

3. **Customizable Options**:
   - Command-line arguments allow users to control the timeout period, status display, colored output, and logo display.

4. **Real-Time Feedback**:
   - Outputs activity status in real-time, with optional colored text for better visibility.

5. **User-Friendly Command-Line Interface**:
   - Use command-line options to customize behavior.

---

## How It Works

1. **Initialization**:
   - The script initializes with customizable parameters, including timeout duration, status visibility, colored output, and logo display.

2. **Event Listeners**:
   - Monitors mouse and keyboard events to detect user activity and reset the inactivity timer.

3. **Mouse Movement**:
   - Moves the mouse or simulates a click to maintain system activity when no user input is detected.

4. **Continuous Monitoring**:
   - Runs indefinitely, alternating between monitoring inactivity and simulating activity.

---

## Usage

Run the script from the command line:

```bash
python app.py --time 60 --color --status --logo
```

### Command-Line Arguments

- `--time`: Set the inactivity timeout in seconds (default is 5 seconds).
- `--color`: Enable colored status output (green for active, yellow for inactive). Use `--no-color` to disable.
- `--status`: Enable or disable activity status display. Use `--no-status` to hide status updates.
- `--logo`: Enable or disable the display of the logo. Use `--no-logo` to hide the logo.

---

## Dependencies

- **pynput**: A library for controlling and monitoring mouse and keyboard events.
  - Install using: `pip install pynput`

---

## Example Output

The script displays activity status dynamically:

```
::Inactive in     45s, ::User Status:   Active
```

With `--color` enabled, status messages are displayed in green or yellow for better visibility.

---

## References

This script was inspired by and utilizes concepts from the following sources:

1. [pynput library on PyPI](https://pypi.org/project/pynput/)
2. [How to Make a Python Auto Clicker - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/)
3. [ASCII Art Generator - asciiart.eu](https://www.asciiart.eu/text-to-ascii-art)
4. [Print Colors in Python Terminal - GeeksforGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)


---

## Visual Appeal

The script features an ASCII art logo for branding and visual appeal:

```
----------------------------------------------
||||||||||||||||||||||||||||||||||||||||||||||
----------------------------------------------
    ____           _____ _____ ____ _   _
   / ___|         |_   _| ____/ ___| | | |
  | |  _   _____    | | |  _|| |   | |_| |
  | |_| | |_____|   | | | |__| |___|  _  |
   \____|           |_| |_____\____|_| |_|

>>>>>>>>> :: Unleash Green Energy :: <<<<<<<<<
----------------------------------------------
|||||||||||| PRESS CTRL-C TO QUIT ||||||||||||
----------------------------------------------
```

---

## License

This script is free to use and modify. Contributions are welcome!

