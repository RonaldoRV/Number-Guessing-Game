print("""
 Welcome to Number Guessing Game 

x = **
""")

x = 20

while True:
    try:
        number_user = int(input("Enter a number and try to guess the saved number before: ")) 
    except ValueError:
        print("Write a number.")

    if number_user == x:
        print(f"Well doing the number is {x}")

    elif number_user < x:
        print(f"The number that you are looking is bigger")

    elif number_user > x:
        print(f"THe number that you are looking is smaller ")
    



