# This week, we're going to spend a bit of time exploring a useful module in Python's standard library: argparse. This module allows you to create command-line programs that take arguments from the user.  You can, of course, do that with sys.argv, but then you need to parse the arguments yourself. argparse does a lot of that work for you.

# For this week's exercise, I want you to implement a single program that combines two classic Unix command-line programs, "head" and "tail".  The "head" command shows you the first few lines of a file, and the "tail" command shows you the final two lines of a file. Our "headtail" program will show you the first few *and* the last few lines of a file. If the user doesn't specify the number of lines he or she wants to see from the start and end, then the default number will be 3.

# For the purposes of this exercise, we'll assume that the file can fit into memory.

# The program will take one positional argument, a filename.

# It'll also take two keyword arguments:
# -s or --start, indicating how many lines to show from the start (default = 3)
# -e or --end, indicating how many lines to show from the end (default = 3)

import argparse


def main(file_name, start, end):
    print(f"Open {file_name} - show {start} at beginning and {end} at end")
    start, end = int(start), int(end)
    with open(file_name, 'r') as f:
        all_lines = f.readlines()

    print(f'Starting {start} line(s)')
    if start > 0:
        for i in range(start):
            print(all_lines[i])

    print(f"#### Ending {end} line(s)")
    if end > 0:
        loop_start = len(all_lines) - end
        for i in range(loop_start, loop_start + end):
            print(all_lines[i])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Head or Tail of a file.')
    parser.add_argument('-s', '--start', dest='start', metavar='X', type=int, default=0,
                        help='the number of lines at the beginning of the file to show')
    parser.add_argument('-e', '--end', dest='end', metavar='Y', default=0,
                        help='the number of lines at the end of the file to show')
    parser.add_argument('filename', help='the file to read')

    args = parser.parse_args()
    main(args.filename, args.start, args.end)