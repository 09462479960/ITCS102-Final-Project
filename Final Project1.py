import os

# Activities

def act1():
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
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")
    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def act4():
    print("\nThis is my activity 4\n")
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)
    print("The sum of", number1 ,"and",number2,"is",answer)

def act5():
    print("\nThis is my activity 5\n")
    print("\nFARENHEIT TO CELCIUS CONVERTER")
    temp = eval(input("\nEnter a temperature in Farenheit ---> "))
    celcius = (temp -32) * 5 / 9
    print("\nThe conversion of ", temp , " degrees Farenheit is ", celcius , " degrees Celcius.")
    print(f"\nThe conversion of {temp} degrees Farenheit is {celcius} degrees Celcius")
    (round(celcius, 2))
    print(f"\nThe convertion of {temp} degrees Farenheit is {round(celcius,2)} degrees Celcius.")

def act6():
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
    print("\nThis is my activity 9\n")
    age = eval(input("Enter your age --->  "))
    if age >=1 and age <=7:
        print("\nYour age is categorized as Toddler")
    elif age >=8 and age <=13:
        print("\nYour age is categorized as Pre-teen")
    elif age >=14 and age <=18:
        print("\nYour age is categorized as Teenager ")
    elif age >=19 and age <=31:
        print("\nYour age is categorized as Early Adulthood ")
    elif age >=32 and age <=45:
        print("\nYour age is categorized as Mid Adulthood ")
    elif age >=46 and age <=59:
        print("\nYour age is categorized as Post Adulthood ")
    elif age >=60 and age <=90:
        print("\nYour age is categorized as Senior ")
    elif age >=91 and age <=100:
        print("\nPwede ka na madeads tol ")
    else:
        print("\nnaman!! May agimat kaba?")

def act10():
    print("\nThis is my activity 10\n")
    name = input("Enter your name: ")
    isStudent = input("are your current student of DLL? (yes or No) -->")
    if isStudent.lower() == "yes":
        yearlevel = input("\n f - Freshman \n s - sophomore \n j - Junior \n r - Senior \n what is your current level right now in DLL? ")
        if yearlevel.lower() == "f":
            print(f"Hi {name} you are Freshman")
        elif yearlevel.lower() == "s":
            print(f"Hi {name} you are Sophomore ")
        elif yearlevel.lower() == "j":
            print(f"Hi {name} you are Junior")
        elif yearlevel.lower() == "r":
            print(f"Hi {name} you are Senior")
        else:
            print("Invalid choice")

def act11():
    print("\nThis is my activity 11\n")
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')

def act12():
    print("\nThis is my activity 12\n")
    for cycle in range (10,0,-1):
        (cycle)

def act13():
    print("\nThis is my activity 13\n")
    sum = 1
    num=int(input('Enter a number: '))
    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")

def act14():
    print("\nThis is my activity 14\n")
    for x in range ( 0, 11,):
        print(x,end =" ")
        for y in range (0, 11):
            print("*",end = " ")
        print("")

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
    tri = eval(input("Enter a number of triangle---> "))
    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()

def act20():
    print("\nThis is my activity 20\n")
    import os
isContinue =True
brrt = 0
while isContinue == True:
    ngi=input("Would you like to add another triangle (yes/no)? ")
    if ngi.lower() == "no":
        print("PROGRAM TERMINATED")
        break
    else:
        os.system('cls')
        brrt += 1
        for x in range(1,6):
            for y in range(brrt+1):
                for z in range(1,x+1):
                    print("*", end= " ")
                for a in range(5,x,-1):
                    print(" ", end= " ")
                print( end= " ")
            print()
        continue    
    isContinue =True
    brrt = 0
    while isContinue == True:
        ngi=input("Would you like to add another triangle (yes/no)? ")
        if ngi.lower() == "no":
            print("PROGRAM TERMINATED")
            break
        else:
            os.system('cls')
            brrt += 1
            for x in range(1,6):
                for y in range(brrt+1):
                    for z in range(1,x+1):
                        print("*", end= " ")
                    for a in range(5,x,-1):
                        print(" ", end= " ")
                    print( end= " ")
                print()
            continue    

