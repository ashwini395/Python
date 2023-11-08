def calculate_sum(data1, data2):
    # All the statements in the block of code must have the same level of indentation
    result_sum = data1 + data2
    return result_sum


result = calculate_sum(10, 20)
print(result)


# Write a Python program that converts temperature in Celsius to Fahrenheit and vice versa. Implement the
# requirements using functions. Hint: 0C= (0F-32)*(5/9)

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def convert_to_celsius(fahren):
    cel = (fahren - 32) * (5 / 9)
    return cel


temp = convert_to_fahrenheit(37)
print(temp)

temp = convert_to_celsius(98)
print(temp)


# lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    # Write your logic here
    adult_ticket_cost = 37550.0
    child_ticket_cost = adult_ticket_cost / 3;
    total_ticket_cost = (no_of_adults * adult_ticket_cost) + (no_of_children * child_ticket_cost)
    # Service Tax
    total_ticket_cost = total_ticket_cost + (total_ticket_cost * (7 / 100))
    # Discount
    total_ticket_cost = total_ticket_cost - (total_ticket_cost * (10 / 100))
    return total_ticket_cost


# Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(1, 2)
print("Total Ticket Cost:", total_ticket_cost)

total_ticket_cost = calculate_total_ticket_cost(5, 2)
print("Total Ticket Cost:", total_ticket_cost)

observe1="What's happening!!"

def passport_check(passport_no):
    observe4="actual copied to formal"
    observe5="func. execution starts"
    if(len(passport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    observe6="func. execution ends"
    return status

observe2="function with formal arg."
observe3="calling with actual arg."
passport_status=passport_check("M9993471")

print("Passport is",passport_status)
#observe1,2,3,4,5,6 are temporary variables used to explain this concept

#Code1
print("code-1")
def func1(a,b):
    return a+b

res=func1(5,10)
print("Value returned:",res)


#Code2:
print("------------------------------------")
print("code-2")
def func2():
    print("This code has nothing to return")
    return

func2()

#Code3:
print("------------------------------------")
print("code-3")
def func3():
    print("This code also has nothing to return and there is no return statement")

func3()

#Code 4:
print("------------------------------------")
print("code-4")
print("------------------------------------")
def func4(a,b):
    if(a>b):
        print("returns from if block")
        return a
    print("returns from outside if block")
    return b
print("1st invocation of code-4")
print("Value returned:",func4(10,5))
print("------------------------------------")
print("2nd invocation of code-4")
print("Value returned:",func4(2,3))




#Code1
print("code-1")
def func6(a,b,c):
    res_avg=(a+b+c)/3
    return res_avg
print("1st invocation of code-1")
func6(6,8,10)
print("returned value is not assigned to any variable")

print("------------------------------------------------")
print("2nd invocation of code-1")
average=func6(10,15,20)
print("returned value assigned to a variable")
print("value of variable, average:", average)

print("------------------------------------------------")
print("3rd invocation of code-1")
print("returned value is directly printed")
print(func6(1,2,3))



#Code2
print("------------------------------------------------")
print("code-2")
print("------------------------------------------------")
def func7(a,b):
    if(a>b):
        return True
    return False
x=5
y=6

print("1st invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")


x=6
y=5
print("------------------------------------------------")
print("2nd invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")

