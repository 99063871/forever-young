tafel = int(input("Welke tafel wilt u?"))

tafelstr = str(tafel)


for x in range(1,11):
    xstr = str(x)
    a = (x*tafel)
    b = str(a)
    print(xstr + " * " + tafelstr + " = "+ b)
    