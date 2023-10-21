# Cannot properly do this exercise because the appbrewery page is locked
# Will try anyway

# Make a list called 'result' that contains
# the numbers that are common in both file1.txt and file2.txt

with open('file1.txt') as file1:
    new_list1 = file1.read().split()
    print(new_list1)

with open('file2.txt') as file2:
    new_list2 = file2.read().split()
    print(new_list2)

# Wrote this code for nothing I guess
# This will be needed if we want to make sure to check ALL values within both files
# This will return many duplicate values though, the code snippet below already returns multiple same values
# if len(new_list2) >= len(new_list1):
#     longerlist = new_list2
# else:
#     longerlist = new_list1

alikeelements = [int(item) for item in new_list1 if (item in new_list2 and item in new_list1)]
print("Alike elements are: ", alikeelements)