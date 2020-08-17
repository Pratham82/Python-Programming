# You FAILEDPASSED the Exam

# You FAILEDPASSED the Exam Required mark is 85% Your score 85%

# The challenge is to fix all of the bugs in this incredibly messy code, which the code in the image might've actually looked like (probably not)! The code given will output the same middle two lines as in the image shown above.

# First parameter is the user's score.
# Second parameter is the required score.

def grade_percentage(user_score, pass_score):
	s=''
	if int(user_score[:-1])< int(pass_score[:-1]) :
		s=s+'FAILED'
	if int(user_score[:-1])>= int(pass_score[:-1]) :
		s=s+'PASSED'
	return 'You' + ' ' + s + ' ' + 'the Exam'


print(grade_percentage("85%", "85%"))

print(grade_percentage("99%", "85%"))

print(grade_percentage("65%", "90%"))