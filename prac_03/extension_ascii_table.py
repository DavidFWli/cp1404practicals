for i in range(33, 127 + 1):
    print(i, chr(i))

while True:
    x = input("Enter a character:")
    if len(x) > 1:
        continue

    print("The ASCII code for %s is %d" % (x, ord(x)))

    x = input("Enter a number between 33 and 127:")
    try:
        a = int(x)
        if a < 33 or a > 127:
            continue
        print("The character for %d is %c" % (a, chr(a)))
    except:
        pass