pin = 1234
option = 0
retry = 0
bal = 4500
KeepLooping = "Y"
while (retry < 5 and KeepLooping == "Y"):
    val = input("Enter your PIN:")
    val = int(val)
    if (val == pin):
        while (KeepLooping == "Y"):
            option = int(input("Press 1 for Balance; 2 for Withdrawal; 3 for Deposit; 4 to exit: "))
            if (option > 4):
                print("Invalid Option Entered. Please Try Again")
            elif (option == 1):
                print("Current Balance: ",bal)
            elif (option == 2):
                withdrawal = int(input("Enter Amount to Withdrawal: "))
                bal -= withdrawal
                print("New Balance: ",bal)
            elif (option == 3):
                deposit = int(input("Enter Amount to Deposit: "))
                bal += deposit
                print("New Balance: ",bal)
            elif (option == 4):
                print("Goodbye!")
                KeepLooping = "N"
                break
    else:
        print("you entered an invalid PIN:")
        retry += 1
        if (retry == 4):
            print("You have exceeded the number of retries!")
            break