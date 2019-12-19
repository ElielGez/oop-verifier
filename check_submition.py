import os
import sys
import subprocess
import re


def parse_input():
    submission_file = sys.argv[1]
    f = open(submission_file, "r")
    for line in f.readlines():
        if re.search(r'\.git', line):
            git_rep = line
            continue
        if re.search(r'\b\d{9}[\s_\Z]', line):
            ids = line
            continue
        if re.search(r'.+', line):
            commit = line
            continue
    return git_rep, ids, commit


def main():
    git_rep, ids,  commit = parse_input()
    print ("git repository is: " + git_rep.strip())
    print ("IDs are: " + ids.strip())
    print ("Commit: " + commit.strip())


if __name__ == "__main__":
    main()
