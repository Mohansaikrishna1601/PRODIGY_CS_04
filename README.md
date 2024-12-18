# Keylogger

## Description
This Python script implements a simple keylogger using the `pynput` library. The keylogger captures and logs keystrokes, including both character keys and special keys, to a specified log file.

## Features
- Keystroke Logging: Captures all keystrokes, including both character keys and special keys, and logs them to a file.
- Real-time Logging: The keylogger runs in real-time, continuously monitoring and recording keystrokes.
- Graceful Termination: The script can be stopped gracefully using `Ctrl+C`.

## How It Works
- Keyboard Listener: Utilizes the `pynput.keyboard.Listener` class to monitor and capture keystrokes.
- Log File: Stores captured keystrokes in a file (`keystrokes.txt`) for later review.
- Event Handling: Handles both character keys and special keys, logging them appropriately.

## Code Explanation
- log_file: Specifies the file where keystrokes will be logged.
- on_key_press(key):
  - Character Keys: Logs the character pressed.
  - Special Keys: Logs special keys (e.g., `Shift`, `Ctrl`, `Enter`).
- Listener Initialization:
  - Start the Listener: Begins capturing keystrokes.
  - Listener Join: Keeps the listener running until `Ctrl+C` is pressed.
  - Graceful Termination: Stops the listener and exits the script gracefully upon `Ctrl+C`.

## Usage
### Clone the Repository
 
    git clone https://github.com/Mohansaikrishna1601/PRODIGY_CS_01.git 
    cd PRODIGY_CS_01 

### Run the Script

      python Keylogger.py


### Stop the Keylogger:
  Press Ctrl+C to stop the keylogger gracefully.

### Requirements:  
Python 3.x

pynput library

## Author:
  Mohan Sai Krishna G M



