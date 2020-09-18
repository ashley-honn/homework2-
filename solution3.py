# Solutions

# This is for Solution 3

## print sum and average of numbers 

number1 = 1000
number2 = 2000
number3 = 4000

sum = 0
list = [1000, 2000, 4000]
for num in list:
    sum = sum +num
average  = sum / len(list)


# this will print the three numbers
print('The users first number is:' , number1)
print("The users first number is:" , number2)
print("The users first number is:" , number3)

#printing a space inbetween input values and output
print("\n")

# this will print the sume
print ('The sum is:', f"{sum:,}" )

# this will print the average
print('The average is:' , f"{round(average, 2):,}")

