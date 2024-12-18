def act_1():
    print("\nThis is my activity 1\n")
print("Hello World")

def act_2():
    name = input("Enter your name:")
    add = input("Enter your address:" )
    age = input("Enter your age:")

    print("Hi", name, "from",  add, "with age of", age)

    #string formatting

    print(f"Hi {name}, from {add}, with age of {age}")

def act3():
    fah = eval(input("Enter temperature in fahrenheit:"))

    c = ((fah - 32)*5) / 9

    print(round(c, 2))
    print(f"{fah} , degrees in fahrenheit converted to celsius is {round(c, 2)} ")

def act4():
    #+=  - incrementor
    #create a program the will assign 10 to the value of x

    x = 10
    print(x)

    x = x + 10
    print(x)

    x = x + 20
    print(x)

    #simplified version

    x+= 10
    print(x)

    #other with operation

    x *= 3
    print(x)

def act5():
    #introduction to decision structure

    #in some programming language or toturial
    password = "secret"

    mypassword = input("Enter Password ---->")

    if password == mypassword.lower():
        print("ACCESS PASSWORD")
        print("ENJOY USING THE SYSTEM")
    else:
        print("ACCES DENIED")
         
def act6():
     # SCHOLAR GRANT APPLICATION SYSTEM
    name = input("Hi, Please enter your name: ")
    isEnrolled = input("Are you currently enrolled in DLL? (yes / no): ")
    if isEnrolled.lower() == "yes":
        print(f"{name}, Welcome to DLL Scholarship Grant System")
        age = eval(input("How old are you right now? "))
        if age >= 18 and age <= 35:
            print("Your age complied to with the age requirement ")
            grades = eval(input("What was your GWA: "))
            if grades >= 86 and grades <= 100:
                print("Your grade pass the requirements")
                is4ps = input("Is your family is currently enrolled/subscribed to the 4ps? (yes / no): ")
                if is4ps.lower() == "yes":
                    print("Congratulation, you are now granted a scholarship ")
                else:
                    print("Oh sorry, pang 4ps lang")
            else:
                print("Oh sorry, your average, expired na")
        else:
            print("Your age is not qualified")
    else:
        print("Thank you for using the system")

def act7():
     sum = 0
     for i in range (0, 10):
        num = eval(input("Enter a number: "))
        sum += num
        print("The sum of all the given numbers is: ", sum)

def act8():
     start = int(input("Enter a starting point: "))
     limit = int(input("Enter a stopping point: "))

     for x in range(start, limit, 1):
         print(x)

     num = int(input("Enter any number: "))
     factorial = 1

     for x in range(num, 0, -1):
         factorial *= x

     print(f"The factorial of {num} is {factorial}")

def act12():
    num = int(input("Enter a number to calculate: "))

    for x in range(1, 11):
        for y in range(1, 10):
            print(x * y, end="\t")
        print()

    for x in range(1, 11):
        for y in range(1, num + 9):
            print(f"{x} x {y} = {x + y}", end="\t")
        print()

def act13():
    num = int(input("Enter no. of right triangle: "))

    for x in range(0, 6):   
        for z in range(0, num):
            for y in range(1, x + 1):      
                print("*", end=" ")
            for a in range(6, x, -1):
                print("", end= " ")
                print(end=" ")
        print()
def act14():
    tuloy = True
    nt = 0 #number of triangles

    while tuloy == True:
        ask = input("Do you wish to print more triangles? (yes/no) ----->")
        
        if ask.lower() == "no":
            print ("LOOP HAS ENDED") 
            break
            tuloy = False
            
        elif ask.lower() == "yes":
            nt += 1
            for x in range (1, 6):
                for r in range(1, nt + 1):
                    for y in range (1,x, + 1):
                        print("*", end= " ")
                    for z in range(6, x, -1):
                        print(" ", end=" ")
                    print(end=" ")
                print()
            continue
        else:
            print("INVALID SELECTION")
            print("PLEASE TYPE yes or no")
            continue

def act15():
    tuloy = True

    sum = 0
    while tuloy == True:
        num = eval(input("Enter any number: "))

        if num == 0:
            print("LOOP STOPPED")
            print(f"The sum of all numbers given is {sum}")
            break
            tuloy = False
                
        else:
            sum += num
            continue

def act16():
    def greet_Someone():
        print("Hi , hoped your having a delightful Tuesday afternoon.")


    def greet_Person(name):
        print(f"Hi {name}, hoped your having a delightful Tuesday afternoon.")

    def right_Triangle():
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(6, x, -1):
                print(" ",end= " ")
            print()

