'''
Create a script called HandleExceptions.py. 
In the script, create a section of code that requests sales numbers from a user. 
The user should be able to enter as many sales values as they choose to. 
All sales values should always be entered as float values. 
Each value entered should be added to a list of sales values.

Provide a means for the user to stop entering sales values. 
Once all the sales values have been entered, 
the user wants to calculate the total of the sales figures. 

Still, the user should be allowed to specify how many sales figures should be added to the total, 
i.e. if the user requests that five sales figures be added to the total, 
the program should sum the first five values in the list. 

There are multiple places in this program where errors may occur. 
Ensure that any exceptions that occur are handled.
'''

sales = []
def enterSales():
    #Enter infinite loop
    while True:   
        # Test for input error
        try:
            valueEntered = float(input("Enter your sales numbers: (or press 0 to exit the script)  "))
            if valueEntered == 0:
                break
            sales.append(valueEntered)
        except:
            print("An input error occurred, try again\n")

def calculateSales():
        # Test for input error
        try:
            numberOfSales = int(input("Enter the number of sales you vant to calculate the total for  "))
            
            if numberOfSales < 1:
                raise ValueError("Cannot calculete for less than 1 sale")   
            elif numberOfSales > len(sales):
                raise ValueError("Number entered is higher than the number of sales")    
            else:
                print("Toatal income from your sales:", sum(sales[:numberOfSales]))
        
        except ValueError as msg:
            print("Input error", msg)
        except:
            print("An input error occurred, try again\n")

while True:
    # Selection menu
    print()
    print("1\tEnter sales")
    print("2\tCalculate totas from sales")
    print()

    try:
        selection = int(input("please select an option: (or enter 9 to quit the program) "))

        if selection == 9:
            break
                
        if selection < 1 or selection > 2:
            raise ValueError()

        if selection == 1:
            enterSales()

        else:
            calculateSales()   
    except:
        print("input error. Try again:\n")

print("\nProgram ended")