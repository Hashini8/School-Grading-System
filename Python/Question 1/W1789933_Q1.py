#Student Version

def main():
   
    credit_range = [0, 20, 40, 60, 80, 100, 120]

    pass_credits = 0
    defer_credits = 0
    fail_credits = 0

#pass credits
    while True:
        try:
            pass_credits = int(input("Please enter the number of pass credits : "))
            if pass_credits not in credit_range:
                print ("Range Error")
            elif pass_credits in credit_range:
                break
        except ValueError:
            print ("Integers required")

#defer credits
    while True:
        try:
            defer_credits = int(input("Please enter the number of defer credits : "))
            if defer_credits not in credit_range:
                print ("Range Error")
            elif defer_credits in credit_range:
                break
        except ValueError:
            print ("Integers required")

#fail credits
    while True:
        try:
            fail_credits = int(input("Please enter the number of fail credits : "))
            if fail_credits not in credit_range:
                print ("Range Error")
            elif fail_credits in credit_range:
                break
        except ValueError:
            print ("Integers required")
        
#progression outcome
    try:
        pass_credits = int(pass_credits)
        defer_credits = int(defer_credits)
        fail_credits = int(fail_credits)

        total_credits = pass_credits + defer_credits + fail_credits

        progression_outcome = "Pending"
        if (pass_credits % 20 == 0 and defer_credits % 20 == 0 and fail_credits % 20 == 0):
            if (total_credits == 120):

                if (pass_credits == 120):
                    progression_outcome = "Progress"
                elif (pass_credits == 100): 
                    progression_outcome = "Progress - module trailer"
                elif (pass_credits < 100 and fail_credits >= 80):
                    progression_outcome = "Exclude"
                else:
                    progression_outcome = "Do not progress - module retriever"
                print("Progression outcome: " + progression_outcome)
            else:
                print("Total Incorrect")
        else:
            print("Range error")
    except:
        print("Integers Required")

    repeat = input("Do you want to start again? ").lower()
    if repeat == "yes":
        main()
    else:
        print (exit)
        exit()
main()
