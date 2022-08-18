# def totalSum(arr):
#     count = 0
#     for i in arr:
#         count += i
            
#     average = count/len(arr)
#     return average

# list = [2, 4, 3, 9]
# averageScores = totalSum(list)
# print(averageScores)

def find_percentage(students, passed):
    percentage_that_passed = passed/students
    return percentage_that_passed


print(find_percentage(10, 5))
