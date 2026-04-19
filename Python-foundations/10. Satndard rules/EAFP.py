# Process file; EAFP
''' 
1. EAFP is standard in python. 
2. EAFP is enabled by exceptions.
3. Without exceptions, error handling is interspersed in program flow.
4. Exceptions can be handled locally 
5. Exceptions are not easily ignored
6. Error codes are silent by default
7. Exceptions plus EAFP makes it hard fpr problems to be silently ignored.

'''

p= '/path/to/datafile.data'

try:
    process_file(f)
except OSError as e:
    print('Error: {e}')