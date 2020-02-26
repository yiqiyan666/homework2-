
import os.path
def count_char(fn):
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            for line in fh:
                total += len(line)
            return total


fn = "unit2/readme.md"
fh = open(fn, "r").read()

if os.path.isfile(fn):
    words_num = len(fh.split())
    print('There are {} words in file {}'.format( words_num ,fn))
else:
    print('The file does not exist')