# Checking multiple conditional statements using list

phones = 300
laptops = 350
desktops = 400
all_in_ones = 450

# if phones >299 and laptops >310 and desktops >350 and all_in_ones >400:
#     print("Inventory is stocked up.")

inventory =[phones>299,
            laptops>310,
            desktops>350,
            all_in_ones>400
            ]
# Use all() for and condtion and any() for or conditon

if all(inventory):
    print("Inventory is stocked up.")
