"""
Name:       problem1.py
Description:    Compute the list of aliens who match the criteria inputted 

Author:         Lauren M

Created:     23/02/2021
"""
#The user will input the number of eyes and antenna
num_antenna = int(input("Enter the number of antenna: "))
num_eyes = int(input("Enter the number of eyes: "))

#The number of antenna and eyes for the list of aliens
AudreyMartian = num_antenna >=3 and num_eyes <=4
MaxMartian = num_antenna <=6 and num_eyes >=2
BrooklynMartian = num_antenna <=2 and num_eyes <=3
MattDamonMartian =  num_antenna == 0 and num_eyes == 2

#The program will compute the type of alien based on the inputted numbers
if num_antenna >=3 and num_eyes <=4:
  print ("Life form detected: AudreyMartian")

if num_antenna <=6 and num_eyes >=2:
  print ("Life form detected: MaxMartian")

if num_antenna <=2 and num_eyes <=3:
  print ("Life form detected: BrooklynMartian")

if num_antenna == 0 and num_eyes == 2:
  print ("Life form detected: MattDamonMartian")

elif not AudreyMartian and not MaxMartian and not BrooklynMartian and not MattDamonMartian:
  print ("No life form detected")