import question_a

def main():
    actual_value = int(input("Enter the actual value of a piece of property "))
    print("Assessment value", question_a.get_assessment_value(actual_value))
    print("Tax assessed", question_a.get_tax_assessed(question_a.get_assessment_value(actual_value)))

main()
