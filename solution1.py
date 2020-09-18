# solutions

##This is for Solution 1

#Titles for cells
cell_1 = 'Number'
cell_2 = 'Square'
cell_3 = 'Cube'
space = '20'
align = ' '


#This will print titles for all cells
print(f'{cell_1 :{align}>{space}}',f'{cell_2 :{align}>{space}}',f'{cell_3 :{align}>{space}}')
num = 0


#This will print number, squared, and cubed from range 0 to 6 
for num in range (0, 6):
    print(f'{num :{space}}',f'{num*num :{space}}',f'{num*num*num :{space}}')
 