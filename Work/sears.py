"""
This is dabeaz's work, not mine. I did type it myself, and that's really
something. It solves the following problem:

One morning, you go out and place a dollar bill on the sidewalk by the
Sears tower in Chicago. Each day thereafter, you go out and double the 
number of bills. How long does it take for the stack of bills to exceed 
the height of the tower?

I must say, as a non-Chicagoan, I don't know how tall the Sears tower is,
so when this runs I have questions like, "did it work," and "did that
do it?"

"""

bill_thickness = 0.11 * 0.001 # In meters (0.11 mm)
sears_height = 442 # Building height in meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
