import random
import datetime

#Global List Declaration
name=[]
phno=[]
reg=[]
checkin=[]
checkout=[]
room=[]
price=[]
rc=[]
p=[]
roomno=[]
custid=[]
day=[]

#Global Variable Declaration

i=0

#Home Function
def Home():
    print("\t\t\t\t\t\t Welcome to JKKNIU CENTRAL ROOM\n")
    print("\t\t\t 1 Conference Room's Info\n")
    print("\t\t\t 2 Booking\n")
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Room ratings\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit\n")

    ch= int(input("Enter your choice:"))

    if ch==1:
        print(" ")
        Rooms_Info()

    elif ch==2:
        print(" ")
        Booking()

    elif ch==3:
        print(" ")
        Payment()

    elif ch==4:
        print(" ")
        ratings()

    elif ch==5:
        print(" ")
        Record()

    else:
        exit()

#Booking Function
def Booking():
    #used global keyword to use global variable 'i'

    global i
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n=str(input("Name:"))
        p1=str(input("Phone No:"))
        a=str(input("Registration No:"))

        #checks if any field is not empty
        if n!="" and p1!="" and a!="":
            name.append(n)
            reg.append(a)
            break

        else:
            print("\tName, Phone No, and Registration No cannot be blank\n")

    cii=str(input("Booking Date:"))
    checkin.append(cii)
    coo=str(input("Booking Time:"))
    checkout.append(coo)
    print("------SELECT ROOM TYPE------")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print("\t\tPress 0 for Room Prices")


    ch=int(input("Enter your choice:"))

    #if-conditions to display allotted room type and it's price
    if ch==0:
        print(" 1. Standard Non-AC- Tk. 3500 for 1 day")
        print(" 2. Standard AC- Tk. 4000 for 1 day")
        ch=int(input("-> Choose room type:"))

    if ch==1:
        room.append('Standard Non-AC')
        print("Room Type- Standard Non-AC")
        price.append(3500)
        print("Price- 3500")

    elif ch==2:
        room.append('Standard AC')
        print("Room Type- Standard AC")
        price.append(4000)
        print("Price- 4000")

    else:
        print("Wrong Choice!")

    #randomly generating customer no
    cid= random.randrange(40)+10

    #checks if allotted room no. and customer id already not allotted
    while cid in custid:
        cid= random.randrange(60)+10

    rc.append(0)
    p.append(0)

    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 ==phno[n]:
                if p1 ==1:
                    phno.append(p1)

    elif p1 in phno:
        for n in range(0, i):
            if p1 ==phno[n]:
                if p[n] ==0:
                    print("\tPhone no. already exists and payment yet not done!")
                    name.pop(i)
                    reg.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()

    print("")
    print("\t\t\t **Room Booked Successfully**\n")
    print("Customer Id -", cid)
    '''roomno.append(rn) '''
    custid.append(cid)
    i=i+1
    n= int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()


#Rooms Info
def Rooms_Info():
    print("               -----------CONFERENCE ROOM'S INFO-----------")
    print("")
    print("STANDARD NON-AC")
    print("-----------------------------------------------------------")
    print("Room amenities include: High Quality Stage, Projector, Telephone, Microphone, Speaker,")
    print("Double-Door Cupboard, 1 Coffee table with 3 sofa for guests, 60 chairs for audience,")
    print("an washroom with hot/cold water.\n")
    print("STANDARD AC")
    print("-----------------------------------------------------------")
    print("Room amenities include: High Quality Stage, Projector, Telephone, Microphone, Speaker, ")
    print("Double-Door Cupboard, 1 Coffee table with 3 sofa for guests, 60 chairs for audience,")
    print("an washroom with hot/cold water, Window/Split AC\n")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()


#Rating Function
def rating():
    ph=int(input("Customer Id:"))
    global i
    f=0
    r=0
    for n in range(0, i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("\n Ratings")
            print(" 1 Very satisfied")
            print(" 2 Somewhat satisfied")
            print(" 3 Neither satisfied nor unsatisfied")
            print(" 4 Somewhat unsatisfied")
            print(" 5 Very unsatisfied")
            print(" Press  0 to exit")
            ch=1
            while (ch!=0):
                ch=int(input("Enter your choice->"))

                #if-elif-conditions to assign item prices listed in menu card
                if ch==1:
                    print("Thanks for your ratings!")
                elif ch==2:
                    print("Thanks for your ratings!")
                elif ch==3:
                    print("Thanks for your ratings!")
                elif ch==4:
                    print("Thanks for your ratings!")
                elif ch==5:
                    print("Thanks for your ratings!")
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice!")

        else:
            pass
        if f==0:
            print("Invalid Customer Id")
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()

#Payment Function
def Payment():
    ph=str(input("Phone Number:"))
    global i
    f=0

    for n in range(0, i):
        if ph==phno[n]:
    # checks if payment is not already done
            if p[n]==0:
                f=1
                print("Payment")
                print("-------------------------------")
                print("Mode of Payment")

                print(" 1- Cash")
                x=int(input("Enter your choice->"))
                print("\n Amount: ", (price[n]))
                print("\n      Pay for JKKNIU")
                print("(y/n)")
                ch=str(input("->"))

                if ch=="y" or ch=="Y":
                    print("\n\n----------------------------")
                    print("         JKKNIU           ")
                    print("--------------------------------")
                    print("            Bill           ")
                    print("--------------------------------")
                    print("Name:", name[n],"\t\n Phone No:", phno[n], "\t\n Registration no:", reg[n], "\t")
                    print("\nBooking Date:", checkin[n], "\t\n Booking Time:", checkout[n], "\t")
                    print("\nRoom Type:", room[n], "\t\n Room Charges:", price[n], "\t")
                    print("--------------------------------")
                    print("\n Total Amount: ", (price[n]), "\t")
                    print("--------------------------------")
                    print("             Thank You!!")
                    print("             Visit Again!!!")
                    print("------------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)

                    #pops room no. and customer id from list and later assigns zero at same position
                    custid.pop(n)
                    custid.insert(n,0)
                else:
                    for j in range(n+1,i):
                        if ph==phno[j]:
                            if p[j]==0:
                                pass
                            else:
                                f=1
                                print("\n\tPayment has been made \n\n")

                if f==0:
                    print("Invalid Customer Id")
                n=int(input("0-BACK\n ->"))
                if n==0:
                    Home()
                else:
                    exit()

#Record Function
def Record():
    #checks if any record exists or not
    if phno != []:
        print("     *Booking Record*\n")
        print("|Name      |Phone No      |Registration No      |Booking Date      |Booking Time      |Room Type      |Price      |")
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )

        for n in range(0, i):
            print("|", name[n], "\t|", phno[n],"\t|", reg[n], "\t|", checkin[n],"\t|", checkout[n],"\t|", room[n], "\t|", price[n])
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )
    else:
        print("No Records Found")
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()

#Driver Code
Home()