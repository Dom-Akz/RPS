# read keybaord log from a file and convert it to a readlble text (skip stuff like volumeup or delete button)


LOG_PATH = "/home/soufiane/.local/share/keylogger/kb.log"
OUT_FILE = "/home/soufiane/.local/share/keylogger/d-kb.txt"

# skip them when decoding
SP_CAHR = [
    "UP",
    "LEFT",
    "RIGHT",
    "DOWN",
    "LEFTSHIFT",
    "LEFTCTRL",
    "RIGHTCTRL",
    "RIGHTALT",
    "HOME",
    "DELETE",
    "GRAVE",
    "END",
    "ESC",
    "PAGEUP",
    "MINUS",
    "PAGEDOWN",
    "VOLUMEUP",
    "VOLUMEDOWN",
    "APOSTROPHE",
    "SWITCHVIDEOMODE",
    "MICMUTE",
    "VOLUMEMUTE",
    "BRIGHTNESSUP",
    "BRIGHTNESSDOWN",
    "RIGHTBRACE",
    "LEFTBRACE",
    "LEFTMETA",
    "LEFTBRACETAB",
    "SEMICOLON",
    "102ND",
    "BACKSLASH",
]


# helper to get the char
# format example:  key press: KEY_UP
def decode(line):
    new_line = line.split("_")

    if new_line[1] in SP_CAHR:
        return ""

    # check if it a SPACE/ENTER/BACKSPACE
    if new_line[1] == "SPACE":
        return " "
    if new_line[1] == "ENTER":
        return "\n"
    if new_line[1] == "BACKSPACE":
        return "BACKSPACE"
    if new_line[1] == "DOT":
        return "."
    if new_line[1] == "SLASH":
        return "/"
    if new_line[1] == "COMMA":
        return ","
    if new_line[1] == "EQUAL":
        return "="

    return new_line[1]


def f_write(content):
    with open(OUT_FILE, "w") as file:
        file.write(content)


def main():
    import os

    # check if every file exist
    if not os.path.exists(LOG_PATH):
        print(f"Error: try creating {LOG_PATH} first")
        exit(1)
    if not os.path.exists(OUT_FILE):
        print(f"Error: try creating {OUT_FILE} first")
        exit(1)

    with open(OUT_FILE, "r") as f:
        out_file = f.read()

    with open(LOG_PATH, "r") as logs:
        if not logs:
            print("Error: logs are empty")
            exit(1)

        for log in logs:
            log = log.strip()
            if "key press" not in log:
                continue

            ch = decode(log)
            if ch == "BACKSPACE":
                # take the last caracter out
                if out_file:
                    f_write(out_file[:-1])
            else:
                out_file += ch.lower()
                f_write(out_file)

    print(f"log has been decode see {OUT_FILE}")


if __name__ == "__main__":
    main()