def Code_Challenge1():
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*")

def Code_Challenge2():
    print("Hi! Leah ")
print("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t*\t*\t Hi !\t Leah \t*\t*\t*\n\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t*")

def Code_Challenge3():
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

def Code_Challenge4():
    name = input("Enter your name: ") 
    print("Hi", name, ",") 
    deposit = eval(input("Enter the amount you want to deposit:"))

    oneT = deposit // 1000 
    oneT_rem = deposit % 1000 

    fiveH = oneT_rem // 500 
    fiveH_rem = oneT_rem % 500 

    twoH = fiveH_rem // 200 
    twoH_rem = fiveH_rem % 200 

    oneH = twoH_rem // 100 
    oneH_rem = twoH_rem % 100 

    fifty = oneH_rem // 50 
    fifty_rem = oneH_rem % 50 

    twenty = fifty_rem // 20 
    twenty_rem = fifty_rem % 20

    ten = twenty_rem // 10
    ten_rem = twenty_rem % 10

    five = ten_rem // 5
    five_rem = ten_rem % 50

    one = five_rem // 1
    one_rem = five_rem % 1
    print("Hi", name, ", your deposit amount breakdown in PH Denomination is as follows:") 
    print(oneT, "- 1,000")
    print(fiveH, "- 500")
    print(twoH, "- 200")
    print(oneH, "- 100")
    print(fifty, "- 50")
    print(twenty, "- 20")
    print(ten, "- 10")
    print(five, "- 5")
    print (one, "- 1")

def Code_Challenge5():
    prelim = eval(input("Enter Prelim Grade:")) 
    midterm = eval(input("Enter Midterm Grade: ")) 
    semifinal = eval(input("Enter Semifinal Grade:")) 
    final = eval(input("Enter Final Grade :")) 
    quiz = eval(input("Enter Quiz :")) 
    project = eval(input("Enter Project :")) 

    #Calculate the Final Grade 

    FG = (prelim*0.15)+(midterm*0.15)+(semifinal*0.15)+(final*0.15)+(quiz*0.25)+(project*0.15) 

    #Display Final Grade 

    print("Final Grade:", FG) 

    #Passed or Failed 

    if FG>=75: 
        print("Congratulation! You passed the course") 
    
    else: 
        print("Sorry, you failed")

def Code_Challenge6():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if 1 <= age <= 8:
        print("You're a Toddler")
    elif 9 <= age <= 14:
        print("You're a Preteen")
    elif 15 <= age <= 18:
        print("You're a Teenager")
    elif 19 <= age <= 27:
        print("You're in Early Adulthood")
    elif 28 <= age <= 44:
        print("You're in Middle Age")
    elif 45 <= age <= 59:
        print("You're in Post Adulthood")
    elif age >= 60:
        print("You're a Senior")
    else:
        print("Invalid age")

def Code_Challenge7():
    name = input("Enter your name: ")
    costumer = input("Did you purchase a grocery today ( yes/no )")
    if costumer.lower() == "yes" :
        item = input("What did you purchase?")
        price = eval(input("Item Price: "))
        #every price you'd purchase have tax of 12.3%
        #if you purchase more than 4000 you will get a discount of 3.8% for the untaxed price then get  12.3% discount
        if price > 4000 :
            discounted = price - (price * 0.038)
            print(f"We have a 3.8% discount for customers who purchase more than 4000 , current price:" , round(discounted,2))
            taxdis = discounted + (price * 0.123) 
            print("Every price you'd purchase have tax of 12.3%, current price: " , round(taxdis, 2))
            age = eval(input("Age: "))
            #if you are a senior who have an age of 60 - 150 you'd get 12.3% discount
            if age >= 60 and age <= 150 : 
                sdiscount = taxdis - ( discounted * 0.123)
                print(f"We have a 12.3% discount for senior costumers ")
                print("Total:" , round(sdiscount,2))
                pay =eval(input("Payment:"))
                change  = pay - sdiscount
                print("Change : " , round(change,2))
                print("Thank you and Have a nice day")
            else :
                pass
                print("Total :" , round(taxdis,2))
                pay =eval(input("Payment: "))
                change = pay - discounted
                print("Change : " , round(change,2))
                print("Thank you and Have a nice day")
        else :
            pass 
            #every price you'd purchase have tax of 12.3%
            taxp = price + (price * .123)
            print("Every price you'd purchase have tax of 12.3%, current price: " , round(taxp, 2))
            age = eval(input("Age: "))
            if age >= 60 and age <= 150 : 
                senior = taxp - (price * 0.123)
                print(f"We have a 12.3% discount for senior costumers")
                print("Total: " , round(senior,2))
                pay = eval(input("Payment: "))
                change = pay - senior
                print("Change:" , round(change,2))
                print("Thank you and Have a nice day")
            else :
                pass
                print("Total: " , round(taxp,2))
                pay = eval(input("Payment: "))
                change = pay - taxp
                print("Change:" , round(change,2))
                print("Thank you and Have a nice day")
    else :
        pass

