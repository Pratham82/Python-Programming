# Date Format
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

def format_date(date):
	# val = 
	return "".join(list(reversed(date.split("/"))))

print(format_date("11/12/2019"))