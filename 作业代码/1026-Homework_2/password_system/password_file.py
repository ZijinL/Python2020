from hashlib import md5
from csv import writer as csv_writer
from csv import DictReader as csv_dictreader
import read_names, generate_password
from os.path import exists as file_exists

"""
save the password dict to file
or read a password from a file
password must be stored in md5 value
"""

def md5PassDict(passDict) -> dict:
    """
    for the safety of your password, we only save the md5 value of your password
    """
    md5Dict = {}
    dict.fromkeys(passDict.keys(), ' ')
    for each in passDict.keys():
        md5Dict[each] = md5(passDict[each].encode(encoding='UTF-8')).hexdigest()
    return md5Dict   

def savePassword(passDict) -> dict:
    """
    save the md5 value of password
    """
    md5Dict = md5PassDict(passDict)
    print("---[SAVE] pls input the csv filepath here, the file will be created if not exists---")
    filepath = read_names.inputFilepathCSV()
    header = ["name", "password"]
    with open(filepath, 'a+', newline="") as f:
        writer = csv_writer(f)
        writer.writerow(header)
        for item in md5Dict.items():
            writer.writerow(item)

def readPassword() -> dict:
    """
    read the md5 value of password from files and used to check password
    """
    print("---[READ] pls input the password filepath here---")
    filepath = read_names.inputFilepathCSV()
    while not file_exists(filepath):
        print("file not found")
        filepath = read_names.inputFilepathCSV()
    with open(filepath, 'r') as f:
        md5Dict = {}
        reader = csv_dictreader(f)
        for row in reader:
            md5Dict[row['name']]=row['password']
    return md5Dict

if __name__ == "__main__":
    testDict = {"ZhangSan": "3sqDf/UG", 
                "LiSi": "TlFHs-6r", 
                "WangWu": "yPJH8o@i", 
                "ZhaoLiu": "k8#hqhwJ"}
    generate_password.printPasswords(testDict)
    savePassword(testDict)
    md5Dict = readPassword()
    generate_password.printPasswords(md5Dict)
