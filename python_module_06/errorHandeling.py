import csv

def read_csv(path):
    rows = []
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    except FileNotFoundError:
        print(f"The file -{path}- was not found in the durrent dirrectory")
    except:
        print("Something else is wrong")
    
    return rows

value = read_csv('feil')

if len(value) > 0:
    print(value)
else:
    print("the file was empty")