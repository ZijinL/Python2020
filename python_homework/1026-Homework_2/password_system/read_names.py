from os.path import exists as file_exists
from csv import reader as csv_reader

"""
return a list of names from a file or the keyboard
"""

def readUserName() -> list:
    """
    easy to input/import lots of names
    return a list of names
    """
    state = input("Do you want to mannually type names or import names from files? (type/import): ")
    while state not in ['type', 'import']:
        state = input("Invalid value, pls enter again: ")
    if state=='type':
        return inputUserName()
    else:
        return importUserName()
        
def inputFilepathCSV() -> str:
    """
    input the filepath of a CSV file
    check the validity of the filepath
    """
    filepath = input("Pls input the CSV filepath:(input 'exit' to terminate) ").strip('"')
    # only usable for .csv files on your computer, only tested on Win10 
    while not filepath.endswith(".csv"):
        if filepath == "exit":
            raise Exception("User quit the program mannually")
        filepath = input("Invalid value! Pls input the CSV filepath: ").strip('"')

    return filepath
    
def importUserName() -> list:
    """
    MUST import os before use
    only applicalbe for .csv files
    names must stored in the first column
    return a list of names
    """
    filepath = inputFilepathCSV()
    while not file_exists(filepath):
        print("file not found")
        filepath = inputFilepathCSV()
    # only usable for small files(less than 10,000 lines, can't used in big data)
    with open(filepath, 'r') as f:
        f_csv = csv_reader(f)
        # name must be stored in first column or we need do further preprocess
        nameList = [row[0].strip('\n') for row in f_csv]
    return nameList
    
def inputUserName() -> list:
    """
    input names mannually
    return a list of names
    """
    nameList = input("input names, seperated by space/tab: ")
    return nameList.split()

if __name__ == '__main__':
   print(*readUserName())
