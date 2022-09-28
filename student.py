#You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
#'A': Absent.
#'L': Late.
#'P': Present.
#The student is eligible for an attendance award if they meet both of the following criteria:
#The student was absent ('A') for strictly fewer than 2 days total.
#The student was never late ('L') for 3 or more consecutivedays.
#Return true if the student is eligible for an attendance award, or false otherwise.
#Example 1:
#Input: s = "PPALLP"
#Output: true
#Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

def student(s):
    if 'LLL' in s:
        return False

    else: 
        return True


print(student('PPALLP'))

def grad(week):
    absent = 0
    late = 0
    for day in week:
        if day == 'A':
            absent = absent + 1
            if absent >= 2:
                return False
        elif day == 'L':
            late = late + 1
            if late >= 3:
                return False
    return True


print(grad('PPLLLA'))
