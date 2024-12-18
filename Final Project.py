def act_1():
    print("\nThis is my activity 1\n")
print("Hello World")

def act2():
        print("\nThis is my activity 2\n")
name = input( "Please enter a name -----> " )
print ( "Hi!" + name )

def act3():
        print("\nThis is my activity \n")
name = input("Please input your name here ---> ")
fname = input("Please input your fname here ---> ")
mname = input("Please input your mname here ---> ")
birthdate = input("Please input your birth date here ---> ")
birthmonth = input("Please input your birthmonth here ---> ")
birthyear = input("Please input your birthyear here ---> ")
maritalstatus = input("Please input your maritalstatus here ---> ")
religion = input("Please input your religion here ---> ")
ethnicity = input("Please input your ethnicity here --->")
mobile = input("Please input your mobile here ---> ")
email = input("Please input your email here ---> ")
gender = input("Please input your gender here ---> ")
address = input("Please input your address here ---> ")
age = input(" Please input your age here ---> ")
print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")  

def act4():
        print("========================================\n")
num1 = eval(input("Number: "))
num2 = eval(input("Number: "))
op = input("Operators(+, -, /, x): ")

if op == "+":
        print("Output:", num1 + num2)
elif op == "-":
	    print("Output:", num1 - num2)
elif op == "/":
	    print("Output:", num1 / num2)
elif op == "x":
	    print("Output:", num1 * num2)
else:
	    print("Invalid operator! \n\n")
print("\n========================================")

def act5():
    print("FAHRENHEIT TO CELSIUS CONVERTER")

temp = eval(input("Enter temperature in fahrenheit : "))
celsius = (temp - 32) * 5 / 9
print("The convertion of ",temp, "degress Fahrenheit is",celsius, "degress celsius")

def act_6():
        print("\nThis is my activity 6\n")
x = 5
print(x)
x = x + 10
print(x)
x = x +15
print(x)
x += 10 
print(x)
x+=20
print(x)

def act7():
        print("\nThis is my activity 7\n")
gold = 0
name=input('Hi, enter your name:  ')
hasMine=input('Did you mine gold today?  ')
if hasMine.lower() == "yes":
        gold +=1
        print(f'Hi! {name}, Today you have a total of {gold} gold')
else:
        print(f'Hi! {name}, Today you have a total of {gold} gold')

def act8():
        print("\nThis is my activity 8\n")
password = input('Enter your password---> ')
if password.lower() == "password" :
    print('Access Granted!!!!')
    print('Enjoy using the system')
elif password.lower() =='secret':
        print('Access Granted!!!!')
        print('Enjoy using the system')
else:
        print('Access Denied!!!!!')
print('Thank you for using the system')

    
def act9():
    age = eval(input("Enter your age--->"))
if age >=1 and age<=7:
    print("toddler")
elif age >=8 and age <=13:
    print("pre-teen")
elif age >=14 and age <=16:
    print("teen")
elif age >=17 and age <=25:
    print("teenager")
elif age >=25 and age <=50:
    print("adult")
elif age >=60 and age <=100:
    print("senior")

def act10():
        isDLL = input("Are you a current student of dll? (yes/no)")
        if isDLL.lower == "yes":
         print("WELCOME TO THE DLL BSIT SCHOLARSHIP FORM")
isgg = input("Are you from Gulang-Gulang? (yes/no)")
if isgg.lower() == "yes":
    print("Please fillup the second form")
    islevel = input("What is your current level right now in DLL\nF-Freshmen\nS-Sophomore\nJ-Junior\nS2-Senior")

    if islevel.lower() == 'f':
        print("Hi Freshmen")
    elif islevel.lower() == 's':
        print("Hi Sophomore")
    elif islevel.lower() == 'j':
        print("Hi Junior")
    elif islevel.lower() == 'S2':
        print("Hi Senior")
    else:
        print("invalid")

    isneeded = input("Do you need this scholarship (yes/no)")
    if isneeded.lower() == "yes":
        print("Scholarship Granted")
    else:
        print("Thank u for stopping by")

#Act11
for line in range(10):
        print("Hellow")

#Act12
for cycle in range(10,0,-1):
        print(cycle)

#Act13
number = int(input("Enter any number: "))
factorial = 1
for fact in range(number, 0, -1):
        factorial *= fact 
        rounded = round(factorial, 2)
print(f"The factorial of {rounded}\n")

#Act14
for x in range(1,11, 5):
        print(x, end="3")
