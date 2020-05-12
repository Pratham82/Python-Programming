'''
Perpare for failure
1. Check for preconditions
2. Prepare for consequences

LBYL: Look before you leap
EAFP: Easier to Ask Forgiveness than Permission
'''

# Precessing a file
# Processing details are not important. process_file() opens a file and reads it

# Process file: LBYL

import os

p= '/path/to/datafile.dat'

if os.path.exist(p):
    process_file(p)
else:
    print(f'No such file as {p}')