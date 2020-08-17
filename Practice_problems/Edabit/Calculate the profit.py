# Calculate the Profit
# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar.

# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796








def profit(info):
	return round((info['sell_price'] * info['inventory']) - info['cost_price']*info['inventory'])


print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))

print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))

print(profit({'cost_price': 19.87, 'sell_price': 110.00, 'inventory': 350}))