print("hello world", end=" - ")
print("BSIT 1C\n")

for x in range(1,11):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print()

#Act15
for x in range(0,11):
    print(x,end = " ")
    for y in range(0,x):
        print("*" ,end=" ")
    print()

#Act16
for x in range(1, 6):
        for y in range(1, x + 1):
            print("  ",end="")
        for z in range(6, y, -1):
            print("^ ",end="")
        for a in range(6, x, -1):
            print("* ",end="")
        for b in range(1, x + 1):
            print(" ",end="")
        print("\n")
        print()

#Act17
pur= int(input("Enter a number: "))
for x in range(1,11):
        for y in range(1, pur + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print()

#Act18
pur = int(input("Enter a number: "))
for a in range(1,5):
        for x in range(1,pur +1 ):
            for y in range(1, a + 1):
                print("*", end= " ")

            for z in range(5, a, -1):
                print(" ", end=" ")
        print()

#Act19
while True:
        name = input("Are You Okay? (yes/ no): ")
        if name.lower() == "yes":
            print("I'm happy for you!")
            break
        elif name.lower() == "no":
            print("I hope your okay\n")
            break
        else:
            print("Invalid input exiting")
            break

#Act20
go = True

while go == True:
    name = input("Please enter a name--->")

    if name.lower() == "stop":
        print("loop stopped")
        break
        go = False

    else:
        print("program would continue")
        continue

#Act21
count = 0
while go == True:
    name = input("Please enter a name---->")

    if name.lower == "stop":
        print("Loop has stopped")
        print(f"You have entered {count} number of names")
        break
        go = False
    else:
        count += 1
        continue

#Act22
print("\nThis is my activity 22\n")
def activity22():
        def activity1():
            print("Hello World")
        activity1()
        activity22()

#Act23
print("\nThis is my activity 23\n")
def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        return fact
print(f"the factorial of 13 is {factorial(13)}")

#Act24
print("This Is a combined progam, activity 23 and activity24\n")
fact = 2
for x in range(10 , 0, -1):
        fact *= x
print(f"\n\t\t\t\t\tTHE FACTORIAL OF 4 IS : ----> {fact} \n")

#Act25
print("This program is about List\n")
    #LIST
    #fruits1 = "apple"
    #fruits2 = "banana"
    #fruits3 = "orange"
    #fruits4 = "star apple"
    #fruits5 = "guyabano"
fruits = ["apples", "banana", "orange", "star apple", "guyabano"]
print(f"\n{fruits}")
print(f"\nMy favorite childhood fruit is {fruits[2]}")
fruits.append("langka")
print(f"\n{fruits}")

#Code_Challenge1
print("\t\t*\n\t*\t*\t*\n*\t*\t*\t*\t*\n\t*\t*\t*\n\t*\t*")

#Code_Challenge2
name = input("Please enter your name: ")
print("\n\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\b\b* * * \n\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n" + "\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b *" +" Hi " + name + " * \n\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n\t\t\t\t\t\t\t\t\b\b* * * \n\t\t\t\t\t\t\t\t*")

#Code_Challenge4
num1 = eval(input("Enter a number--->"))
num2 = eval(input("Enter another number--->"))
answer = num1 + num2
print("The sum of" ,num1, "and" ,num2, "is" ,sum)
diff = num1 - num2
print("The difference of" ,num1, "and" ,num2, "is" ,diff)
product = num1 * num2
print("The product of" ,num1, "and" ,num2, "is" ,product)
quotient = num1 / num2
print("The quotient of" ,num1, "and" ,num2, "is" ,quotient)
exponent = num1 ** num2
print("The exponent of" ,num1, "and" ,num2, "is" ,exponent)
remainder = num1 % num2
print("The remainder of" ,num1, "and" ,num2, "is" ,remainder)
fd = num1 // num2
print("The floordivision of" ,num1, "and" ,num2, "is" ,fd)

#Code_Challenge5
name = input("Enter your Name: ")
deposit = eval(input("Enter amount to deposit: "))

n1 = deposit % 1000
ans2 = n1 // 500
n2 = n1 % 500
ans3 = n2 // 200
n3 = n2 % 200
ans4 = n3 // 100
n4 = n3 % 100
ans5 = n4 // 50
n5 = n4 % 50
ans6 = n5 // 20
n6 = n5 % 20
ans7 = n6 // 10
n7 = n6 % 10
ans8 = n7 // 5
n8 = n7 % 5
ans9 = n8 // 1
n9 = n8 % 1

print("Hello" ,name, "the breakdown of your deposit is:")
print(n1, "- 1000")
print(ans2, "- 500")
print(ans3, "- 200")
print(ans4, "- 100")
print(ans5, "- 50")
print(ans6, "- 20")
print(ans7, "- 10")
print(ans8, "- 5")
print(ans9, "- 1")

#Code_Challenge6
prelim = eval(input("Enter your grade in prelim: "))
midterm = eval(input("Enter your grade in midterm: "))
finals = eval(input("Enter your grade in finals: "))
quizzes = eval(input("Enter your grade in quizzes: "))
projects = eval(input("Enter your grade in projects: "))

fg = (prelim * .15) + (midterm * .15) + (finals * .15) + (quizzes * .20) + (projects * .20)

if fg <= 100:
    print("Congratulations your passed:")
elif fg:
    print("invalid")
elif fg >= 75:
    print("Sorry your failed")

#Code_Challenge7
user = input("Please Enter your name: ")
age = eval(input("Please Enter your age: "))
money = 500
while True:
        print("================================================================================")
        print("             ITEMS: (1).milk (2).Chicken (3).pizza (4).burger")
        print("================================================================================")
        print(f"Your money is: {money}")
        print("\nChoices (1-4)")
        print("\nType [exit] to exit program")
        choice = input("Please choose which item you would like to buy: ")

        if choice == "1":
            num1 = input("Milk costs 50. Would you like to buy it? (yes/no): ")
            if num1.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 50 
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num1.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "2":
            num2 = input("Chicken costs 100. Would you like to buy it? (yes/no): ")
            if num2.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 100
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num2.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "3":
            num3 = input("Pizza costs 200. Would you like to buy it? (yes/no): ")
            if num3.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 200
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num3.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "4":
            num4 = input("Burger costs 30. Would you like to buy it? (yes/no): ")
            if num4.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 30
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num4.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice.lower() == "exit":
            print(f"Goodbye, {user}! Your remaining balance is {money}.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

#Code_Challenge8
odd_count = 0
even_count = 0
total_sum = 0

for i in range(1, 11):
        user_input = int(input(f"Enter number {i}: "))
        total_sum += user_input
        
        if user_input % 2 == 0:
            even_count += 2
        else:
            odd_count += 1
        print(f"\nThe total sum of the numbers you entered is: {total_sum}")
        print(f"Even numbers tally: {even_count}")
        print(f"Odd numbers tally: {odd_count}")

#Code_Challenge9
size = 7
for i in range(size,0,-1):
        print(" " * (size - i) + "*" * i)

#Code_Challenge10
for r in range(1,6):
        for i in range(6,r, -1):
            print(" ",end="")
        for j in range(0, r):
            print("*", end="")
        for k in range(r,6, -1):
            print("*", end="")
        for l in range(0,r):
            print("*", end="")
        print()
for t in range(1,6):
        for x in range(1,t + 1):
            print(" ", end="")
        for y in range(6,t, -1):
            print("*", end="")
        for y in range(6,t, -1):
            print("*", end="")    
        print()

#Code_Challenge11
for r in range(1, 7):
        for i in range(7, r, -1):
            print(" ", end="")
        for j in range(1, r):
            print("*", end="")
        for k in range(0, r):
            print("*", end="")
        print()
    
for t in range(0, 7):
        for x in range(1, t + 1):
            print(" ", end="")
        for y in range(t, 6):
            print("*", end="")
        for z in range(t, 7):
            print("*", end="")
        print()

#Code_Challenge12
for i in range(0, 9):
        for j in range(9, i, -1):
            print(" ", end="")
        for k in range(i + 1):
            print("*", end=" ")
        print()

for a in range(6):
        print("       * * * *")

#Code_Challenge13
for r in range(1, 8):
        for i in range(8, r, -1):
            print(" ", end="")
        for j in range(r - 1, 1, -1):
            print(j, end="")
        for k in range(1, r):
            print(k, end="")
        print()

for t in range(6, 1, -1):
        for x in range(8, t, -1):
            print(" ", end="")
        for y in range(t - 1, 1, -1):
            print(y, end="")
        for z in range(1, t):
            print(z, end="")
        print()

#Code_Challenge14
tuloy = True
a = 0
while tuloy == True:
    number = eval(input("Enter a number--->  "))
    if number == 0:
        print("Program Terminated")
        print(f"The total of the number you enter is {a}")
        break

    else:
        a += number
        continue

#Code_Challenge15
import os

isContinue = True
no = 0
while isContinue == True:
    ask = input("Would you like to add another triangle (yes / no )--> ")

    if ask.lower() == "no":
        print("PROGRAM TERMINATED")
        break
        isContinue = False
    elif ask.lower() == "yes":
        os.system('cls')
        no += 1
        for x in range (1, 6):
            for r in range (1 , no + 1):
                for y in range (1 , x + 1):
                    print("*", end=" ")
                for z in range (6, x, -1):
                    print(" ",end=" ")
            print()
    else:
        print("INVALID ANSWER it's only (yes/no)")
        continue

#Code_Challenge16
print("\nThis is my Code Challenge 16\n")
def breakdown_denomination(amount):
        print("Denomination Breakdown:")
        denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
        for denom in denominations:
            if amount >= denom:
                count = amount // denom
                print("PHP", denom, ":", count)
                amount = amount % denom
def create_account():
        account_name = input("Enter your name: ")
        initial_deposit = eval(input("Enter initial deposit: "))
        if initial_deposit >= 0:
            print("Account created for", account_name, "with balance PHP", initial_deposit)
            return account_name, initial_deposit
        else:
            print("Initial deposit must be 0 or more.")
            return None, 0
def deposit(account_name, account_balance):
        if account_name == None:  
            print("No account found. Please create an account first.")
        else:
            amount = eval(input("Enter amount to deposit: "))
            if amount > 0:
                account_balance += amount
                print("Deposited PHP", amount, ". Current balance: PHP", account_balance)
                breakdown_denomination(amount)
            else:
                print("Deposit amount must be greater than 0.")
        return account_balance
def withdraw(account_name, account_balance):
        if account_name == None:
            print("No account found. Please create an account first.")
        else:
            amount = eval(input("Enter amount to withdraw: "))
            if amount > account_balance:
                print("Insufficient balance!")
            elif amount > 0:
                account_balance -= amount
                print("Withdrew PHP", amount, ". Current balance: PHP", account_balance)
            else:
                print("Withdrawal amount must be greater than 0.")
        return account_balance
def check_balance(account_name, account_balance):
        if account_name == None:
            print("No account found. Please create an account first.")
        else:
            print("Your current balance is PHP", account_balance)
def main():
        account_name = None
        account_balance = 0
        while True:
            print("\n=== Welcome to Kabayan-Bank ===")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")
            if choice == "1":
                account_name, account_balance = create_account()
            elif choice == "2":
                account_balance = deposit(account_name, account_balance)
            elif choice == "3":
                account_balance = withdraw(account_name, account_balance)
            elif choice == "4":
                check_balance(account_name, account_balance)
            elif choice == "5":
                print("Thank you for using the banking system!")
            else:
                print("Invalid option. Please try again.")
main()

# Menu & Body

def body():
    tuloy = True
while tuloy == True:
    def body():
        print(f"\nWelcome to code compilation of Zyra Marie A. Pureza")
        print(f"Bachelor Of Science In Infomation Technology - 1C")
        print(f"\nPlease Select an Option:   ")
        print(f"\n1. Open Activity Folder")  
        print(f"2. Open Code Challenge Folder")
        print(f"3. Exit Program")
        menu = input(f"\nChoose what action you want to do:  ")
        while body:
            if menu == "1":
                os.system("cls")
                act_folder()
            elif menu == "2":
                cc_folder()
                os.system("cls")
            elif menu == "3":
                os.system("cls")
                print(f"\nProgram terminated, Thank you for checking my Program.\n")
            else:
                print("Invalid Choice, Please try again.")         

        if menu == "1":
            os.system("cls")
            def act_folder():
                print(f"\nWelcome to code compilation of Zyra Marie A. Pureza")
                print(f"Bachelor Of Science In Infomation Technology - 1C")
            act_folder()
        elif menu == "2":
            cc_folder()
            os.system("cls")
        elif menu == "3":
            os.system("cls")
            print(f"\nProgram terminated, Thank you for checking my Program.\n")
        else:
            print("Invalid Choice, Please try again.")         
body()

def act_folder():
    print(f"\nWelcome to code compilation of Zyra Marie A. Pureza")
    print(f"Bachelor Of Science In Infomation Technology - 1C")
def cc_folder():
    print(f"\nWelcome to code compilation of Zyra Marie A. Puureza")
    print(f"Bachelor Of Science In Infomation Technology - 1C")