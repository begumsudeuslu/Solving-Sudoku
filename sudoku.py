import sys
#First step: Read input and put lines in lists.
def read_file(file_name):
    with open(file_name) as file: 
        all_list = file.read()   
#In line 4, all the numbers in the lines in order are put into the same list.
    all_list = [int(i) for i in all_list if i.isdigit()] 
    sudoku_list=[]
#We start first item to final item and small list of nine are created, then every nine items add to lists
    for i in range(0, len(all_list), 9):
        x = i
        sudoku_list.append(all_list[x:x+9])
    return sudoku_list

#Second step: We try to bring together the numbers in the row, column, 3x3 areas and find out which numbers are here. 
"""We add the numberes in row, column, 3x3 areas. """
def exist_valid(row, col, sudoku_list):
    exist_number = []
    #Check the row and add all number which in the row.
    for i in range(0, 9):
        exist_number.append(sudoku_list[row][i])    
    
    #Check the column and add all number which in the column.     
    for i in range(0, 9):
        exist_number.append(sudoku_list[i][col])
   
    #Check the 3x3 areas and add all number which in the 3x3 areas.
    x_axis = (col // 3) * 3
    y_axis = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            exist_number.append(sudoku_list[y_axis + i][x_axis + j])
    
    #Finally exist_valid function return exist_number as a set. We turn to set because if we have same number in list, this function cannot run. If I use as set, automatically same numbers cancel execpt one.
    return set(exist_number)

#Third an the most important step. In this step, we will solve sudoku one by one empty cell.
"""We take one input with sys in main function. This input will be my variable as list and these codes will change this list.
These codes run and load the number which have just one possibility until sudoku has no empty cell anymore.
While sudoku be changed, this function add last sudoku which modified to empty list as move and we add this lis and we  take from this list. """
def find_zero(input,moves=[],step=1):   
    #We call read_file function to get input list, because read_file fnction return as set. 
    sudoku_list=input
    
    #These are the numbers we need to enter when filling the sudoku.
    all_number ={1,2,3,4,5,6,7,8,9}
    
    #This loop run until sudoku list has no empty cell.
    while True:
        for row in range(0,9):        #We look row.
            for col in range(0,9):      #We look col.
                
                #Here we checked whether there are empty cells in this row and column. If this cell is empty, continue.
                if sudoku_list[row][col]==0:
                    
                    #From all numbers, we substract the list and zeros.
                    possible_number=list(all_number-exist_valid(row,col,sudoku_list)-{0})
                    
                    #Since the numbers we found are probabilities, if there is a single number in the list, it is written instead.
                    if len(possible_number)==1:
                        sudoku_list[row][col]=possible_number[0]    #number is written instead of zero.
                        
                        #We add all the result which is returned by show_change.
                        moves.append(show_change(row+1,col+1,possible_number[0],step,sudoku_list))  
                        find_zero(sudoku_list,moves,step+1)   #this is recursive function. this way we start to begin. We add step again until stop.                        
            
        return moves
        
        
#Fourth step: Actually this function in the find_zero. This function show us where and at what step we changes.
def show_change(row,col,num,i,sudoku):
    step= '-'*18 + '\n'
    step+= f"Step {i} - {num} @ R{row}C{col}" + '\n'
    step+= '-'*18 + '\n'
    sudoku_str=[[str(num) for num in row] for row in sudoku]
    for row in sudoku_str:
        step+=' '.join(row) + '\n'       #we add space all the number between. But if we want that we have to turn number to str from int, because space is str.
    return step
        
#Final step: We write all lis as txt file.   
def write_output(file_name, input):
    with open(file_name, 'w') as f:
        moves=find_zero(input)    
        for move in moves:       #All the line be written with for loop.
            f.write(move)
        f.write('-'*18)   #At the final we have to write 18 times - again.
            
    
#And we run all function in main.   
def main():
    input_file= (sys.argv[1])     #Input from user.
    output_file= (sys.argv[2])      #Output txt from user.
    sudoku_list=read_file(input_file)    #We turn input file to text.
    write_output(output_file,sudoku_list)   #And write as text.       
if __name__ == '__main__':
    main()