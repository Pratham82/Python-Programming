try:
    f = open('test.txt','r')
    f.write("Write in a test file")

# Every These will check for specific exceptions
# But if we want all in one exception we can use the parent exception similar to java using only except
# It will automatically checks which kind of exception presents 
# This default except must be written in the last after specific exceptions

except TypeError:
    print("TypeError found while execution")

except:
    print("OSError found while execution")

finally:
    print("This is finally block")

    
