regex_pattern = r"M{,3}"	# Do not delete 'r'.

import re
# print(str(bool(re.match(regex_pattern, input()))))
print(bool(re.match(regex_pattern, input())))

