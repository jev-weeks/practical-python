# bounce.py
#
# Exercise 1.5
"""
Above is from dabeaz; below is mine.

A rubber ball is dropped from a height of 100 meters and each time it
hits the ground, it bounces back up to 3/5 the height it fell. Write a
program bounce.py that prints a table showing the height of the first
10 bounces - round to four places.
"""

height = 100 # Imitial value in meters.

for i in range(10):
    height = height * (3 / 5)
    print(i + 1, round(height, 4))
