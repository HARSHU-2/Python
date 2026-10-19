# Write a program to read a file and count how many vowels are
# present in its content.
f = open("Sum.py", "r")
content = f.read()
count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1
f.close()

print("Number of vowels:", count)
