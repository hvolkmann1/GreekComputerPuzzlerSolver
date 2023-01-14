
#This code is designed to solve a puzzle called "the greek wheel"
#All the numbers in each column must add up to '42'


import numpy as np

#below are the 
c0 = np.array([[15,0,8,0,3,0,6,0,10,0,7,0]]) #Must be a 2D array for "shiftArray" to work

c1 = np.array([[11,11,6,11,0,6,17,7,3,0,6,0],
               [0,14,0,9,0,12,0,4,0,7,15,0]])

c2 = np.array([[13,9,7,13,21,17,4,5,0,7,8,9],
               [6,15,4,9,18,11,26,14,1,12,0,21],
               [0,10,0,8,0,22,0,16,0,9,0,5]])

c3 = np.array([[0,9,0,7,14,11,0,8,0,16,2,7],
               [20,12,3,6,0,14,12,3,8,9,0,9],
               [26,6,0,2,13,9,0,17,19,3,12,3],
               [0,9,0,12,0,6,0,10,0,10,0,1]])

c4 = np.array([[14,11,14,11,11,14,11,14,11,14,14,11], #! Never shift this circle, it is the base circle
               [13,14,15,4,5,6,7,8,9,10,11,12],
               [21,9,9,4,4,6,6,3,3,14,14,21],
               [8,7,8,8,3,4,12,2,5,10,7,16]])

# This shifts the array / mimics shifting of the circle basically (counter clockwise) 
def shiftArray(array):
    for i in range(0,len(array)):
        temp = np.insert(array[i], 0, array[i][-1])
        array[i] = temp[:-1]
    return array

# This calculates the sum and returns a boolean
def find42(num1, num2, num3 = 0, num4 = 0):
    if(num1 + num2 + num3 + num4 == 42):
        return True
    else:
        return False

# The following 4 are simple, they return the number given the required circles
def getNum1(c3, c4):
    if(c3[3][0] == 0):
        return c4[3][0]
    else:
        return c3[3][0]

def getNum2(c2, c3, c4):
    if(c2[2][0] == 0):
        if(c3[2][0] == 0):
            return c4[2][0]
        else:
            return c3[2][0]
    else:
        return c2[2][0]

def getNum3(c1, c2, c3, c4):
    if(c1[1][0] == 0):
        if(c2[1][0] == 0):
            if(c3[1][0] == 0):
                return c4[1][0]
            else:
                return c3[1][0]
        else:
            return c2[1][0]
    else:
        return c1[1][0]

def getNum4(c0, c1, c2, c3, c4):
    if(c0[0][0] == 0):
        if(c1[0][0] == 0):
            if(c2[0][0] == 0):
                if(c3[0][0] == 0):
                    return c4[0][0]
                else:
                    return c3[0][0]
            else:
                return c2[0][0]
        else:
            return c1[0][0]
    else:
        return c0[0][0]

#This checks for the solution (activate if find42 is correct)
def checkSolution(c0, c1, c2, c3, c4):
    shifts = 0
    for w in range(0,12):
        temp1 = getNum1(c3, c4)
        temp2 = getNum2(c2, c3, c4)
        temp3 = getNum3(c1, c2, c3, c4)
        temp4 = getNum4(c0, c1, c2, c3, c4)

        #shifting to re-align the indecies to make checking easier
        c0 = shiftArray(c0)
        c1 = shiftArray(c1)
        c2 = shiftArray(c2)
        c3 = shiftArray(c3)
        c4 = shiftArray(c4) # in this case, and this case only do we shift c4 to maintain the correct order. 
        shifts = shifts + 1
        
        if not find42(temp1, temp2, temp3, temp4):
            for n in range(0, 12-shifts):
                c0 = shiftArray(c0)
                c1 = shiftArray(c1)
                c2 = shiftArray(c2)
                c3 = shiftArray(c3)
                c4 = shiftArray(c4)
            return False
        print(temp1, temp2, temp3, temp4)
        if(w > 10):
            print("Solution found!")
            return True

#these circles track what shifts in numbers are occuring
c0Shifts = 0
c1Shifts = 0
c2Shifts = 0
c3Shifts = 0


#sets the break case for the end
solution = False

for i in range(0,12): # set num1 (outer most layer)
    num1 = getNum1(c3, c4)
    for j in range(0,12): #set num2
        num2 = getNum2(c2, c3, c4)
        if(num1 + num2 >= 42): #this checks the sum of the first three rows, if they are over 42 then it should shift without checking the following circles
            continue
        for k in range(0,12): #set num3
            num3 = getNum3(c1, c2, c3, c4)
            if(num1 + num2 + num3 >= 42): #this checks the sum of the first three rows, if they are over 42 then should shift without checking the following circles
                continue
            for m in range(0,12): #set num4 (inner most layer)
                num4 = getNum4(c0, c1, c2, c3, c4)
                if(find42(num1, num2, num3, num4)):
                    solution = checkSolution(c0, c1, c2, c3, c4)
                if(solution):
                    break
                shiftArray(c0)
                c0Shifts = c0Shifts + 1
            if(solution):
                break
            shiftArray(c1)
            c1Shifts = c1Shifts + 1
        if(solution):
            break
        shiftArray(c2)
        c2Shifts = c2Shifts + 1
    if(solution):
        break
    shiftArray(c3)
    c3Shifts = c3Shifts + 1



# This simplifies the number of shifts on the circles so we can figure out how to find the solution on the physical puzzle
c0Shifts = c0Shifts % 12
c1Shifts = c1Shifts % 12
c2Shifts = c2Shifts % 12
c3Shifts = c3Shifts % 12

#Finishing output
print("Here are the number of turns you should do to find the correct solution!")
print("(inner to outter)")
print(c0Shifts, c1Shifts, c2Shifts, c3Shifts)
print()
