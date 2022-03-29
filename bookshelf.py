shelf = []
w1 = 1
while w1 < 2:
    a1 = str(input("Change booklist or Search books ? (c, s)    "))
    if a1 == "c":
        w2 = 1
        while w2 < 2:
            q = str(input("Do you want add or remove books ? (y, n)  "))
            if q == "y":
                a2 = str(input("Add or Remove book ? (a, r)     "))
                if a2 == "a":
                    b = str(input("Input name of book - "))
                    shelf.append(b)
                elif a2 == "r":
                    b == str(input("Input name of book - "))
                    shelf.remove(b)
            elif q == "n":
                w2 = w2 + 1

    elif a1 == "s":
        a2 = str(input("Input name of book - "))
        if a2 in shelf:
            print(a2)
        else:
            print("Not found")
    print(shelf)
