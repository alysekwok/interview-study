# Write a function that prints a chessboard pattern, with "W" being white
# square and "B" being black. Input is an integer that is the number of squares
# on the board. Output is 2D char array. For example,
# Input = 2
# Output =
# W B
# B W

def checkerboard(numSquares):
    count = 0
    for col in range(numSquares):
        string = ""
        for row in range(numSquares):
            if count % 2 == 0:
                if row % 2 == 0:
                    string += "W "
                else:
                    string += "B "
            else:
                if row % 2 == 1:
                    string += "W "
                else:
                    string += "B "
        print(string)
        string = ""
        count += 1
checkerboard(5)