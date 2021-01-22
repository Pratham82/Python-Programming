stop = '-'*10

# Normal Pyramid
[print(i * '*') for i in range(1,6)]
print(stop)

# Reversed Pyramid
[print('*' * i) for i in range(5, 0, -1)]
print(stop)

# Print pyramid with numbers
[print(i * f'{i}')   for i in range(1,6) ]
print(stop)

# Print reverse pyramid with numbers
[print(i * f'{i}')   for i in range(5, 0, -1) ]
print(stop)

# Print  pyramid with one # and one *
[ print('*' * i) if i % 2 ==0 else print('#' * i) for i in range(1,6) ]
print(stop)

# Print reversed  pyramid with one # and one *
[ print('*' * i) if i % 2 ==0 else print('#' * i) for i in range(5,0,-1) ]
print(stop)

#for i in range(1,7):
#    for j in range(1, i):
#        print(j, end='')
#    print(' ')
#
#print(stop)

# [ print(j, end='')  for i in range(1,7)  for j in range(1,i)  ]

print('\n'.join(''.join(str(j) for j in range(1,i)) for i in range(1,7) ))
print(stop)

print('\n'.join(''.join(str(j) for j in range(i,7)) for i in range(1,7) ))
print(stop)

print( '\n'.join( ''.join('*' if j % 2 ==0 else '#' for j in range(1,i) ) for i in range(1,7) ))
print(stop)

print( '\n'.join( ''.join('*' if j % 2 ==0 else '#' for j in range(i,7) ) for i in range(1,7) ))
print(stop)

# Output: 
# *
# **        
# ***       
# ****      
# *****     
# ----------
# *****     
# ****      
# ***       
# **        
# *
# ----------
# 1
# 22        
# 333       
# 4444      
# 55555     
# ----------
# 55555     
# 4444      
# 333       
# 22        
# 1
# ----------
# #
# **        
# ###       
# ****      
# #####
# ----------
# #####
# ****
# ###
# **
# #
# ----------

# 1
# 12
# 123
# 1234
# 12345
# ----------
# 123456
# 23456
# 3456
# 456
# 56
# 6
# ----------

# #
# #*
# #*#
# #*#*
# #*#*#
# ----------
# #*#*#*
# *#*#*
# #*#*
# *#*
# #*
# *
# ----------

