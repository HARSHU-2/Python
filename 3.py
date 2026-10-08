# Accept two values S and N. Print square of first N numbers starting from S.
S = int(input("Enter Starting Number:"))
N = int(input("Enter N:"))

for i in range(S, S+N):
    print(i ** 2)
