studentList = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 40, 0], [80, 20, 20], [80, 0, 40], [60, 60, 0], [60, 40, 20], [60, 20, 40], [60, 0, 60], [40, 80, 0], [40, 60, 20], [40, 40,40], [40, 20, 60], [40, 0, 80], [20, 100, 0], [20, 80, 20], [20, 60, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 120, 0], [0, 100, 20], [0, 80, 40], [0, 60, 60], [0, 40, 80], [0, 20, 100], [0, 0, 120]]

numberOfProgressedStudents = 0
numberOfExcludedStudents = 0
numberOfTrailedStudents = 0
numberOfRetriveredStudents = 0

for singleStudent in studentList:
    try:
        pass_credits = int(singleStudent[0])
        defer_credits = int(singleStudent[1])
        fail_credits = int(singleStudent[2])

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

print("Progress: " + str(numberOfProgressedStudents) + ", Trailing: " + str(
                numberOfTrailedStudents) + ", Retriever: " + str(numberOfRetriveredStudents) + ", Excluded: " + str(
                numberOfExcludedStudents))

stars = ""

for i in range(numberOfProgressedStudents):
    stars += "*"
print("Progress " + str(numberOfProgressedStudents) + ": " + stars)

stars = ""

for i in range(numberOfRetriveredStudents):
    stars += "*"
print("Trailing " + str(numberOfRetriveredStudents) + ": " + stars)
stars = ""

for i in range(numberOfTrailedStudents):
    stars += "*"
print("Retriever " + str(numberOfTrailedStudents) + ": " + stars)

stars = ""

for i in range(numberOfExcludedStudents):
    stars += "*"
print("Excluded " + str(numberOfExcludedStudents) + ": " + stars)

print(str(
    numberOfExcludedStudents + numberOfTrailedStudents + numberOfRetriveredStudents + numberOfProgressedStudents),
    " outcomes in total")
