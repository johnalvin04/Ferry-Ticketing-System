temp = [[" ", 1, 2, 3, 4, 5], ["A", 0, 0, 0, 0, 0], ["B", 0, 0, 0, 0, 0]]
temp3= [[" ", 1, 2, 3, 4, 5], ["C", 0, 0, 0, 0, 0], ["D", 0, 0, 0, 0, 0], ["E", 0, 0, 0, 0, 0], ["F", 0, 0, 0, 0, 0],
       ["G", 0, 0, 0, 0, 0], ["H", 0, 0, 0, 0, 0], ["I", 0, 0, 0, 0, 0], ["J", 0, 0, 0, 0, 0]]

def MainMenu():
    print("**************************************************************************")
    print("                         FERRY TICKETING SYSTEM                           ")
    print("**************************************************************************")
    print("P = Purchasing menu")
    print("V = View Seating Arrangement")
    print("Q = Quit")
    print(" ")
    opt=str(input("Select your option: "))
    if(opt == "P"):
        SubMenu()
    elif(opt == "V"):
        SeatMenu()
    elif(opt == "Q"):
        quit()
    else:
        print("Option invalid, please try again!")
        MainMenu()


def SubMenu():
    print("**************************************************************************")
    print("                             PURCHASE MENU                                ")
    print("**************************************************************************")
    print("B = Business Class")
    print("E = Economy Class")
    print("M = Main Menu")
    print(" ")
    opt=str(input("Select your option: "))
    if(opt=="B"):
        BusinessClassMenu()
    elif(opt=="E"):
        EconomyClassMenu()
    elif(opt=="M"):
        MainMenu()
    else:
        print("Option invalid, please try again!")
        SubMenu()

def BusinessClassMenu():
    print("**************************************************************************")
    print("                       BUSINESS CLASS SEAT SELECTION                      ")
    print("**************************************************************************")
    grid()
    print()
    print("Please select a seat from A1 to B5")
    print()
    b_opt=[str(input("Select your seat : "))]
    row = ord(b_opt[0][0]) - 64
    column = int(b_opt[0][1])
    if(temp[row][column]==0):
          temp[row][column] = 1
    else:
        print("Option invalid, please try again!")
        BusinessClassMenu()
    grid()
    print()
    print("PLEASE KEY 'Y' TO CONFIRM SELECTION AND PROCEED TO TICKET MENU")
    print("PLEASE KEY 'N' TO CHOOSE ANOTHER SEAT")
    print(" ")
    ans=str(input("Confirm selection? "))
    if(ans=="Y"):
        SeatMenu()
    elif(ans=="N"):
        BusinessClassMenu()
    else:
        print("Option invalid, please try again!")
        BusinessClassMenu()

def EconomyClassMenu():
    print("**************************************************************************")
    print("                       ECONOMY CLASS SEAT SELECTION                       ")
    print("**************************************************************************")
    gridtwo()
    print()
    print("Please select a seat number from C1 to J5")
    print()
    e_opt=[str(input("Select your seat : "))]
    row = ord(e_opt[0][0]) - 66
    column = int(e_opt[0][1])
    if(temp3[row][column]==0):
          temp3[row][column] = 1
    else:
        print("Option invalid, please try again!")
        EconomyClassMenu()
    gridtwo()
    print("PLEASE KEY 'Y' TO CONFIRM SELECTION AND PROCEED TO TICKET MENU")
    print("PLEASE KEY 'N' TO CHOOSE ANOTHER SEAT")
    print(" ")
    ans=str(input("Confirm selection? "))
    if(ans=="Y"):
        SeatMenu()
    elif(ans=="N"):
        EconomyClassMenu()
    else:
        print("Option invalid, please try again!")
        EconomyClassMenu()
            

def SeatMenu():
    print("************************************************************************")
    print("                        SEATING ARRANGEMENT MENU                        ")
    print("************************************************************************")
    print()
    print("F = Select Ferry ID")
    print("T = Select Trip Time")
    print("M = Main Menu")
    print()
    opt=str(input("Select your option: "))
    print()
    if(opt=="F"):
        FerryIDMenu()
    elif(opt=="T"):
        TripTimeMenu()
    elif(opt=="M"):
        MainMenu()
    else:
        print("Option invalid, please try again!")
        SeatMenu()

def FerryIDMenu():
    print("************************************************************************")
    print("                            FERRY ID MENU                               ")
    print("************************************************************************")
    print()
    print("Ferry ID\tTrip Time")
    print("1)001\t\t10.00am\n2)002\t\t11.00am\n3)003\t\t12.00pm\n4)004\t\t1.00pm\n5)005\t\t2.00pm\n6)006\t\t3.00pm\n7)007\t\t4.00pm\n8)008\t\t5.00pm")
    fid=int(input("Choose your Ferry ID:"))
    if(fid==1):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 10.00am")
        bookfile.close()
        DetailsMenu()
    elif(fid==2):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 11.00am")
        bookfile.close()
        DetailsMenu()
    elif(fid==3):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 12.00pm")
        bookfile.close()
        DetailsMenu()
    elif(fid==4):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 1.00pm")
        bookfile.close()
        DetailsMenu()
    elif(fid==5):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 2.00pm")
        bookfile.close()
        DetailsMenu()
    elif(fid==3):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 3.00pm")
        bookfile.close()
        DetailsMenu()
    elif(fid==3):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 4.00pm")
        bookfile.close()
        DetailsMenu()
    elif(fid==3):
        bookfile = open("bookfile.txt","w")
        bookfile.write("Time depart: 5.00pm")
        bookfile.close()
        DetailsMenu()
    else:
        print("Option invalid, please try again!")
        FerryIDMenu()

def DetailsMenu():
    print("**************************************************************************")
    print("                          PERSONAL DETAILS                                ")
    print("**************************************************************************")
    print()
    print("Key in your details so that your boarding ticket can be issued")
    name = str(input("Enter your Name: "))
    ferryID = str(input("Enter your Ferry ID: "))
    triptime = str(input("Enter your Trip Time: "))
    seatnum = str(input("Enter your Seat Position: "))
    seattype = str(input("Enter your Seat Type (Business / Economy): "))
    source = str(input("Enter your current place: "))
    destination = str(input("Enter your destination: "))
    userdetails = open("userfile.txt","a")
    userdetails.write(name)
    userdetails.write("\n")
    userdetails.write(ferryID)
    userdetails.write("\n")
    userdetails.write(triptime)
    userdetails.write("\n")
    userdetails.write(seatnum)
    userdetails.write("\n")
    userdetails.write(seattype)
    userdetails.write("\n")
    userdetails.write(source)
    userdetails.write("\n")
    userdetails.write(destination)
    userdetails.close()
    print("Kindly print out the boarding pass as it will be needed at the gate.")
    print()
    print("When done printing, press 'D' to go back to the Main Menu. ")
    t_opt=str(input("Press P to print boarding ticket: "))
    if(t_opt=="P"):
        print()
        userdetails = open("userfile.txt","r")
        print(userdetails.read())
        userdetails.close()
    else:
        print("Option invalid, please try again")
    print()
    doneprint=str(input("Press D to exit to main menu: "))
    if(doneprint=="D"):
        MainMenu()

def grid():
    for i in range (len(temp)):
        temp2 = " | ".join(map(str, temp[i]))
        print(temp2)

def gridtwo():
    for i in range (len(temp3)):
        temp4 = " | ".join(map(str, temp3[i]))
        print(temp4)

    
    
        
    
    
MainMenu()
