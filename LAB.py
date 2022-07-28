import pandas as pd
SYSTEM = []
class Car:
  def __init__(self, car_id, model, year, km_travelled, price):
    # assign the parameter's values to the attributes of the class
        self.car_id = car_id  # ID 
        self.model = model  # Model 
        self.year = year  # Year of Production
        self.km_travelled = km_travelled  # distance travelled
        self.price = price  # price of the car
    def print_menu():
    
    print("1. ADD NEW CARS TO THE SYSTEM")
    print("2. FIND A CAR BASED ON ITS ID")
    print("3. UPDATE THE INFORMATION OF A SPECIFIC CAR")
    print("4. DELETE A CAR FROM THE SYSTEM")
    print("5. WRITE TO CSV FILE")
    print("6. EXIT THE PROGRAM")
    number = input("CHOOSE AN OPTION (1-6): ")

    return number
    def add_car():
  
    car_id = input("ENTER CAR'S ID: ")
    model = input("ENTER CAR'S MODEL: ")
    year = int(input("ENTER CAR'S YEAR OF PRODUCTION: "))
    travelled = float(input("ENTER DISTANCE TRAVELLED (IN KM): "))
    price = float(input("ENTER CAR'S PRICE (IN DOLLARS): "))

    new_car = Car(car_id, model, year, travelled, price)
    found = False
    for car in SYSTEM:
        if car.car_id == car_id:
            found = True
            break

    if found:
        print(f"CAR ID ({car_id}) ALREADY EXISTS IN THE SYSTEM !!!")
    else:
        SYSTEM.append(new_car)
    def find_car_by_id():
    
    car_id = input("ENTER CAR'S ID: ")
    found = False

    for car in SYSTEM:
        if car.car_id == car_id:
            found = True
            print("CAR FOUND:")
            print("%-14s%s" % ("ID:", car.car_id))
            print("%-14s%s" % ("MODEL:", car.model))
            print("%-14s%d" % ("YEAR:", car.year))
            print("%-14s%.2f KM" % ("KM TRAVELLED:", car.km_travelled))
            print("%-14s$%.2f" % ("PRICE:", car.price))

            break
    if not found:
        print(f"CAR ID ({car_id}) DOES NOT EXISTS IN THE SYSTEM !!!")
def update_car():

    car_id = input("ENTER CAR'S ID: ")
    print("WHAT DO YOU WANT TO UPDATE?")
    print("1. MODEL NAME")
    print("2. PRODUCTION YEAR")
    print("3. DISTANCE TRAVELLED")
    print("4. PRICE")
    ch = input("CHOOSE AN OPTION (1-4): ")

    found = False
    index = 0
    for i, car in enumerate(SYSTEM):
        if car.car_id == car_id:
            index = i
            found = True
            break

    if not found:
        print(f"CAR ID ({car_id}) DOES NOT EXISTS IN THE SYSTEM !!!")
        return

    if ch == "1":
        model = input("ENTER NEW MODEL NAME: ")
        SYSTEM[index].model = model

    elif ch == "2":
        year = int(input("ENTER NEW YEAR: "))
        SYSTEM[index].year = year

    elif ch == "3":
        travelled = float(input("ENTER NEW DISTANCE TRAVELLED (IN KM): "))
        SYSTEM[index].km_travelled = travelled

    elif ch == "4":
        price = float(input("ENTER NEW PRICE (IN DOLLARS): "))
        SYSTEM[index].price = price

    else:
        print("INVALID OPTION !!!")
   def delete_car():

    car_id = input("ENTER CAR'S ID TO DELETE: ")

    found = False
    for car in SYSTEM:
        if car.car_id == car_id:
            found = True
            SYSTEM.remove(car)
            print("The car is delete from the system")
            break

    if not found:
        print(f"CAR ID ({car_id}) DOES NOT EXISTS IN THE SYSTEM !!!")
    def write_csv():
  
    dict_to_write = {
        "Car_ID": [],
        "Model": [],
        "Production_year": [],
        "Kilometers_travelled": [],
        "Price": [],
    }

    for car in SYSTEM:
        dict_to_write["Car_ID"].append(car.car_id)
        dict_to_write["Model"].append(car.model)
        dict_to_write["Production_year"].append(car.year)
        dict_to_write["Kilometers_travelled"].append(car.km_travelled)
        dict_to_write["Price"].append(car.price)

    df=pd.DataFrame(dict_to_write)
    print('DataFrame Values:\n',df)
    csv_data = df.to_csv()
    print('\nCSV String Values:\n',csv_data)
    if __name__ == "__main__":

    while True:
        ch = print_menu()
        print()

        if ch == "1":
            add_car()
        elif ch == "2":
            find_car_by_id()
        elif ch == "3":
            update_car()
        elif ch == "4":
            delete_car()
        elif ch == "5":
            write_csv()
        elif ch == "6":
            print("THANK YOU FOR USING PROGRAMING")
            break
        else:
            print("INVALID OPTION !!!")

        print()
