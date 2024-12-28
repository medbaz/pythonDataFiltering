#Run this prior to starting the exercise
from random import randint as rnd

memReg = r'C:\Users\DELL\Desktop\Cours_3D_impression\Python\pythonDataFiltering\members.txt'
exReg = r'C:\Users\DELL\Desktop\Cours_3D_impression\Python\pythonDataFiltering\inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):

    with open(currentMem,'r+') as currentMembers:
        with open(exMem,'a+') as oldMembers:

            currentMembers.seek(0,0)
            allMembers = currentMembers.readlines()
            header = allMembers.pop(0)


        #TODO: iterate through the members and create a new list of the innactive members


            currentMembers.seek(0)
            # print(allMembers)
            currentMembers.write(header)
            
            print(oldMembers.tell())
            print(currentMembers.tell())
            for member in allMembers:
                if ('no' in member):
                    oldMembers.write(member)
                else:
                    currentMembers.write(member)
                currentMembers.truncate()





        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem

        
    
    pass # Remove this line when done implementation





# The code below is to help you view the files.
# Do not modify this code for this exercise.


cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
    
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = r"C:\Users\DELL\Desktop\Cours_3D_impression\Python\pythonDataFiltering\testWrite.txt"
testAppend = r"C:\Users\DELL\Desktop\Cours_3D_impression\Python\pythonDataFiltering\testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does'nt match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    
