# Accept sentence from user and count vowels.
s = input("Enter Sentence:")
a = e = i = o = u = 0

for ch in s:
    if ch == 'a' or ch == 'A':
        a += 1
    elif ch == 'e' or ch == 'E':
        e += 1
    elif ch == 'i' or ch == 'I':
        i += 1
    elif ch == 'o' or ch == 'O':
        o += 1
    elif ch == 'u' or ch == 'U':
        u += 1

print("A =", a)
print("E =", e)
print("I =", i)
print("O =", o)
print("U =", u)
