scores = [90, 20,40, 60, 112, 32,523, 234,456,3,56,123,7,4,3,]
highest = 0

for i in scores:
    if i > highest:
        highest = i

print(scores)
print("The highest score from the class is: ", highest)