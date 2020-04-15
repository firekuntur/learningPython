#libraries
import os
from os import path
import logging

def deleteFile(fileName):
  tempSTR="rm -rf "+fileName
  if path.exists(fileName):
    os.system(tempSTR)
    logging.warning("File Deleted")

def main():

  #constant filename
  cFileName="test.txt"
  url="http://files.usgwarchives.net/id/bearlake/military/ww1/wwiblkHE_I.txt"
  
  #for windows
  #os.system("cls")  
  
  #unix based 
  os.system("clear")  
  
  #check if file exists
  if path.exists(cFileName):
    logging.warning("***File Found")
    fileX = open (cFileName,"r")
    lines=fileX.read()
    print(lines)

    if input("DO YOU WANT TO DELETE FILE? (Y/N) ")=="Y":
    #deletes the file calling the funciton  
      deleteFile(cFileName)
  else:
    logging.warning("***ERROR****\nFile NOT Found")
    #created file manually
    #fileX = open (cFileName,"w+")
    #logging.warning("File created")
    
    #build unix command
    tempSTR="curl -o "+cFileName+" "+url
    #print(tempSTR)
    #sends commandY
    os.system(tempSTR)
    logging.warning("File downloaded from URL:", url)
if __name__ == "__main__":
  main()
