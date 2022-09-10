import random
amount = input("How many pencils would you like to use")


def value_errors():
    global a
    while True:

        if a not in list_num:
            a = input("Possible values: '1', '2' or '3'")
        else:
            break


while True:
    global val

    try:
        val = int(amount)
        if val < 0:
            print("The number of pencils should be numeric")
            amount = input()
        elif val == 0:
            amount = input("The number of pencils should be positive")
        elif val > 0:
            break

    except ValueError:
        print("The number of pencils should be numeric")
        amount = input()


player_1 = input("Who will be the first (John, Jack)")

while True:
    if player_1 == "John":
        break
    elif player_1 == "Jack":
        break
    player_1 = input("Choose between 'John' and 'Jack'")


if player_1 == "John":  # bot implementation
    player_2 = "Jack"
else:
    player_2 = "John"


turn = True
list_num = ["1", '2', '3']
while val > 0:
    print("|" * val)
    if turn:
        if player_1 == "Jack":
            if val % 4 == 0:
                a = str(3)
            elif (val + 1) % 4 == 0:
                a = str(2)
            elif (val + 2) % 4 == 0:
                a = str(1)
            elif val == 1:
                a = str(1)
            else:
                a = str(random.randint(1, 3))
            value_errors()  # function of problem 5
            print(player_1 + "'s turn:")
            print(a)
            a = int(a)
            while a > val:
                a = int(input("Too many pencils were taken"))

            val = val - a
            turn = False
        else:
            a = input(player_1 + "'s turn:")
            value_errors()  # function of problem 5
            a = int(a)
            while a > val:
                a = int(input("Too many pencils were taken"))
            val = val - a
            turn = False


    else:
        if player_2 == "Jack":

           if val % 4 == 0:
              a = str(3)
           elif (val + 1) % 4 == 0:
              a = str(2)
           elif (val + 2) % 4 == 0:
              a = str(1)
           elif val == 1:
              a = str(1)
           else:
               a = str(random.randint(1, 3))

           print(player_2 + "'s turn:")
           print(a)

        else:
            a = input(player_2 + "'s turn:")
            value_errors()  # function of problem 5
            a = int(a)
            while a > val:
                a = int(input("Too many pencils were taken"))

        val = val - int(a)
        turn = True
if turn:
    print(player_1 + " won!")
else:
    print(player_2 + " won!")
