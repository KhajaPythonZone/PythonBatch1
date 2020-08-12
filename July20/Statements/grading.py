maths = int(input("Enter the marks obtained in maths:  "))
physics = int(input("Enter the marks obtained in physics:  "))
chemistry = int(input("Enter the marks obtained in chemistry:  "))
average = (maths+physics+chemistry)/3
if average >= 70:
    print("Distinction")
elif average >= 60:
    print("First class")
elif average >= 50:
    print("Second class")
else:
    print("Third class")