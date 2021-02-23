"""
Name:       problem1.py
Description:    The program allows a user to input three side lengths. The program will compute and output whether or not the figure is a triangle. 

Author:         Lauren M

Created:     23/02/2021
"""

print ("Welcome to the Triangle Checker")

#The user will input three side lengths
length_one = int(input("Enter the length of the first side: "))
length_two = int(input("Enter the length of the second side: "))
length_three = int(input("Enter the length of the third side: "))

#The program will compute and output whether or not the three side lengths make a triangle
if (length_one + length_two > length_three) and (length_one + length_three > length_two) and (length_two + length_three > length_one):
  print ("The figure is a triangle")

else:
  print ("The figure is NOT a triangle")