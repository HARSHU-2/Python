# Read all lines from a file into a list. Print the total number of
# lines and display the 2nd and 4th line.
f = open("data.txt", "r")

lines = f.readlines()
print("Total lines:", len(lines))

f.seek(0)
f.readline()
print("2nd line:", f.readline())

f.seek(0)
f.readline()
f.readline()
f.readline()
print("4th line:", f.readline())

f.close()
