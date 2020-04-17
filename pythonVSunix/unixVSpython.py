#You must download the .txt file for this to work

#!/usr/bin/python3
import os
from os import path
def buildURL(iNum,strID):
        #condition to output the correct instance number
        if iNum.lower()=='io':iNum='0'

        print("ID: {0} is in instance OHIO{1}".format(strID, iNum))

        #builds the correct URL
        url="https://mytots-exisiting-website/instance/s3cr3t{0}".format(iNum)

        #prints the URL for browser
        print("URL is: ",url)

def unixWay(vID,cFileName):
        #Unix command to extract the column 
        tempSTR2="cat "+cFileName+" | grep -i "+vID+" |cut -d '|' -f 6"
        print("\t\t\tUsage of GREP  and CUT")
        print("Python script will use this command \n{0}\n".format(tempSTR2))

        #stores output in variable
        readOutput=os.popen(tempSTR2).read()
        print(readOutput)

        #checks for the last 2 characters
        last2Chars=readOutput.strip()[-2:]
        buildURL(last2Chars , vID)



def pythonWay(vID,cFileName):
        #vars
        nElem=''

        print("\t\t\t Python Way Baby!\n Used the following\nMethods: split(), strip()\nLoops:for")

        '''Read the whole content of the file
        if path.exists(cFileName):
                fileX = open (cFileName,"r"
                lines=fileX.read()
                print(lines)
        '''
        #read line per line
        if path.exists(cFileName):
                #open in read mode
                fileX= open(cFileName,'r')
                #indicate to read per  line
                fileLines=fileX.readlines()
                #loop through lines
                for iPerLine in fileLines:
                        #remove spaces and inital and end symbols
                        #use of strip and split in the same line
                        dividedLine=iPerLine.strip("|").split()
                        #compare input ID with ID in that line
                        if vID==dividedLine[0]:
                                nElem=dividedLine[-2]
                                last2=nElem[-2:]
                                buildURL(last2,vID)
                #Dont forget to  close the file after finishing
                fileX.close()
def main():
        #constant
        vNameFile="ohioInstance.txt"
        #clear screen
        os.system("clear")
        varID=input("Enter ID: ")
        #unixWay(varID, vNameFile)
        pythonWay(varID, vNameFile)

if __name__ == "__main__": main()