def act21():
    print("\nThis is my activity 21\n")
    def pang_hi():
        print("HI IT1C")
        def pang_hi_v2(name):
            print(f"Hello {name}")
        def termi():
            print("PROGRAM TERMINATED")
        def activity_2():
            number1 = eval (input("enter a number--->" ))
            number2 = eval (input("enter another number--->" ))
            answer = (number1 + number2)
            print(f"The sum of {number1} and {number2} is {answer}")
        tuloy =  True
        while tuloy == True:
            ask = input("Enter a name---> ")
            if ask.lower() != "stop":
                pang_hi_v2(ask)
                if ask == "2":
                    activity_2()
                    continue
            else:
                termi()
                break
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
    from Activity23 import factorial
    print(f"the factorial of 7 is {factorial(7)} ")

def act25():
    print("\nThis is my activity 25\n")
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]
    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")
    print(courses)

#Code_Challenge

def codechallenge1():
    print("\nThis is my Code Challenge 1\n")
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")

def codechallenge2():
    print("\nThis is my Code Challenge 2\n")
    name = input("\nType your name here --->")
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*","  Hi",name,"\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")

def codechallenge3():
    print("\nThis is my Code Challenge 2\n")
    lname = input("\nPlease type your last name ---> ")
    fname = input("\nPlease type your first name ---> ")
    mname = input("\nPlease type your middle name ---> ")
    age = input("\nPlease type your age ---> ")
    gender = input("\nPlease type your gender ---> ")
    birthdate = input ("\nPlease type your birth date ---> ")
    birthmonth = input ("\nPlease type your birth month ---> ")
    birthyear = input ("\nPlease type your birth year ---> ")
    maritalStatus = input("\nPlease type your marital status ---> ")
    religion = input("\nPlease type your religion ---> ")
    nationality = input("\nPlease type your nationality ---> ")
    height = input("\nPlease type your height in cm ---> ")
    weight = input("\nPlease type your weight in kg ---> ")
    contactnumber = input("\nPlease type your contact number ---> ")
    email = input ("\nPlease type your e-mail ---> ")
    address = input("\nPlease type your home address ---> ")
    fname = input("\nPlease type your father's full name ---> ")
    mname = input("\nPlease type your mother's full name ---> ")
    hobby = input ("\nPlease type your hobby ---> ")
    print ("\nHello, My name is" , lname , fname , mname ,  "and I'm" , str(age) , "years old," , gender , "\n I was born on" , birthmonth , birthdate , birthyear , "\n And right now I am" , maritalStatus , "\n My religion is" , religion , "\n I am" , nationality ,  "and my height is" , height , "cm" " and I'm" , weight , "kl" , "\n You can contact me at my number" , contactnumber , "\n And you may also contact me through my e-mail" , email , "\n I live in" , address , "\n My father is" , fname , "and my mother is" , mname , "\n And lastly, I love" , hobby )

def codechallenge4():
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

def codechallenge5():
    print("\nThis is my Code Challenge 5\n")
    lname = input("\nType your last name ---> ")
    fname = input("\nType your first name ---> ")
    mname = input("\nType your middle name ---> ")
    prtt1 = eval(input("\nAmount to deposit ---> "))
    blck1 = prtt1 // 1000
    brtt1 = prtt1 % 1000
    blck2 = brtt1 // 500
    brtt2 = brtt1 % 500
    blck3 = brtt2 // 200
    brtt3 = brtt2 % 200
    blck4 = brtt3 // 100
    brtt4 = brtt3 % 100
    blck5 = brtt4 // 50
    brtt5 = brtt4 % 50
    blck6 = brtt5 // 20
    brtt6 = brtt5 % 20
    blck7 = brtt6 // 10
    brtt7 = brtt6 % 10
    blck8 = brtt7 // 5
    brtt8 = brtt7 % 5
    blck9 = brtt8 // 1
    brtt9 = brtt8 % 1
    print("\nHello", fname , mname , lname ,"this is the breakdown of your deposit: \n")
    print(blck1 ," - 1000")
    print(blck2 ," - 500")
    print(blck3 ," - 200")
    print(blck4 ," - 100")
    print(blck5 ," - 50")
    print(blck6 ," - 20")
    print(blck7 ," - 10")
    print(blck8 ," - 5")
    print(blck9 ," - 1")

