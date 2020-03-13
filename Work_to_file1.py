

def openFile(fileName, options):
    if options=="a":
       with open(fileName, options) as myFile:
             a=input()
             myFile.write("\n"+a)
    elif options=="r":
        with open(fileName, options) as myFile:
             line = myFile.readline()
             while line:
                print(line, end="") 
                line = myFile.readline()
    myFile.close()


def main():
   strFilename = input()
   strOption = input()
   openFile(strFilename, strOption)

   
main()