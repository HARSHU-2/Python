# create a list of 10 numbers. Print the sum of last 4 elements of the list.
# Find out the difference between max and min element of the list. Insert a
# number in the list at 6th position. This number must be 1/3rd of number
# stored at 4th position

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Sum of last 4 elements:", sum(numbers[-4:]))
print("Difference:", max(numbers) - min(numbers))

number = numbers[3] / 3
numbers.insert(5, number)

print("Updated list:", numbers)
