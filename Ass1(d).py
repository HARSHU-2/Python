# Read a file, split its content into words, and store them in a list.
# i. Print the total number of words.
# ii. Print all unique words.
f = open("data.txt", "r")
content = f.read()

words = content.split()

print("Total words:", len(words))

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique Words:", unique_words)
f.close()
