import os
import sys
import subprocess
import re


def parse_input(submission_file):
    f = open(submission_file, "r")
    git_rep = ""
    ids = ""
    commit = ""
    try:
        for line in f.readlines():
            if 'git' in line:
                git_rep = line
                continue
            elif re.search(r'\b\d{9}', line):
                ids = line
                continue
            elif re.search(r'.+', line) and "/" not in line:
                commit = line
                continue
    except UnicodeDecodeError as e:
        print(e)
    return git_rep.strip(), ids.strip(), commit.strip()


def main():
    git_rep, ids,  commit = parse_input(sys.argv[1])
    print (f"git repository is: {git_rep}")
    print (f"IDs are: {ids}")
    print (f"Commit: {commit}")

if __name__ == "__main__":
    main()
