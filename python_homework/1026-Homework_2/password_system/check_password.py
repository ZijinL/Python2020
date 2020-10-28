from hashlib import md5
import password_file

"""
simulate login process and check the validity of the password
generate a Token if you enter the right username and password
"""

def mockLogin(md5Dict):
    """
    simulate the process of user login
    you must give 
    """
    # maximum times to try your password
    for counts in range(3):
        name = input("pls enter the username(input 'exit' to terminate): ")
        if name == "exit":
            return False
        password = input("pls input the password: ")
        if checkPassword(name, password, md5Dict):
            Token = genToken(name)
            return Token
        else:
            print("invalid username and password")
        counts += 0 # avoid 'counts not used' error alert
    print("the time you try exceed the max value 3")
    return False

def genToken(username="null", expire=60):
    """
    will be updated in future version
    (to be updated)
    """
    token = "LoginSuccesfully"
    return token

def checkPassword(name, password, md5Dict):
    """
    for the safety of your password
    we only check the MD5 checksum
    """
    if name not in md5Dict.keys():
        return False
    elif md5(password.encode(encoding='UTF-8')).hexdigest() != md5Dict[name]:
        return False
    else:
        return True

if __name__ == "__main__":
    md5Dict = password_file.readPassword()
    outcome = mockLogin(md5Dict)
    if outcome:
        print("Login Successfully! Your token is ", outcome)
    else:
        print("Invalid login infomation, see you next time!")
