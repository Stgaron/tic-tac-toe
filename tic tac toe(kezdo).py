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
    for row in range(table):
        line = ""
        for col in range(table):
            line += "   "
            if col < table - 1:
                line += "|"
        print(line)
        if row < table - 1:
            print("-" * (table * 4 - 1))
    
boardprint(table)
    
    
    

