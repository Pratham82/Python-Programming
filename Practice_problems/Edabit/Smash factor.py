# Smash Factor
# Smash factor is a term in golf that relates to the amount of energy transferred from the club head to the golf ball. The formula for calculating smash factor is ball speed divided by club speed.

# Create a function that takes ball speed bs and club speed cs as arguments and returns the smash factor to the nearest hundredth.

def smash_factor(bs, cs):
	return round(bs / cs,2)


print(smash_factor(139.4, 93.8))