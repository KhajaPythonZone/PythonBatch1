maths = int(input("Enter the marks obtained in maths:  "))
physics = int(input("Enter the marks obtained in physics:  "))
chemistry = int(input("Enter the marks obtained in chemistry:  "))
average = (maths+physics+chemistry)/3
if average >= 70:
    print("Distinction")
if 60 <= average < 70:
    print("First class")
if 50 <= average < 60:
    print("second class")
if average < 50:
    print("third class")