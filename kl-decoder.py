# read keybaord log from a file and convert it to a readlble text

import os

LOG_PATH = "/home/soufiane/.local/share/keylogger/kb.log"
OUT_FILE = "/home/soufiane/.local/share/keylogger/d-kb.txt"


# helper to get the char
# format example:  key press: KEY_UP
def decode(line):
    new_line = line.split(":")

    # check if it a SPACE/ENTER/BACKSPACE
    if new_line[0] == "SPACE":
        return " "
    elif new_line[0] == "ENTRE":
        return "\n"

    if new_line[0] == "BACKSPACE":
        return "BACKSPACE"

    return new_line[0]


def main():
    # check if every file exist
    if not os.path.exists(LOG_PATH):
        print(f"Error: try creating {LOG_PATH} first")
        exit(1)
    if not os.path.exists(OUT_FILE):
        print(f"Error: try creating {OUT_FILE} first")
        exit(1)

    # load log
    with open(LOG_PATH, "r") as log_file:
        logs = log_file.read()

    # what is the best approche (with inside loop or the opposite)
    with open(OUT_FILE, "rw") as out_file:
        for log in logs:
            ch = decode(log)
            # check if the ch is SPACE/ENTRE/BACKSPACE
            if ch == "BACKSPACE":
                # take the last caracter out
                pass
            else:
                out_file.write(ch)

    print(f"log has been decode see {OUT_FILE}")


if __name__ == "__main__":
    main()

