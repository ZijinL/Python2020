from random import choice, shuffle

"""
generate a password dict for all users
"""

def charLibrary() -> dict:
    """
    generate a char libray, easy to adjust the characters in your password
    """
    specChar = "+-*/?!@#$%&"
    numsChar = [str(i) for i in range(10)]
    alphaChar = [chr(i+ord('a')) for i in range(26)] + [chr(i+ord('A')) for i in range(26)]
    alphaChar_upper = [chr(i+ord('A')) for i in range(26)]
    alphaChar_lower = [chr(i+ord('a')) for i in range(26)]
    return {"spec": specChar, "num": numsChar, "alpha": alphaChar, "alpha_upper": alphaChar_upper, "alpha_lower": alphaChar_lower}

def setPassLength() -> int:
    """
    set the length of password
    """
    length = input("Pls enter the length for password(2-256): ")
    while (not length.isdigit() or not 2 <= int(length) <= 256):
        length = input("Invalid input! \nPls enter the length for password(2-256): ")
    return int(length)

def generatePassword(length = 2, alphaState = 0, passStrenth = 0) -> str:
    """
    MUST import random befor use
    generate a password for one user
    include one number and one special char
    length(2): password length
        2: minimum length for this function
    alphaState(0): check if you need upper cases or lower cases or both
        0: both upper cases and lower cases, 1: upper cases, 2: lower cases
    passStrength(0): set pass word strength, reserved for future version
        0: default state, include one number and one special char 
    """
    if alphaState == 0:
        alphaChar = charLibrary()["alpha"]
    elif alphaState == 1:
        alphaChar = charLibrary()["alpha_upper"]
    elif alphaState == 2:
        alphaChar = charLibrary()["alpha_lower"]
    else:
        raise ValueError("Invalid alphaState")
        
    password = []
    # generate (length-2) letters
    for counts in range(length-2):
        password.append(choice(alphaChar))
        counts += 0 # avoid 'not used' error alert
    password.append(choice(charLibrary()["num"]))
    password.append(choice(charLibrary()["spec"]))
    shuffle(password)
    return "".join(password)

def userPasswords(userList, length) -> dict:
    """
    generate a password for every single user in user list
    """
    passDict = {}
    for user in userList:
        passDict[user] = generatePassword(length)
    return passDict

def printPasswords(passDict):
    formatSpec = "{0: ^8} {1:>16}: {2:<}"
    print(formatSpec.format("No. ", "---User Name---", "---Password---"))
    index = 0
    for user_pass in passDict:
        index += 1
        print(formatSpec.format(index, user_pass, passDict[user_pass]))

if __name__ == "__main__":
    test_names = ["ZhangSan", "LiSi", "WangWu", "ZhaoLiu"]
    test_length = 8
    printPasswords(userPasswords(test_names, test_length))
    