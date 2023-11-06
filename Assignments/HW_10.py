# Homework for Lectures 17 & 18
# Rename the file as HW_10_YOURNAME.py

##----------------------------Dictionary operator and methods ---------------------------
# Question 1: There are five small, related questions (A-E).

'''
A: Create a Car Inventory System, named car_inventory. You work for a vintage car dealership, 
    and you have been tasked with creating an inventory system to track the cars in the showroom. 
    Each car has a unique ID, with details like brand, model, and year.
TODO: Create a dictionary for a car: id: VIN1234567890, brand: Porsche, model: 911, year: 1965
        Print it out.
'''
print("QUESTION 1.A")
# write your code below




'''
B: Update the Inventory. A car enthusiast is interested in a Porsche 911 from 1965 but also wants 
    to know if it comes in red and what its price is. 
    However, this information is missing from your current records.
TODO: Update the car dictionary, car_inventory, from Question 1 to include color and price keys with values 
    "red" and "$100,000" respectively, and print the updated dictionary.
    a) ONLY use [] operator
    b) ONLY use update() method
'''
print("QUESTION 1.B")
# write your code below




'''
C: Re-arrange the Inventory, create a nested dictionary, new_car_inventory. For the outer dictionary, 
    uses a car's ID as a key, whose value is an inner dictionary containing brand, model, year as the keys. 
    reuse the info listed in car_inventory in Question 1. 
    Print the updated Inventory. You should see something like this:
    {VINxxx: {brand:xxx, model:xxx, year:xxx, color:xxx, price:xxx}}
'''
print("QUESTION 1.C")
# write your code below





'''
D: Add a new car to the Inventory, new_car_inventory. The dealership acquires a rare 1964 Ford Mustang 
    that you need to add to the inventory system.
TODO: Add another inner dictionary inside the Inventory, new_car_inventory:
    brand: Ford, model: Mustang, color: black, price: $50,000, year:1964 of ID "VIN0987654321".
    Print the updated Inventory with two cars inside. You should see something like this:
    {VINxxx: {brand:xxx, model:xxx, year:xxx, color:xxx, price:xxx},VINyyy: {brand:yyy, model:yyy, year:yyy,color:yyy, price:yyy}}
'''
print("QUESTION 1.D")
# write your code below





'''
E: Remove a car from the Iventory, new_car_inventory. Good news! Your Porsche 911 has been sold. 
    Now, you need to update the inventory to reflect this sale.
TODO: Remove the "price" key from the Porsche 911's dictionary because the car's sale price is confidential.
    Print the dictionary after the removal of the price information.
'''
print("QUESTION 1.E")
# write your code below





##----------------------------Iterating a dictionary ---------------------------
'''
Question 2: You are responsible for tracking the growth of trees planted in the school yard. The dictionary below 
    contains the tree species and their height in feet. After a year, it's time to measure them again, and you 
    expect every tree has grown by 10%. 
TODO: Update the heights and print out which trees have reached over 15 feet tall after updating.
NOTE: Use a for loop to iterate each item in the dictionary and update the values as needed.
'''
print("QUESTION 2")
trees = {
    "Oak": 12.1,
    "Maple": 15.5,
    "Birch": 9.8,
    "Cherry": 13.9
}
# write your code below


