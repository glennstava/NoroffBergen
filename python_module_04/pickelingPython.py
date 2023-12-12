import pickle
import os

# The data we have
car_01 = {'make' : 'Volvo', 'drive' : 'petrol', 'price' : 649000}
car_02 = {'make' : 'Ford', 'drive' : 'petrol', 'price' : 349800}
car_03 = {'make' : 'Tesla', 'drive' : 'electric', 'price' : 989000}
car_04 = {'make' : 'Ferrari', 'drive' : 'petrol', 'price' : 1649200}
car_05 = {'make' : 'Audi', 'drive' : 'petrol', 'price' : 897000}
car_06 = {'make' : 'VW', 'drive' : 'electric', 'price' : 279800}
car_07 = {'make' : 'Honda', 'drive' : 'electric', 'price' : 466000}
car_08 = {'make' : 'Fiat', 'drive' : 'electric', 'price' : 158600}
car_09 = {'make' : 'porche', 'drive' : 'petrol', 'price' : 971000}
car_10 = {'make' : 'Toyota', 'drive' : 'petrol', 'price' : 345800}
cars = [car_01, car_02, car_03, car_04, car_05, car_06, car_07, car_08, car_09, car_10]

# Opening an existing file if it is there
if os.path.isfile("pickledCarList.dat"):
    print("Loading pickle")

    # Open the pickle file
    # Use pickle to read the data from the file.
    # Since it was stored as a list, it should load as a list.
    with open("pickledCarList.dat","rb") as file:
        savedPickle = pickle.load(file)
        print(savedPickle)

else:
    print("No data to load to load")  
    print("Pickeling the exixting car-datafile")

    with open("pickledCarList.dat","wb") as file:
        pickle.dump(cars, file)
        print("Process done")

'''
# Open the pickle file
savedPickle = open("pickledCarList.dat","rb")
data = pickle.load(savedPickle)
savedPickle.close()

# Printing retrieved data
print(data)
'''