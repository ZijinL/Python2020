import sys


def EnterNumber()->int:
    """
    enter a number
    return a valid number
    """
    temp = input("enter a number: ")
    flag = 0;
    while flag == 0:
        try:
            number = int(temp)
        except:
            print("illeagal input")
            temp = input("pls enter again: ")
        else:
            flag = 1
    return number  

def Elevator(minfloor, maxfloor)->int:
    """
    enter the floor you want to go 
    return the actual floor you will go
    enter 0 to exit this program
    """
    print("Welcome to Zijin's elevator, pls enter the floor you want to go!\n (enter '0' to exit)")
    floor_des = EnterNumber()
    while floor_des != 0:
        if floor_des > maxfloor:
            print("the floor is too high")
        elif floor_des < minfloor:
            print("the floor is too low")
        elif floor_des < 14:
            print("actual floor: ", floor_des)
        elif floor_des in [14, 18]:
            print("floor not exists")
        elif floor_des < 18:
            print("actual floor: ", floor_des - 1)
        else:
            print("actual floor: ", floor_des - 2)
        floor_des = EnterNumber()
        
def initElevator():
    print("Pls enter the minfloor (smaller than 14)")
    flag = 0;  # 设立循环标志位
    while flag == 0:
        minfloor = EnterNumber()
        if minfloor < 14:
            flag = 1
    print("Pls enter the maxfloor (larger than 18)")
    flag = 0;  # 设立循环标志位
    while flag == 0:
        maxfloor = EnterNumber()
        if maxfloor > 18:
            flag = 1
    return minfloor, maxfloor

def main():
    minfloor, maxfloor = initElevator()
    Elevator(minfloor, maxfloor)

if __name__ == "__main__":
    sys.exit(main())