from math import *
from time import *
import numpy as np
from playsound import *
from statistics import *
def arthematic():
    print("##########################################################################################################################")
    print("########################################## ARTHEMATIC OPERATIONS #######################################################")
    print("############################################################################################################################")
    playsound("arthematic.mpeg")
    print()
    sleep(2)
    con = 1
    while (con):
        print("a) Addition(+) --> PRESS 1 ")
        print("b) Substraction(-) --> PRESS 2 ")
        print("c) Multiplication(*) --> PRESS 3 ")
        print("d) Division (%) --> PRESS 4")
        print("e) power(x^y, x to the power y --> PRESS 5")
        print("f) square root (n^(1/2), x to the power half --> PRESS 6 ")
        print("g) expression evaluation(e.g.:- 3+7*5%3+8%2) --> PRESS 7")
        sleep(2)
        choice = int(input("enter your choice :- "))
        print(
            "<-----***********************########################################################**********************------>")
        if choice == 1:
            print("READY FOR ADDITION")
            sleep(1)
            sleep(1)
            print("write all the number to be added in a row , must be separated by space .for e,g, 2 5 6 8 ...")
            arr=[int(i) for i in input().split()]
            sleep(1)
            print("sum is :-",sum(arr))
            sleep(1)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice == 2:
            print("READY FOR SUBTRACTION")
            sleep(1)
            sleep(1)
            print("write all the number to be  subtracted in a row in a proper order , must be separated by space .for e,g, 2 5 6 8 ...")
            arr = [int(i) for i in input().split()]
            sub=arr[0]
            for i in arr[1:]:
                sub=sub-i
            sleep(1)
            print("subtractiob is :-", sub)
            sleep(1)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 3:
            print("READY FOR MULTIPLICATION")
            sleep(1)
            sleep(1)
            print("write all the number to be multiplication , must be separated by space .for e,g, 2 5 6 8 ...")
            arr = [int(i) for i in input().split()]
            mul = 1
            for i in arr[1:]:
                mul=mul*i
            print("multiplication  is :-", mul)
            sleep(2)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 4:
            print("READY FOR DIVISIONI")
            x=int(input("divident:-"))
            y=int(input("divisor:-"))
            z=x/y
            print(f" {x} divided by {y} gives {z}")
            print("quitient is",x//y,"and","reminder is",x%y)
            sleep(2)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 5:
            print("READY FOR POWER CALCULATION")
            x=int(input(" Base number:- "))
            y=int(input("Power :- "))
            z=x**y
            print(f" {x} to the power {y} is {z}")
            sleep(2)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 6:
            print("READY FOR SQUARE ROOT CALCULATION")
            x=int(input("Enter your number :-"))
            z=sqrt(x)
            print(f" Square root of {x} is {z}")
            sleep(2)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 7:
            print("READY FOR EXPRESSION SOLVING")
            print()
            s=input("Enter your BODMAS expresiion :- ")
            print(s+" =",eval(s))
            sleep(2)
            print( "<-----***********************########################################################**********************------>")
        else:
            print("Invalid number entered, please entered a valid one ")
            continue
        print("Do you want to perform more arthematic operation?")
        print( "for yes--> PRESS 1 and for No--> PRESS 0")
        con=int(input())
def conversion():
    print("##########################################################################################################################")
    print("########################################## NUMBER SYSTEM CONVERSION #######################################################")
    print("##########################################################################################################################")
    playsound("conversion.mpeg")
    sleep(2)
    con = 1
    while (con):
        print("a) BINARY CONVERSION --> PRESS 1 ")
        print("b) OCTAL CONVERSION--> PRESS 2 ")
        print("c) HEXADECIMAL COVERSION--> PRESS 3 ")
        print("d) DECIMAL CONVERSION --> PRESS 4")
        choice=int(input( "Enter your choice :- "))
        sleep(2)
        print(
            "<-----***********************########################################################**********************------>")
        print()
        n=input(" Enter the number to convert ")
        print()
        print(" Your entered number is in form??\n")
        print("a) BINARY FORM--> PRESS b/B ")
        print("b) OCTAL FORM--> PRESS O/o ")
        print("c) HEXADECIMAL FORM--> PRESS h/H ")
        print("d) DECIMAL FORM --> PRESS d/D")
        c=input()
        if c=="b" or c=="B":
            n= int(n,2)
        elif c=="O" or c=="O":
            n = int(n,8)
        elif c=="h" or c=="H":
            n = int(n,16)
        elif c=="d" or c=="D":
            n = int(n)
        if choice == 1:
            print(f"binary of {n} is ",bin(n)[2:])
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 2:
            print(f"octal of {n} is ", oct(n)[2:])
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 3:
            print(f"hexadecimal of {n} is ", hex(n)[2:])
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 4:
            print(f"decimal of {n} is ", n)
            print(
                "<-----***********************########################################################**********************------>")
        else:
            print("Invalid number entered, please entered a valid one ")
            continue
        sleep(2)
        print("Do you want to perform more conversions?")
        print("for yes--> PRESS 1 and for No--> PRESS 0")
        con = int(input())
def matrix():
    print("##########################################################################################################################")
    print("############################################ MATRIX OPERATIONS #######################################################")
    print("###########################################################################################################################")
    playsound("matrix.mpeg")
    sleep(2)
    con = 1
    while (con):
        print("a) Matrix Addition(+) --> PRESS 1 ")
        print("b) Matrix Substraction(-) --> PRESS 2 ")
        print("c) Matrix  elementwise Multiplication(*) --> PRESS 3 ")
        print("d) Matrix Multiplication(*) --> PRESS 4 ")
        print("e) Matrix division(%) --> PRESS 5 ")
        print("f) Matrix dot operations --> PRESS 6")
        print("g) determinant--> PRESS 7 ")
        print("h) Adjoints of a matrix--> PRESS 8 ")
        print("i) Inverse of a matrix--> PRESS 9 ")

        sleep(2)
        choice = int(input("enter your choice :- "))
        print(
            "<-----***********************########################################################**********************------>")
        if choice == 1:
            print("Matrix Addition")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1=int(input())
            print("enter no. column of the matrix 1")
            c1=int(input())
            arr=[]
            print(" enter element for your first matrix\n")
            for i in range(1,r1+1):
                print(f" enter row {i} having {c1} ")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2= int(input())
            brr = []
            print(" enter element for your  second matrix\n")
            for i in range(1, r2 + 1):
                print(f" enter row {i} having {c2} ")
                brr.append([int(z) for z in input().split()])
            arr=np.array(arr)
            brr=np.array(brr)
            print()
            if r1!=r2 or c1!=c2:
                print(" ERROR: different  shapes; dimensions of matrices must be same ")
            else:
                print(" matrix after addition")
                crr=arr+brr
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")


        elif choice == 2:
            print("Matrix Subtraction")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1 = int(input())
            print("enter no. column of the matrix 1")
            c1 = int(input())
            arr = []
            print(" enter element for your first matrix\n")
            for i in range(1, r1 + 1):
                print(f" enter row {i} having {c1} separated by single space")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2 = int(input())
            brr = []
            print(" enter element for your second matrix\n")
            for i in range(1, r2 + 1):
                print(f" enter row {i} having {c2} separated by single space")
                brr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            brr = np.array(brr)
            print()
            if r1 != r2 or c1 != c2:
                print(" ERROR: different  shapes; dimensions of matrices must be same ")
            else:
                print(" matrix after substraction")
                crr = arr - brr
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice == 3:
            print("Matrix element wise multiplication ( correspondind elements are get multiplied")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1 = int(input())
            print("enter no. column of the matrix 1")
            c1 = int(input())
            arr = []
            print(" enter element for your first matrix\n")
            for i in range(1, r1+ 1):
                print(f" enter row {i} having {c1} separated by single space ")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2 = int(input())
            brr = []
            print(" enter element for your second matrix\n")
            for i in range(1, r2 + 1):
                print(f" enter row {i} having {c2} separated by single space")
                brr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            brr = np.array(brr)
            print()
            if r1 != r2 or c1 != c2:
                print(" ERROR: different  shapes; dimensions of matrices must be same ")
            else:
                print(" matrix after element wise multiplication")
                crr = arr * brr
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice == 4:
            print("Matrix Multiplication")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1 = int(input())
            print("enter no. column of the matrix 1")
            c1 = int(input())
            arr = []
            print(" enter element for your first matrix\n")
            for i in range(1, r1 + 1):
                print(f" enter row {i} having {c1} separated by single space ")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2 = int(input())
            brr = []
            print(" enter element for your second matrix\n")
            for i in range(1, r2 + 1):
                print(f" enter row {i} having {c2} separated by single space ")
                brr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            brr = np.array(brr)
            print()
            if c1 != r2:
                print(" ERROR: dimensions of the entered matrixes are not valid for the multiplication.\n column of first matrix must be equal ro row of second matrix ")
            else:
                print(" matrix after Multiplication")
                crr =np.matmul(arr,brr)
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice == 5:
            print("Matrix Division")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1 = int(input())
            print("enter no. column of the matrix 1")
            c1 = int(input())
            arr = []
            print(" enter element for your first matrix\n")
            for i in range(1, r1 + 1):
                print(f" enter row {i} having {c1} separated by single space ")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2 = int(input())
            brr = []
            print(" enter element for your second matrix\n")
            for i in range(1, r2 + 1):
                print(f" enter row {i} having {c2} separated by single space ")
                brr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            brr = np.array(brr)
            print()
            if r1 != r2 or c1 != c2:
                print(" ERROR: different  shapes; dimensions of matrices must be same ")
            else:
                print(" matrix after division")
                crr = arr/brr
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice == 6:
            print("Matrix Dot Product(multiplies both the corresponding element of matrix and sum it ")
            sleep(1)
            print("enter no. row of the matrix 1")
            r1 = int(input())
            print("enter no. column of the matrix 1")
            c1 = int(input())
            arr = []
            print(" enter element for your first matrix\n")
            for i in range(1, n + 1):
                print(f" enter row {i} having {c1} separated by single space ")
                arr.append([int(z) for z in input().split()])
            print("enter no. row of the matrix 2")
            r2 = int(input())
            print("enter no. column of the matrix 2")
            c2 = int(input())
            brr = []
            print(" enter element for your second  matrix\n")
            for i in range(1, n + 1):
                print(f" enter row {i} having {c2} separated by single space ")
                brr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            brr = np.array(brr)
            print()
            if r1 != r2 or c1 != c2:
                print(" ERROR: different  shapes; dimensions of matrices must be same ")
            else:
                print(" matrix after Dot Product")
                crr =np.dot(arr,brr)
                for i in crr:
                    print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        elif choice==7:
            print(" Determinants of Matrix")
            sleep(1)
            print("enter no. row of the matrix")
            r = int(input())
            print("enter no. column of the matrix")
            c= int(input())
            arr = []
            print(" enter element for your matrix\n")
            for i in range(1, r + 1):
                print(f" enter row {i} having {c} separated by single space ")
                arr.append([int(z) for z in input().split()])
            if r!=c:
                print(" matrix should be square . row and coulumn must be equal")
            else:
                arr = np.array(arr)
                print()
                b=np.linalg.det(arr)
                print("determinat of the matrix is ",b)
            print(
                "<-----***********************########################################################**********************------>")
        elif choice==8:
            print(" adjoints of a Matrix")
            sleep(1)
            print("enter no. row of the matrix")
            r = int(input())
            print("enter no. column of the matrix")
            c = int(input())
            arr = []
            print(" enter element for your matrix\n")
            for i in range(1, r + 1):
                print(f" enter row {i} having {c} separated by single space")
                arr.append([int(z) for z in input().split()])
            arr = np.array(arr)
            print()
            if r!=c:
                print(" matrix should be square . row and coulumn must be equal")
            else:
                brr=np.linalg.inv()*np.linalg.det(arr)
                print("Adjoint of the matrix is ")
                print()
                for i in brr:
                    print(*i)
                print("<-----***********************########################################################**********************------>")
        elif choice==9:
            print(" Inverse of Matrix")
            sleep(1)
            print("enter no. row of the matrix")
            r = int(input())
            print("enter no. column of the matrix")
            c = int(input())
            arr = []
            print(" enter element for your matrix\n")
            for i in range(1, r+ 1):
                print(f" enter row {i} having {c}  separated by single space")
                arr.append([int(z) for z in input().split()])
            arr=np.array(arr)
            if r!=c:
                print(" matrix should be square . row and coulumn must be equal")
            else:
                if np.linalg.det(arr)==0:
                    print("determinant of the matrix is zero so inverse for singular matrix cant be calculated")
                else:
                    brr = np.linalg.inv(arr)
                    print("Inverse of the matrix is ")
                    print()
                    for i in brr:
                        print(*i)
            print(
                "<-----***********************########################################################**********************------>")

        else:
            print("Invalid number entered, please entered a valid one ")
            continue
        print("Do you want to perform more arthematic operation?")
        print("for yes--> PRESS 1 and for No--> PRESS 0")
        con = int(input())


def statistical():
    print("##########################################################################################################################")
    print("############################################ STATISTICAL ANALYSIS #######################################################")
    print("############################################################################################################################")
    playsound("statics.mpeg")
    sleep(2)
    con = 1
    while (con):
        print("a) Mean--> PRESS 1 ")
        print("b) Median --> PRESS 2 ")
        print("c) Mode --> PRESS 3 ")
        print("d) variance --> PRESS 4 ")
        print("e) standard deviation --> PRESS 5 ")
        print("f) Maximum and Minimum eliment --> PRESS 6")
        print("h) Full statictical analysis--> PRESS 7 ")
        sleep(2)
        choice = int(input("enter your choice :- "))
        print(
            "<-----***********************########################################################**********************------>")
        if choice == 1:
            print(" FINDING MEAN OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr=list(map(int,input().split()))
            print("Mean is ",mean(arr))
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 2:
            print(" FINDING MEDIAN OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Median is ", median(arr))
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 3:
            print(" FINDING MODE OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Mode is ", mode(arr))
            print("<-----***********************########################################################**********************------>")
        elif choice == 4:
            print(" FINDING VARIANCE OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Variance is ", variance(arr))
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 5:
            print(" FINDING STANDARD DEVIATION OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Standard Deviation is ", stdev(arr))
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 6:
            print(" FINDING MINIMUM AND MAXIMUM ELEMENT OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Minimum Element is ", min(arr))
            print("Maximum Element is ", max(arr))
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 7:
            print(" FULL STATISTICAL ANALYSIS OF THE DATA ")
            print(" Enter your data in a single row separated by a space ")
            print()
            arr = list(map(int, input().split()))
            print("Mean is ", mean(arr))
            print()
            print("Median is ", variance(arr))
            print()
            print("Mode is ", variance(arr))
            print()
            print("Variance is ", variance(arr))
            print()
            print("Standard Deviation is ", stdev(arr))
            print()
            print("Minimum Element is ", min(arr))
            print()
            print("Maximum Element is ", max(arr))
            print()
            print("Sum is ", sum(arr))
            print(
                "<-----***********************########################################################**********************------>")
        else:
            print("Invalid number entered, please entered a valid one ")
            continue
        print("Do you want to perform more arthematic operation?")
        print("for yes--> PRESS 1 and for No--> PRESS 0")
        con = int(input())


pass
def computation():
    print("##########################################################################################################################")
    print("############################################ MATHEMATICAL COMPUTATION  #######################################################")
    print("##########################################################################################################################")
    playsound("math.mpeg")
    sleep(2)
    con = 1
    while (con):
        print("a) log values --> PRESS 1 ")
        print("b) Degree to radian --> PRESS 2 ")
        print("c) Radian of the degree --> PRESS 3 ")
        print("d) expomemtial value(e^x)--> PRESS 4 ")
        print("e) factorial  --> PRESS 5 ")
        print("f) All trigonometric values --> PRESS 6")
        sleep(2)
        choice = int(input("enter your choice :- "))
        print(
            "<-----***********************########################################################**********************------>")
        if choice == 1:
            print(" FINDING VALUES OF LOAGRATHIMIC FUNCTION")
            print(" Enter the number")
            n=int(input())
            print(" Enter the base for the log (NOTE:- for natural lof PRESS --> e")
            b = int(input())
            print(f"Value of log{n} base {b}", log(n,b))
            print("<-----***********************########################################################**********************------>")
        elif choice == 2:
            print(" DEGREE TO RADIAN CONVERSION  ")
            print()
            print(" Enter the angle in degree")
            n=int(input())
            print(f"{n} degree is equals to", radians(n),"radian")
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 3:
            print(" DEGREE TO RADIAN CONVERSION  ")
            print()
            print(" Enter the angle in degree")
            n = int(input())
            print(f"{n} randian is equals to", degrees(n), "degree")
            print(
                "<-----***********************########################################################**********************------>")
        elif choice == 4:
            print(" FINDING VALUES OF EXPONENTIAL FUCTIONS")
            print()
            x=int(input("Enter the value(x) of the expotent power i.e. e^x ,value for x"))
            print(f"Exponent of {x} is", exp(x))
            print( "<-----***********************########################################################**********************------>")
        elif choice == 5:
            print(" FINDING FACTORIAL")
            print()
            n=int(input("Enter a number whose factorial is to be determined"))
            print(f"Factorial of {n} is ",factorial(n))
            print( "<-----***********************########################################################**********************------>")
        elif choice == 6:
            print(" FINDING VALUE FOR EACH TRIGONOMETRIC FUNCTION FOR ENTERED ANGLE ")
            print()
            n=int(input("Enter the angle in degree"))
            print(f"Sin{n} is equals to", sin(n*pi/360))
            print(f"Cos{n} is equals to", cos(n*pi/360))
            print(f"Tan{n} is equals to", tan(n*pi/360))
            print(f"Cot{n} is equals to", 1/tan(n*pi/360))
            print(f"Sec{n} is equals to", 1/cos(n*pi/360))
            print(f"Cosin{n} is equals to", 1/sin(n*pi/360))
            print("<-----***********************########################################################**********************------>")
        else:
            print("Invalid number entered, please entered a valid one ")
            continue
        print("Do you want to perform more arthematic operation?")
        print("for yes--> PRESS 1 and for No--> PRESS 0")
        con = int(input())


# MAIN CODE

print("##########################################################################################################################")
print("############################################ SCIENTITIC CALCULATOR #######################################################")
print("#############################################  created by- Y@shh   #######################################################")
print("##########################################################################################################################")
playsound("intro.mpeg")
print()
sleep(2)
con=1
while(con):
    print("What operations due you want of cope up with?????")
    print("A) Arthematic operations (+,-,*,%)-----> PRESS 1")
    print()
    print("B) Number system conversion( binary to decimal ,decimal to hexadecimal etc)-----> PRESS 2")
    print()
    print("C) Matrixes operations ( dot , addition multiplication) -----> PRESS 3")
    print()
    print("D) Statistical analysis  -----> PRESS 4")
    print()
    print("E)other mathematical value computation( log x,e^x,sin(),nPr,nCr etc) -----> PRESS 5")
    print()

    choice=int(input())
    if choice==1:
        arthematic()
    elif choice==2:
        conversion()
    elif choice==3:
        matrix()
    elif choice==4:
        statistical()
    elif choice==5:
        computation()
    else:
        print("Invalid number entered, please entered a valid one ")
        continue
    print("Do you want to use it more?\n for yes ---> PRESS 1  and  for No ---> PRESS 0")
    con=int(input())
print("Thanks for using ! Good bye")
playsound("goodbye.mpeg")