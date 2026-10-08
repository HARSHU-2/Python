# Print sum of even numbers
def index(a):
    sum = 0
    for i in range(0, len(a), 2):
        sum += a[i]
    return sum


a = [10, 20, 30, 40, 50]
print("Sum of even index numbers:", a)
