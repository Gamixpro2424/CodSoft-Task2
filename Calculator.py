def getInput():
    a = float(input("Enter Number 1:"))
    b = float(input("Enter Number 2:"))
    return float(a),float(b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Math error"
def switch():
    while True:
            case = input("Enter Your Choice: ")
            if(case=='+' or case =='1' or case.lower() == 'addition' ):
                a,b = getInput()
                print(add(a,b))
            elif(case== '-' or case =='2' or case.lower() == 'subtraction'):
                a,b = getInput()
                print(sub(a,b))
            elif(case =='*' or case =='3' or case.lower() == 'multiplication'):
                a,b = getInput()
                print(multi(a,b))
            elif(case =='/' or case =='4' or case.lower() == 'division'):
                a,b = getInput()
                print(divide(a,b))
            elif(case.lower() in ['e','exit'] or case == '5'):
                break
            else:
                print("Invalid Input- Try Again")
print("***********Calculator************")
print("Select your Choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
switch()



