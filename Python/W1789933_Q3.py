#Vertical Histogram

shouldContinue = True
numberOfProgressedStudents = 0
numberOfExcludedStudents = 0
numberOfTrailedStudents = 0
numberOfRetriveredStudents = 0

while shouldContinue:
    user_input = input("Press any key to input student progress. 'q' to quit:")

    if not(user_input == "q"):
        #code
        pass_credits = (input("please enter number of pass credits : "))
        defer_credits = (input("please enter number of defer credits : "))
        fail_credits = (input("please enter number of fail credits : "))

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
            print("Not an integer")
    else:
        shouldContinue = False

        header = "{:^12s}".format("Progress") + "{:^12s}".format("Trailing") + "{:^12s}".format("Retriever") + "{:^12s}".format("Excluded")
        print(header)

        maxCount = numberOfProgressedStudents
        if (maxCount < numberOfExcludedStudents):
            maxCount = numberOfExcludedStudents
        if (maxCount < numberOfRetriveredStudents):
            maxCount = numberOfRetriveredStudents
        if (maxCount < numberOfTrailedStudents):
            maxCount = numberOfTrailedStudents

        currentSymbol = ""

        for i in range(maxCount):

            row = ""

            if i + 1 <= numberOfProgressedStudents:
                currentSymbol = "*"
            else:
                currentSymbol = " "

            row += "{:^12s}".format(currentSymbol)

            if i + 1 <= numberOfTrailedStudents:
                currentSymbol = "*"
            else:
                currentSymbol = " "

            row += "{:^12s}".format(currentSymbol)

            if i + 1 <= numberOfRetriveredStudents:
                currentSymbol = "*"
            else:
                currentSymbol = " "

            row += "{:^12s}".format(currentSymbol)

            if i + 1 <= numberOfExcludedStudents:
                currentSymbol = "*"
            else:
                currentSymbol = " "

            row += "{:^12s}".format(currentSymbol)

            print(row)
