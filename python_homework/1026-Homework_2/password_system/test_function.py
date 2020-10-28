import read_names, generate_password, password_file, check_password

"""
test all the functions in this module
"""

def test_function():
    """
    test all the functions in this module
    """
    print("\n---Welcome to the password system---\n")
    print("\n---1. Read names from files or keyboard---\n")
    userList = read_names.readUserName()
    print("Users: ", *userList)

    print("\n---2. Generate password for all users---\n")
    passLength = generate_password.setPassLength()
    passDict = generate_password.userPasswords(userList, passLength)
    generate_password.printPasswords(passDict)

    print("\n---3. Save password (md5) to csv file---\n")
    password_file.savePassword(passDict)
    print("Save Successfully!\n")

    print("\n---4. User Login Test---\n")
    md5Dict = password_file.readPassword()
    check_password.mockLogin(md5Dict)

    print("\nALL DONE! \n")

