
# AlwaysGreen: Prevent Inactivity and Stay Active!

## Overview

The `AlwaysGreen` tool prevents system inactivity by simulating mouse movements. It ensures that screensavers, timeouts, or auto-lock mechanisms do not activate while the user is away or during specific exempted periods.

This script is helpful for:
- Preventing inactivity during long-running tasks.
- Avoiding auto-logout due to system timeouts.

---

## Key Features

1. **Activity Detection**:
   - Monitors mouse and keyboard actions using the `pynput` library.

1. **Timeout-Based Activity**:
   - Simulates activity after a user-defined period of inactivity.

2. **Exempted Periods**:
   - Define time windows where the system will not enforce activity.

3. **Modern Output**:
   - Optional colored and emoji-based status outputs.

4. **Customizable Settings**:
   - Timeout duration
   - Logo display
   - Status and exempt period visibility

5. **Real-Time Feedback**:
   - Outputs activity status in real-time, with optional colored text for better visibility.

6. **User-Friendly Command-Line Interface**:
   - Use command-line options to customize behavior.

7. **Keyboard Interrupt Handling**: Graceful termination with `CTRL-C`.


---

## How It Works

1. **Initialization**:
   - The script initializes with customizable parameters, including timeout duration, status visibility, colored output, and logo display.

2. **Event Listeners**:
   - Monitors mouse and keyboard events to detect user activity and reset the inactivity timer.

3. **Mouse Movement**:
   - Moves the mouse and simulates a click to maintain system activity when no user input is detected.

4. **Continuous Monitoring**:
   - Runs indefinitely, alternating between monitoring inactivity and simulating activity.

---

## Usage

Run the script from the command line:

```bash
python app.py [OPTIONS]
```

### Command-Line Arguments

|       Argument      	| Default 	|                           Description                          	|
|:-------------------:	|:-------:	|:--------------------------------------------------------------:	|
|  --time             	| 5       	| Timeout period in   seconds before inactivity action is taken. 	|
| --classic           	| Disabled 	| Enable classic   (non-colored) output mode.                    	|
| --no-logo           	| Disabled 	| Disable the display of   the logo.                             	|
| --no-exemped-period 	| Disabled 	| Disable the display of   exempt periods.                       	|
| --no-status         	| Disabled 	| Disable the display of   user activity status.                 	|

---

## Example
Run with default settings:

```bash
python app.py
```

Run with a 10-second timeout and no colored output:

```bash
python AlwaysGreen.py --time 10 --classic
```

Run without displaying exempt periods or the logo:

```bash
python AlwaysGreen.py --no-logo --no-exemped-period
```

---

## Dependencies

- **pynput**: A library for controlling and monitoring mouse and keyboard events.
  - Install using: `pip install pynput`

---

## Exempted Periods

Define custom exempted periods within the code to prevent enforced activity during specific times.

```Python
exempted_periods = [
    ('12:00:00', '13:00:00'),  # Lunch break
    ('17:00:00', '18:00:00'),  # Evening break
]
```

---

## Output Example

The script displays activity status dynamically:

Default Mode

```
| ENFORCED | Inactive in     5s | Status:🟡 |
```
Classic Mode
```
| ENFORCED | Inactive in     5s | #INACTIVE |
```


---

## References

This script was inspired by and utilizes concepts from the following sources:

1. [pynput library on PyPI](https://pypi.org/project/pynput/)
2. [How to Make a Python Auto Clicker - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/)
3. [ASCII Art Generator - asciiart.eu](https://www.asciiart.eu/text-to-ascii-art)
4. [Print Colors in Python Terminal - GeeksforGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)


---

## License

This script is free to use and modify. Contributions are welcome!

