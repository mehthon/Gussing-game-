import random
attempt_list = []


def len_list():
    if len(attempt_list) == 0:
        print("NO gusses right now")
    else:
        print("you have guss {} number so far!".format(len(attempt_list)))
        

def start_game():
    number = random.randint(1,10)
    print("Hi welcome to our fun game!")
    print("You should guss our number and win")
    print("Good luck")
    try:
        while True:
            guss_number = int(input())
            attempt_list.append(guss_number)
            if guss_number == number:
                print("exactly conguratulation!")
                break
            else:
                print("NO try again")
                len_list()
                continue
    except ValueError as err:
        print("Oops invalid please try again...")
        print("{}".format(err))



start_game()
