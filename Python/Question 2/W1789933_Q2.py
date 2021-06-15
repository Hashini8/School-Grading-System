#Staff Version

shouldContinue = True
numberOfProgressedStudents = 0
numberOfExcludedStudents = 0
numberOfTrailedStudents = 0
numberOfRetriveredStudents = 0

while(shouldContinue):
    user_input = (input("Press any key to input student progress. 'q' to quit:"))

    if not(user_input == "q"):
        pass_credits = (input("Please enter the number of pass credits : "))
        defer_credits = (input("Please enter the number of defer credits : "))
        fail_credits = (input("Please enter the number of fail credits : "))

        try:
            pass_credits = int(pass_credits)
            defer_credits = int(defer_credits)
            fail_credits = int(fail_credits)

            total_credits = pass_credits + defer_credits + fail_credits

            progression_outcome = "Pending"
            if (pass_credits % 20 == 0 and defer_credits % 20 == 0 and fail_credits % 20 == 0):
                if (total_credits == 120):

                    if (pass_credits == 120):
                        numberOfProgressedStudents += 1
                    elif (pass_credits == 100):
                        numberOfTrailedStudents += 1
                    elif (pass_credits < 100 and fail_credits >= 80):
                        numberOfExcludedStudents += 1
                    else:
                        numberOfRetriveredStudents += 1
                else:
                    print("Total Incorrect")
            else:
                print("Range error")
        except:
            print("Integers Required")
    else:
        shouldContinue = False
        print("Progress: " + str(numberOfProgressedStudents) + ", Trailing: " + str(numberOfTrailedStudents) + ", Retriever: " + str(numberOfRetriveredStudents) + ", Excluded: " + str(numberOfExcludedStudents))

        stars = ""

        for i in range(numberOfProgressedStudents):
            stars += "*"
        print("Progress " + str(numberOfProgressedStudents) + ": " + stars)

        stars = ""

        for i in range(numberOfRetriveredStudents):
            stars += "*"
        print("Retriever " + str(numberOfRetriveredStudents) + ": " + stars)

        stars = ""

        for i in range(numberOfTrailedStudents):
            stars += "*"
        print("Trailing " + str(numberOfTrailedStudents) + ": " + stars)

        stars = ""

        for i in range(numberOfExcludedStudents):
            stars += "*"
        print("Excluded " + str(numberOfExcludedStudents) + ": " + stars)

        print("Total number of outcomes: " + str(numberOfExcludedStudents + numberOfTrailedStudents + numberOfRetriveredStudents + numberOfProgressedStudents))
