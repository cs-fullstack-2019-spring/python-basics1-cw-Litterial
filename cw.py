def main():

    def quest1():
    # Create a function with two variables. One should equal “My name is: “ and the other should equal your actual name.
    # Print the two variables in one print message.
        def printmyname():
            greet= "My name is: "
            name = input("Please enter your name. ")  #asks for name
            print(greet+name)
        printmyname()      #calls function
    def quest2():
    #Create a function to ask the user to enter the extra credit they earned. If they entered less than 5 print
    # “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.
        def myextracredit():
            extra= int(input("Please enter the amount of extra credit you've earned. ")) #ask for amount
            if (extra<5):                                      #if statements to see if extra is less than 5, greather
                                                                # than 20, or other
                print("That's not enough extra credit.")
            elif(extra>20):
                print("That's too much extra credit.")
            else:
                print(extra)
        myextracredit()               #calls function

    def quest3():
    #Create a function to ask a user to enter a password. Enter a password. Ask user to reenter password.
    # Check to see if they are correct.
        def passwordcheck():
            first= input("Please enter your password. ")
            second= input("Please re-enter your password. ")
            if(first==second):    #check if passwords match
                print("Correct")
            else:
                print("The passwords don't match.")
        passwordcheck()    #calls function

    def quest4():
    #Create a function to ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print
    # BUST!, if it’s less than 21 print “The total is [THE TOTAL]”
        def blackjack():
            firstcard= int(input("Enter your card value. " ))
            secondcard = int(input("Enter your second card value. " ))
            sum= firstcard+secondcard   #adds both card values

            if(sum>21):        #checks if total is over 21, 21, or less than 21
                print("Bust")
            elif(sum ==21):
                print("Blackjack")
            else:
                print("The total is: " ,sum)
        blackjack()   #calls function

    #quest1()
    #quest2()
    #quest3()
    quest4()
if __name__ == '__main__':
    main()