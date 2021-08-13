def collatz(number):
    counter = 0
    while number != 1: #if the number doesn't equal one the function executes
        counter = counter + 1
        if number <= 0:
            print("You must enter a positive integer!")
            break
        elif number %2 == 0: #check for even number
            newnumber = number // 2
            print(newnumber)
            number = newnumber #the while function will now check the new number    
        else: #if the number ain't even it's odd
            newnumber = 3 * number + 1
            print(newnumber)
            number = newnumber #the while function will now check the new number
    print("\nIt took " + str(counter) + " iterations to get to 1")
try:
    number = int(input("Enter a positive number: "))
    print("The number you chose is: " + str(number))
    collatz(number)

except ValueError:
    print("You did not enter an integer!")





    

        
        
        
