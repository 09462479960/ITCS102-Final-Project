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
        print("\This is my Activity 9\n")
age = eval(input("Enter your age--->"))
if age >=5 and age <=7:
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
        print("\This is my activity 10\n")
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

def act11():
    print("\nThis is my activity 11\n")
for line in range(10):
        print("Hellow")

def act12():
    print("\nThis is my activity 12\n")
for cycle in range(10,0,-1):
        print(cycle)

def act13():
    print("\nThis is my activity 13\n")
number = int(input("Enter any number: "))
factorial = 1
for fact in range(number, 0, -1):
        factorial *= fact 
        rounded = round(factorial, 2)
        print(f"The factorial of {rounded}\n")

def act14():
    print("\nThis is my activity 14\n")
for x in range(1,11, 5):
        print(x, end="3")
        print("hello world", end=" - ")
        print("BSIT 1C\n")

for x in range(1,11):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print()

def act15():
    print("\nThis is my activity 15\n")
for x in range ( 0, 11,):
            print(x,end =" ")
            for y in range (0, x):
                print("*",end = " ")
            print("")

def act16():
    print("\nThis is my activity 16\n")
for x in range (1,11,):
            for y in range (1, x + 1):
                print(" ",end=" ")
            for z in range(11, x, -1):
                print(" * ",end=" ")
            print()

def act17():
    print("\nThis is my activity 17\n")
col = eval(input("Enter number of columns---> "))
for x in range (1, 11):
            for y in range (1, col + 1):
                print(f"{x} x {y} = {x*y}" ,end="\t")
            print()


def act18():
    print("\nThis is my activity 18\n")
tri = eval(input("Enter a number of triangle---> "))
for x in range (1, 6):
            for r in range (1 , tri + 1):
                for y in range (1 , x + 1):
                    print("*", end=" ")
                for z in range (6, x, -1):
                    print(" ",end=" ")
            print()

def act19():
    print("\nThis is my activity 19\n")
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
def act20():
    print("\nThis is my activity 20\n")
go = True

while go == True:
    name = input("Please enter a name--->")

    if name.lower() == "stop":
        print("loop stopped")
    break
    go = False

else:
    print("program would continue")

def act21():
    print("\nThis is my activity 21\n")
go = True
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

def act22():
    print("\nThis is my activity 22\n")
def activity22():
            def activity1():
                print("Hello World")
            activity1()
activity22()

def act23():
    print("\nThis is my activity 23\n")
def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        return fact
print(f"the factorial of 13 is {factorial(13)}")

def act24():
    print("\nThis is my activity 24\n")
def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        return fact
print(f"the factorial of 13 is {factorial(13)}")
print(f"the factorial of 7 is {factorial(7)} ")

def act25():
    print("\nThis is my activity 25\n")
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

#Code_Challenges

def cc1():
    print("\nThis is my Code Challenge1\n")
print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")

def cc2():
    name = input("\nType your name here --->")
print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*","  Hi",name,"\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")

def cc4():
    print("\nThis is my Code Challenge 4\n")
number1 = eval(input("\nEnter a number ---> "))
number2 = eval(input("\nEnter another number ---> "))
answer1 = number1 + number2 
answer2 = number1 - number2 
answer3 = number1 * number2 
answer4 = number1 / number2 
answer5 = number1 % number2 
answer6 = number1 ** number2 
answer7 = number1 // number2 
print("\nThe sum of " , number1 , " and " , number2 , " is " , answer1)
print("The difference of " , number1 , " and " , number2 , " is " , answer2)
print("The product of " , number1 , " and " , number2 , " is " , answer3)
print("The quotient of " , number1 , " and " , number2 , " is " , answer4)
print("The remainder of " , number1 , " and " , number2 , " is " , answer5)
print("The exponent of " , number1 , " and " , number2 , " is " , answer6)
print("The floor division of " , number1 , " and " , number2 , " is " , answer7)

def cc5():
    name = input("Enter your Name: ")
deposit = eval(input("Enter amount to deposit: "))

ans1 = deposit // 1000
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

def cc6():
    print("\nThis is my Code Challenge 6\n")
prelim = eval(input("\nEnter your grades in Prelims ---> "))
midterm = eval(input("\nEnter your grades in Midterms ---> "))
finals = eval(input("\nEnter your grades in Finals ---> "))
quizzes = eval(input("\nEnter your grades in Quizzes ---> ")) 
projects = eval(input("\nEnter your grades in Projects ---> "))

