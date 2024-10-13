import question_c

def main():
    to_continue = True
    while (to_continue):
        day = int(input("Enter a number for the day of the week "))
        print(question_c.get_day_of_week(day))
        to_quit_or_not_to_quit = input("Do you want to quit? [y/n] ")
        if (to_quit_or_not_to_quit == "y" or to_quit_or_not_to_quit == "Y"):
            to_continue = False

main()
