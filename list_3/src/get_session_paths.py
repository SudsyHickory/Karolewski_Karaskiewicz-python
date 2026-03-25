import sys
from common_tools import *

def get_session_paths(log):

    session_paths = {}

    for entry in log:

        uid = entry[IDX_UID]
        uri = entry[IDX_URI]

        if uid not in session_paths:
            session_paths[uid] = []

        if uri is not None and uri != "-" and uri != "":
            session_paths[uid].append(uri)

    return session_paths

def main():

    try:
        log = read_log()
        session_paths = get_session_paths(log)

        for uid, paths in session_paths.items():
            sys.stdout.write(str(uid) + " " + str(paths) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()