# Use only 1 line of code to square each number in the list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num*num for num in numbers]

print(squared_numbers)

# Use only 1 line of code, filter the even numbers in the list

even_numbers = [num for num in numbers if num%2 == 0]

print(even_numbers)