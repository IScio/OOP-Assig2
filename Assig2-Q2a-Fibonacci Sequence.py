#OOP Assignment 2

'''a) Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34 (5 marks)
'''
num=0          # This will be our counter in the loop
num_p1=1       # This will be smaller of the last 2 number
num_p2=0       # This will be larger of the last 2 number
mbuffer=0       # This will be a buffer to exchange numbers 

while num_p1+num_p2 < 50:          # run loop as long as the sum of the numbers is less than 50
  print(num_p1+num_p2,end = ' ')   # Output the sum of the last two numbers
  
  mbuffer=num_p1+num_p2      # Use buffer to move store the sum,      
  num_p1=num_p2              # then shift the numbers p1 and p2
  num_p2=mbuffer
  
  num +=1                    # Use our counter num to move one step in the loop
  
print('\n')                # Just print a blank line at the end