def Code_Challenge8():
    equal = 0
    even = 0
    odd = 0

    for ikot in range (0, 10):
        num = eval(input("Enter a number: "))
        equal += num
        
        if num % 2 == 0:
            even += num
        else: 
            odd += num
            
    print(f"The sum of all the given numbers is:{equal}")
    print(f"The sum of odd numbers is:{odd}")
    print(f"The sum of even nunbers is:{even}")

def Code_Challenge9():
    for l in range(9, 0, -1):
        for y in range(9, l, -1):
            print(" ", end=" ")
        print(" *" * l)

def Code_Challenge10():
    for t in range(1, 6):
        for y in range(6, t, -1):
            print(" ", end=" ")
        print(" *" * t, end="")
        print("", end="")
        print(" *" * t)
        
    for z in range(5, 0, -1):
        for a in range(6, z, -1):
            print(" ", end=" ")
        print(" ^" * z, end="")
        print("", end="")
        print(" ^" * z)

def Code_Challenge11():
    for k in range(1, 7 + 1):
        print(" " * (7 - k), end="")
        print("*" * (k * 2 - 1))
    for k in range(7 - 1, 0, -1):
        print(" " * (7 - k), end="")
        print("*" * (k * 2 - 1))

def Code_Challenge12():
    for v in range(1, 8 + 1):
        print(" " * (8 - v), end="")
        print("*" * (v * 2 - 1))
    for c in range(1, 12):
        print(" " * (4), end="")
        print("*" * (7))

def Code_Challenge13():
    sum = 0
    isRepeat = True

    while isRepeat == True:
        num = eval(input("Enter a number:"))
        sum += num
        if num == 0:
            print(f"The sum of all the number is {sum}")
            break
            isRepeat = false
        else:
            sum += num
            continue

def Code_Challenge14():
    balance = 0

    def breakdown_denomination(amount):
        print("Denomination Breakdown:")
        denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
        for denom in denominations:
            if amount >= denom:
                count = amount // denom
                print("PHP", denom, ":", count)
                amount = amount % denom

    def create_account(name, initial_deposit=0):
        account_name = name
        global balance
        balance = initial_deposit
        print(f"ACCOUNT CREATED for \n {account_name} with initial deposit of {balance}")

    def check_balance():
        print(f"Current balance is {balance}")

    def deposit(amount):
        breakdown_denomination(amount)
        global balance
        choice = input("DO YOU WISH TO DEPOSIT THE AMOUNT? YES/NO: ").lower()
        if choice == "yes":
            balance += amount
            print(f"Amount deposited {amount}")
            check_balance()

    def withdraw(amount):
        global balance
        if balance >= amount:
            balance -= amount
            print(f"Withdrawal amount: {amount}")
            check_balance()
        else:
            print("Insufficient funds!")

    tuloy = True

    while tuloy:
        print("WELCOME TO MY BANK SIMULATION PROGRAM")
        print("SELECT FROM THE OPTION BELOW")
        print("1 --- CREATE ACCOUNT")
        print("2 --- CHECK BALANCE")
        print("3 --- DEPOSIT")
        print("4 --- WITHDRAW")
        print("5 --- EXIT")
        choice = input("Please choose a menu select from (1 - 5) --> ")

        if choice == "1":
            print("CREATE ACCOUNT SELECTED")
            full_name = input("Please input your full name: ")
            amount = input("Enter Initial Deposit Amount: ")
            create_account(full_name, amount)
            continue
            
        elif choice == "2":
            check_balance()
            continue
        elif choice == "3":
            print("DEPOSIT MENU SELECTED")
            amount = eval(input("Enter amount to deposit:"))
            deposit(amount)
        elif choice == "4":
            print("WITHDRAW MENU SELECTED")
            amount = eval(input("Enter amount to withdraw:"))
            withdraw(amount)      
        elif choice == "5":
            print("EXITING BANK PROGRAM")
            break
        else:
            print("INVALID CHOICE")
            continue


