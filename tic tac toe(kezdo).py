print("Hello welcome to my tic tac toe game")
def boardmaker():
    try:
        table= int(input("How big should the table be(give one number):"))
        return table
    except ValueError:
        print("Please only put in numbers")
        return boardmaker()
table = boardmaker()

def boardprint(table):
    for i in range(table):
        print("--------"*table)
        print("|      |"*table)
    print("--------"*table)
boardprint(table)

def gamestart(table):
    print("1. player is up next and he will be with the X")
    X1=int(input("Which row do you want to put your X (only 1 number)"))
    Y1=int(input("Which collumn do you want to put your X(only 1 number)"))
    
    

