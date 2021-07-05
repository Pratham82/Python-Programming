# Input: 
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

#* Working Approach
# Steps:
# 1. Take all the inputs
# 	1.1 Take an no. of shoes(int)
# 	1.2 Take list of shoes_sizes(string) eg. ('1 2 5 4')
# 	1.3 Take a count of customers (int)
# 	1.4 Take a shoe size corresponding to price for each customer line by line till no. of customers (string )

# 3. Add the price in the global counter and Remove the shoe size from the list of shoe_sizes if the i/p from 1.4 contains the shoe size from shoes_sizes listo
len_of_shoes = int(input())
shoes_sizes_list = input().split()
customer_count = int(input())
customer_shoe_sizes = []
profits = 0
for i in range(customer_count):
	customer_shoe_sizes.append(input().split())

for i in customer_shoe_sizes:
  # Check if the customer_shoe_sizes's 0th element is present in shoe_sizes_list
  # print(shoes_sizes_list)
  if i[0] in shoes_sizes_list:
    profits += int(i[1])
    shoes_sizes_list.remove(i[0])

print(profits)

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(Counter(myList))

# l1 = "2 3 4 5 6 8 7 6 5 18"

# ------------------------ Brain storming------------------------------
# Taking input
# Shit storm
# shoes_len = int(input())
# shoes_list = list((map(lambda n: int(n), input().split(" "))))
# customer_len = int(input())
# main_count = Counter(shoes_list)
# desired_shoes = []
# a = 0
# for i in range(customer_len):
#     desired_shoes.append(input())

# new_desired_shoes = list(map(lambda n: n.split(" "), desired_shoes))
# profits = 0
# for i in range(len(new_desired_shoes)):
#     if int(new_desired_shoes[i][0]) in shoes_list:
#         print(new_desired_shoes[i][1])
#         profits += int(new_desired_shoes[i][1]) 
#         # Remove the values from shoe_list if
#         if new_desired_shoes[i][0] in shoes_list:
#             shoes_list.remove(new_desired_shoes[i][0])
#     # print(new_desired_shoes[i][0])

# # for i in range(len(desired_shoes)):
# #     print(desired_shoes[i][0])

# print(profits)
# shoes_list.remove(6)
# print(shoes_list)


# print(f'customer_len= {customer_len}\n shoes_list = {shoes_list}\n shoes_len ={shoes_len}\n') 
# print(new_desired_shoes)


