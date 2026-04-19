# Rather than using print statements for debugging we can use python's own module
# debugging which is pdb module. The pdb module implements an interactive 
# debugging environment for Python programs.you pause your program, look at the 
# values of variables, and watch program execution step-by-step

import pdb

l1 = [12,445,6,664,32]
v1 = 231
v2 = 232
print(v1+v2)

# Purposely making an error
# Here we are calling an interactive debugging environment 
# Set a trace using Python Debugger
pdb.set_trace()
print(v1+l1)

# use q for quitting from a debugging environment