if (prelim >= 65 and midterm <=100) and (midterm >= 65 and midterm <=100) and (finals >= 65 and finals <=100) and (quizzes >= 65 and quizzes <=100) and (projects >= 65 and projects <=100):
        brtt = (prelim * 0.15) + (midterm * 0.15) + (finals * 0.15) + (quizzes * 0.25) + (projects * 0.15) 
        if brtt >= 75:
            print("\nCongratulations for passing the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
        else:
            print("\nYou failed for the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
else:
        print("\nINVALID GRADES")

def cc7():
    print("\nThis is my Code Challenge 7\n")
name = input("\nEnter your name ---> ")
grocery = input("\nDid you buy a grocery? (yes/no) ---> ")
if grocery.lower() == "yes":
        item = input("\nName of the item ---> ")
        price = eval(input("\nPrice of the item ---> "))
        amount = eval(input("\nExact amount given ---> "))
        age = eval(input("\nAge ---> "))
        tax = 0.123
        ttm = price * tax
        total = price + ttm
        if age <= 59:
            change = amount - total
            print(f"\nHi {name} you purchased a {item} , with a price of {price} plus 12.3% of tax ({ttm}) total of ({total}) ")
            print(f"\nAmount given ---> ({amount})php ")
            print(f"\nChange ---> [round(change , 2)] ")
            print("\nThank you for shopping! ")
        if age >= 60:	
            discount = 0.052
            ddm = price * 0.052
            dtotal = price - ddm
            cchange = amount - dtotal
            print(f"\nHi {name} you paid a price of {price}, for an {item} with a discount of 5.2% ({ddm}). The total amount you paid is (round{dtotal , 2}) ")
            print(f"\nAmount given ---> ({amount})php ")
            print(f"\nChange ---> {cchange} ")
            print("\nThank you for shopping! ")
else:
        print("\nThank you for checking in")	

def cc8():
    print("\nThis is my Code Challenge 8\n")
sum = 0
odd = 0
even = 0

for j in range(1,11):
        num = int(input(f"\nEnter a Number {j}:  "))
        sum += num 
        if num % 2 == 0:
            odd+=num
        else:
            even+=num

print(f"\nThe sum of all given numbers is {sum}")
print(f"\nThe even of all given numbers is {even}")
print(f"\nThe odd of all given numbers is {odd}")


def cc9():
    print("\nThis is my Code Challenge 9\n")
for x in range(0,11):
        print(" ",end=" ")
        for y in range(0,x):
            print(" ",end=" ")
        for z in range(x,10):
            print("*",end=" ")
        print()

def cc10():
    print("\nThis is my Code Challenge 10\n")
for x in range (6, 1, -1):
        for y in range(x, 1, - 1):
            print(" ", end =" ")
        for z in range(x, 7, 1):
            print("*",end=" ")
        for j in range (x, 6, 1):
            print("^",end=" ")
        print()

for x in range (1,7):
        for y in range(1, x, 1):
            print(" ", end =" ")
        for z in range(7, x, -1):
            print("^",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print()

def cc11():
    print("\nThis is my Code Challenge11\n")
for x in range(1, 8 + 1):
        print(" " * (8 - x + 1), end=" ")
        print(" *" * (x - 1))
for x in range(8 - 1, 0, - 1):
        print(" " * (8 - x + 1), end=" ")
        print(" *" * (x - 1))

def cc12():
    print("\nThis is my Code Challenge12\n")
for v in range(1, 8 + 1):
            print(" " * (8 - v), end="")
            print("*" * (v * 2 - 1))
for c in range(1, 10):
            print(" " * (4), end="")
            print("*" * (7))

def cc13():
    print("\nThis is my Code Challenge 13\n")
for x in range(1,6):
        for u in range(6,x,-1):
            print(" ",end= " " )
        for v in range(x,1,-1):
            print(v, end= " ")
        for y in range(1,x+1):
            print(y, end= " ")
        print()

for x in range(4,0,-1):
        for u in range(6,x,-1):
            print(" ",end= " " )
        for v in range(x,1,-1):
            print(v, end= " ")
        for y in range(1,x+1):
            print(y, end= " ")
        print()
def cc14():
    print("\nThis is my Code Challenge14\n")
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

def cc15():
    print("\nThis is my Code Challenge 15\n")
ting = True
nut = 0
while ting == True:
        ilan = input("\nDo you wish to create more triangle (yes/no) ? ")
        if ilan.lower() == "no":
            print("Program terminated")
            break
        elif ilan.lower() == "yes":
            nut += 1
            for x in range(1,6):
                for y in range(1,nut+1):
                    for z in range(1,x+1):
                        print("*", end= " ")
                    for a in range(5,x,-1):
                        print(" ", end= " ")
                    print( end= " ")
                print()
                continue
        else:
            print("\nInvalid input, Please enter 'yes' or 'no' only")
            continue


def cc16():
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
                print("\n=== Welcome to Metro-Bank ===")
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