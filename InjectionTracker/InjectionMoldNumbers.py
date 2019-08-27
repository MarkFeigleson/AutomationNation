
# create a list to get sums from for
# good pieces and scrap
dailyTotal = []
scrapLeftTotal = []
scrapRightTotal = []

# getting an increasing integer to limit the number of loops
count = 0


# function to give me hourly statistics
def hourly():
    print(hourlyTotal, " total for hour")
    # The number divided by half will tell me how many are on left and right side
    print((hourlyTotal * .5), "per side")
    # adding to the list
    dailyTotal.append(hourlyTotal)

    # message about performance
    if hourlyTotal == 90:
        print("On target")
    elif hourlyTotal >= 91:
        print("Check the cycle time to see if the machine is running too fast")
    else:
        print("Be sure to check downtime numbers")


# this asks for scrap count and records it

def scrapCheck():
    scrapHour = input("Did you have scrap? Yes or No ").lower()

    if scrapHour == "yes" or "y":

        leftScrap = float(input("How many left side pieces? "))

        rightScrap = float(input("How many right side pieces? "))

        scrapLeftTotal.append(rightScrap)

        scrapRightTotal.append(leftScrap)

    else:
        print("Great!")

#this totals up the scrap for the day on each side

def sumCollection():
    dailySum = sum(dailyTotal)

    leftSum = sum(scrapLeftTotal)

    rightSum = sum(scrapRightTotal)

    print(str(dailySum) + ("  total pieces today."))

    print(str(leftSum) + " total left hand scrap pieces")
    print(str(rightSum) + " total right hand scrap pieces")


# user input to begin program.repeat 8 times
for i in range(8):
    count = count + 1

    hourlyTotal = float(input("Hour " + str(count) + "'s numbers? "))

    scrapCheck()

    hourly()

    sumCollection()

