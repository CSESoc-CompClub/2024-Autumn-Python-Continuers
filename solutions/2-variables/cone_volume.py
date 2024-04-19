
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Variables!               #
#************************************#

PI = 3.14159265359

# You are given two variables 'radius' and 'height' which are radius and height of a cone. 
# Using the formula ( Pi* r^2 *h)/3, can you find the volume of the cone? 
# Print the height, radius and volume, rounded to the nearest whole number.

# Hint: Do you remember what data type we use for decimals?

def main():
    radius = float(input("Radius of the cone = "))
    height = float(input("Height of the cone = "))
    res = PI * (radius ** 2) * height / 3
    print("%.2f" % res)

#################################################
main()
