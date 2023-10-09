def calculatearea(height, width, coverage):
    numcans = (height * width) / coverage
    if numcans % 1 != 0:
        numcans = int(numcans) +1
    else:
        numcans = int(numcans)

    print(f"You will need {numcans} cans in order to paint this wall")

inputheight = int(input("Enter the HEIGHT of the wall in meters: "))
inputwidth = int(input("Enter the WIDTH of the wall in meters: "))
coverage = 5

calculatearea(inputheight, inputwidth, coverage)