# Broken Bridge
# Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).

def is_safe_bridge(s):
	return " " not in list(s)

print(is_safe_bridge("## ####")) # False 
print(is_safe_bridge("###")) # True