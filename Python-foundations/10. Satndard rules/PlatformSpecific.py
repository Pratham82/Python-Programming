# keypress- a module for detecting a single keypresss 

try:
    import msvcrt

    def getKey():
        # Wait for a keypress and return a single character string.
        return msvcrt.getch()

except ImportError:
    import sys
    import tty
    import termios

    def getKey():
        # Wait for a keypress and return a single character string 

        fd = sys.stdin.fileno()
        original_attributes =termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        
        finally:
            termios.tcgetattr(fd,termios.TCSADRAIN,original_attributes)
        return ch

# If either of the unix specific tty or termios are not found, 
# We allow the ImportErrror to propagate from here