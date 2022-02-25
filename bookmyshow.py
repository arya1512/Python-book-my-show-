movies = ('M1', 'M2', 'M3')
rec1 = []
pre1 = []
clas1 = []

rec2 = []
pre2 = []
clas2 = []

rec3 = []
pre3 = []
clas3 = []

global sums
#sums=0
for j in range(1, 13):
    t = "R" + " " + str(j)
    rec1.append(t)
for i in range(65,68):
    for j in range(1,13):
        r=chr(i)
        t=str(r)+" "+str(j)
        pre1.append(t)
for i in range(68, 72):
    for j in range(1, 13):
        r = chr(i)
        t = str(r) + " " + str(j)
        clas1.append(t)

for j in range(1, 13):
    t = "R" + " " + str(j)
    rec2.append(t)
for i in range(65,68):
    for j in range(1,13):
        r=chr(i)
        t=str(r)+" "+str(j)
        pre2.append(t)
for i in range(68, 72):
    for j in range(1, 13):
        r = chr(i)
        t = str(r) + " " + str(j)
        clas2.append(t)

for j in range(1, 13):
    t = "R" + " " + str(j)
    rec3.append(t)
for i in range(65,68):
    for j in range(1,13):
        r=chr(i)
        t=str(r)+" "+str(j)
        pre3.append(t)
for i in range(68, 72):
    for j in range(1, 13):
        r = chr(i)
        t = str(r) + " " + str(j)
        clas3.append(t)

def show_theatre_pvr():

    print("\n")
    print("-----RECLINERS- Rs 199-----")

    for i in range(12):
        print(rec1[i], end="  ")
    print("\n")

    print("------PREMIUM- Rs 85--------")
    for i in range(12):
        print(pre1[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(pre1[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(pre1[i], end="  ")
    print("\n")
    print("\n")
    print("------CLASSIC- Rs 85--------")
    for i in range(12):
        print(clas1[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(clas1[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(clas1[i], end="  ")
    print("\n")
    for i in range(36, 48):
        print(clas1[i], end="  ")
    print("\n")
    print("|||---------SCREEN THIS SIDE-------------|||")
    global sum
    sum = 0
    n = int(input("Kindly enter the number of people"))
    if (n > 10):
        print("Cannot select more than 10 seats at a time")
        show_theatre_pvr()
    seats = []
    for i in range(n):
        seat = input("Enter seat number")
        seats.append(seat)
    for s in seats:
        x = s.split()

        if x[0] == "R":
            sum = sum + 199
            for i in range(12):
                if rec1[i] == s:
                    rec1[i] = "XX"
        if x[0] == 'A' or 'B' or 'C':
            sum = sum + 85
            for i in range(36):
                if pre1[i] == s:
                    pre1[i] = "XX"
        if(x[0]=='D' or 'E' or 'F' or 'G'):
            sum = sum + 85
            for i in range(48):
                if clas1[i] == s:
                    clas1[i] = "XX"
    snacks()


def show_theatre_inox():
    print("\n")
    print("-----RECLINERS- Rs 199-----")

    for i in range(12):
        print(rec2[i], end="  ")
    print("\n")

    print("------PREMIUM- Rs 85--------")
    for i in range(12):
        print(pre2[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(pre2[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(pre2[i], end="  ")
    print("\n")
    print("\n")
    print("------CLASSIC- Rs 85--------")
    for i in range(12):
        print(clas2[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(clas2[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(clas2[i], end="  ")
    print("\n")
    for i in range(36, 48):
        print(clas2[i], end="  ")
    print("\n")
    print("|||---------SCREEN THIS SIDE-------------|||")
    global sum
    sum = 0
    n = int(input("Kindly enter the number of people"))
    if (n > 10):
        print("Cannot select more than 10 seats at a time")
        show_theatre_inox()
    seats = []
    for i in range(n):
        seat = input("Enter seat number")
        seats.append(seat)
    for s in seats:
        x = s.split()

        if x[0] == "R":
            sum = sum + 199
            for i in range(12):
                if rec2[i] == s:
                    rec2[i] = "XX"
        if x[0] == 'A' or 'B' or 'C':
            sum = sum + 85
            for i in range(36):
                if pre2[i] == s:
                    pre2[i] = "XX"
        if (x[0] == 'D' or 'E' or 'F' or 'G'):
            sum = sum + 85
            for i in range(48):
                if clas2[i] == s:
                    clas2[i] = "XX"
    snacks()


def show_theatre_PAR():
    print("\n")
    print("-----RECLINERS- Rs 199-----")

    for i in range(12):
        print(rec3[i], end="  ")
    print("\n")

    print("------PREMIUM- Rs 85--------")
    for i in range(12):
        print(pre3[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(pre3[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(pre3[i], end="  ")
    print("\n")
    print("\n")
    print("------CLASSIC- Rs 85--------")
    for i in range(12):
        print(clas3[i], end="  ")
    print("\n")
    for i in range(12, 24):
        print(clas3[i], end="  ")
    print("\n")
    for i in range(24, 36):
        print(clas3[i], end="  ")
    print("\n")
    for i in range(36, 48):
        print(clas3[i], end="  ")
    print("\n")
    print("|||---------SCREEN THIS SIDE-------------|||")
    global sum
    sum = 0
    n = int(input("Kindly enter the number of people"))
    if (n > 10):
        print("Cannot select more than 10 seats at a time")
        show_theatre_PAR()
    seats = []
    for i in range(n):
        seat = input("Enter seat number")
        seats.append(seat)
    for s in seats:
        x = s.split()

        if x[0] == "R":
            sum = sum + 199
            for i in range(12):
                if rec3[i] == s:
                    rec3[i] = "XX"
        if x[0] == 'A' or 'B' or 'C':
            sum = sum + 85
            for i in range(36):
                if pre3[i] == s:
                    pre3[i] = "XX"
        if (x[0] == 'D' or 'E' or 'F' or 'G'):
            sum = sum + 85
            for i in range(48):
                if clas3[i] == s:
                    clas3[i] = "XX"
    snacks()


def snacks():
    global sums
    sums = 0
    snackss = input("Do you wish to have snacks to enjoy your movie?? Type YES to get our super delicious snacks")
    if snackss == 'YES':
        snack = ['1- popcorn for 50rs', '2- chips for 20rs ', '3- sandwich for 60rs']
        print(snack)
        ss = int(input("Press number of any 1 snack"))
        if ss == 1:
            q = int(input("Enter quantity"))
            sums = sums + 50 * q
        elif ss == 2:
            q = int(input("Enter quantity"))
            sums = sums + 20 * q
        elif ss == 3:
            q = int(input("Enter quantity"))
            sums = sums + 60 * q
        more = input("do you wish to have more snacks?")
        if more == 'YES':
            snacks()

while (1):
    print("Welcome to Showbooking")
    search = input("Search here to find your favourite movies")
    if search not in movies:
        print("This movie is currently not available")
    elif search == "M1":
        print("M1 is available in theatre PVR")
        show_theatre_pvr()
    elif search == "M2":
        print("M2 is available in theatre INOX")
        show_theatre_inox()
    elif search == "M3":
        print("M3 is available in theatre PARVATI MULTIPLEX")
        show_theatre_PAR()
    money = sums + sum
    print("Your total is {}".format(money))



