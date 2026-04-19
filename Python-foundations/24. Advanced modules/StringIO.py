#String IO objects and io module
# You can create in-memory file-like objects within your program
# Text data is stored in a StringIO object, while binary data would be stored in a BytesIO object. 
# This object can then be used as input or output to most functions that would expect a standard file object.
# application: when we are scaping text from the web

import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

# Now we have an object f that we will be able to treat just like a file.

print(f.read())
f.seek(0)

# We can perform most of the file methods with this object
f.write('Second line written to file like object')
f.read()

# Close the object when contents are no longer needed
f.close()