def codechallenge6():
    print("\nThis is my Code Challenge 6\n")
    blck1 = eval(input("\nEnter your grades in Prelims ---> "))
    blck2 = eval(input("\nEnter your grades in Midterms ---> "))
    blck3 = eval(input("\nEnter your grades in Semi-Finals ---> "))
    blck4 = eval(input("\nEnter your grades in Finals ---> "))
    blck5 = eval(input("\nEnter your grades in Quizzes ---> "))
    blck6 = eval(input("\nEnter your grades in Projects ---> "))

    if (blck1 >= 65 and blck1 <=100) and (blck2 >= 65 and blck2 <=100) and (blck3 >= 65 and blck3 <=100) and (blck4 >= 65 and blck4 <=100) and (blck5 >= 65 and blck5 <=100) and (blck6 >= 65 and blck6 <=100):
        brtt = (blck1 * 0.15) + (blck2 * 0.15) + (blck3 * 0.15) + (blck4 * 0.15) + (blck5 * 0.25) + (blck6 * 0.15) 
        if brtt >= 75:
            print("\nCongratulations for passing the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
        else:
            print("\nYou failed for the Semester ")
            print(f"\nThis is your grades for the Semester {brtt} ")
    else:
        print("\nINVALID GRADES")

def codechallenge7():
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

def codechallenge8():
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


def codechallenge9():
    print("\nThis is my Code Challenge 9\n")
    for x in range(0,11):
        print(" ",end=" ")
        for y in range(0,x):
            print(" ",end=" ")
        for z in range(x,10):
            print("*",end=" ")
        print()

def codechallenge10():
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

def codechallenge11():
    print("\nThis is my Code Challenge 11\n")
    for x in range (7, 1, -1):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(7, x,- 1):
            print("*",end=" ")
        for j in range (5, x ,- 1):
            print("*",end=" ")
        print()     
    for x in range (1,7):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(4, x, -1):
            print("*",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print()

def codechallenge12():
    print("\nThis is my Code Challenge 12\n")
    for j in range(6,1-1):
        for v in range(1,j):
            print(" ",end=" ")
        for q in range(7,j -1):
            print("*",end=" ")
        for q in range(6,j -1):
            print("*",end=" ")
        print()
    for t in range(1,7):
        for p in range(1,5):
            print(" ",end=" ")
        for s in range(1,4):
            print("*",end=" ")
        print()

def codechallenge13():
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

def codechallenge14():
    print("\nThis is my Code Challenge 14\n")
    dang = True
    bilang = 0
    while dang == True:
        num = eval(input("Write a number:   "))
        if num == 0:
            print("Loop has terminated")
            print(f"The sum of all numbers given is {bilang}")
            break
        else:
            bilang += num
            continue

def codechallenge15():
    print("\nThis is my Code Challenge 15\n")
    ting = True
    nut = 0
    while ting == True:
        ilan = input("\nDo you wish to create more triangle (yes/no) ? ")
        if ilan.lower() == "no":
            os.system("cls")
            print("Program terminated")
            break
        elif ilan.lower() == "yes":
            os.system("cls")
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
            os.system
            print("\nInvalid input, Please enter 'yes' or 'no' only")
            continue


def codechallenge16():
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
                break
            else:
                print("Invalid option. Please try again.")
    main()

# Menu & Body
def body():
    tuloy = True
    while tuloy == True:
        def body():
            print(f"\nWelcome to code compilation of Zyra Marie Pureza")
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
                print(f"\nWelcome to code compilation of Zyra Marie Pureza")
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
    print(f"\nWelcome to code compilation of Zyra Marie Pureza")
    print(f"Bachelor Of Science In Infomation Technology - 1C")

def cc_folder():
    print(f"\nWelcome to code compilation of Zyra Marie Pureza")
    print(f"Bachelor Of Science In Infomation Technology - 1C")
