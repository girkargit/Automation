c = 0
for i in range(1, 100):
    if (i % 2 == 0 and i % 5 == 0):
        print(i)
        c = c + 1
        if c == 3:
            break
print("***",c)