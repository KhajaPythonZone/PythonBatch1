from problems.problem1 import Problem1
from problems.problem2 import Problem2
from problems.problem3 import Problem3


def print_menu():
    print("""
    Welcome to Project Euler Answers
    Right now problem 1,2,3 is solved
    Which questions answer do you want to check?
    """)
    user_input = input("Enter the problem number")
    if user_input == "1":
        euler_problem = Problem1()
        euler_problem.compute()
    elif user_input == "2":
        euler_problem = Problem2()
        euler_problem.compute()
    elif user_input == "3":
        euler_problem = Problem3()
        euler_problem.compute()



if __name__ == '__main__':
    print_menu()
