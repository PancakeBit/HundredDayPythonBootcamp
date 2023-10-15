# Don't change this code
row1 = ["🟫", "🟫", "🟫"]
row2 = ["🟫", "🟫", "🟫"]
row3 = ["🟫", "🟫", "🟫"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?: ")
# Don't change this code

#This code works too
#x = int(position[0]) -1
#y = int(position[1]) -1
#map[x][y] = "X"

map[int(position[0]) -1][int(position[1]) -1] = "X"

print(f"{row1}\n{row2}\n{row3}")