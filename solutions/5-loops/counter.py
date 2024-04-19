# Given a number, print all the numbers from 0 to your number.
# For example:
# -> if 'num' is 5, then we print 0, 1, 2, 3, 4, 5
# -> if 'num' is -5, then we print 0, -1, -2, -3, -4, -5

#####################################################################
def main():
    num = int(input("Enter your number: "))

    # If 'num' is bigger or equal to 0, count in increasing order
    if num >= 0:
        count = 0
        while count <= num:
            print(count)
            count += 1

    # If 'num' is smaller than 0, count in decreasing order
    if num < 0:
        count = 0
        while count >= num:
            print(count)
            count -= 1

#####################################################################
main()