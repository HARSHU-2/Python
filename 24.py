# Write a function sum_of_evens(numbers) that takes
# a list of integers and returns the sum of only the even numbers.
def sum_of_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num

    return total


print(sum_of_even([1, 3, 4, 2, 8, 10, 12]))

# Write a function count_positives(numbers) that takes a list of integers
# and returns the total count of numbers greater than 0.


def count_positives(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count


print(count_positives([-2, 5, 0, 8, -1, 3]))

# Write a function count_vowels(text) that takes a string and returns
# the total count of vowels (a, e, i, o, u), case-insensitively.


def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))

#  Write a function square_odds(numbers) that takes a list of integers
# and returns a new list containing the squares of only the odd numbers.


def square_odds(numbers):
    squares = []
    for num in numbers:
        if num % 2 != 0:
            squares.append(num * num)
    return squares


print(square_odds([1, 2, 3, 4, 5]))

# Write a function word_lengths(words) that takes a list of strings and returns
#  a *dictionary* where each word is a key and its length is the value.


def word_lengths(words):
    result = {}

    for word in words:
        result[word] = len(word)

    return result


words = ["apple", "bat", "cherry"]
print(word_lengths(words))

# Write a function passed_students(scores) that takes a dictionary where keys
#  are student names and values are their marks. The function should return
#  a *list* containing only the names of students who scored *50 or more*.


def passed_students(scores):
    passed = []

    for name, marks in scores.items():
        if marks >= 50:
            passed.append(name)

    return passed


scores = {"Amit": 45, "Sara": 78, "Raj": 52, "Pooja": 39}
print(passed_students(scores))

# Write a function count_letters(word) that takes a string and returns
# a dictionary where each letter is a key and its frequency count is the value.


def count_letters(word):
    count = {}

    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    return count


print(count_letters("banana"))

# Write a function min_max_sum(numbers) that takes a list of numbers
# and returns a tuple containing three values in this exact order:
# The minimum number
# The maximum number
# The sum of all numbers
# (You can use built-in functions min(), max(), and sum())


def min_max_sum(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)

    return (minimum, maximum, total)


numbers = [10, 5, 20, 15]
print(min_max_sum(numbers))

# Write a function sum_all(*args) that accepts any number of arguments,
# adds up only the numbers (int and float), and returns the total sum.
# (Make sure to exclude booleans, because in Python type(True) is considered
# an int unless explicitly excluded).


def sum_all(*args):
    total = 0

    for value in args:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            total += value

    return total


print(sum_all(10, 20, "hello", 5.5, True, [1, 2]))
