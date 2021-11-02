#Print de hele uren van de dag. Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe

for x in range(1,25):
    xstr = str(x)
    if x < 12:
        print(xstr + "AM")
    else:
        print(xstr + "PM")