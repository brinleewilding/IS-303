has_error = True

#while has_error:
    #try:
    #    number = int(input("Enter a number: "))
    #    print(number)
        
    #except ValueError:
    #    print("Invalid number. Please try again.")
    #    continue
    #except KeyboardInterrupt:
    #    print("You stopped the program")
    #except:
    #    print("You got some rando error")
   #     break

        #question on the exam dealing with continue and break

#from BankFunction import withdraw
 
def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient funds")

    return balance - amount    

balance = 100

try:
    amount = int(input("Please Enter the amount you want to withdraw: "))
    balance = withdraw(amount, balance)
except:
    print("Invalid amount")
    