import database

def display_menu():
    print("Crop and Soil Management System")
    print("1. Add Crop")
    print("2. Add Soil Data")
    print("3. View Crops")
    print("4. View Soil Data for a Crop")
    print("5. Exit")

def add_crop():
    name = input("Enter crop name: ")
    planting_date = input("Enter planting date (YYYY-MM-DD): ")
    harvest_date = input("Enter harvest date (YYYY-MM-DD): ")
    database.insert_crop(name, planting_date, harvest_date)
    print("Crop added successfully.")

def add_soil():
    crop_id = int(input("Enter crop ID: "))
    pH = float(input("Enter soil pH: "))
    nitrogen = float(input("Enter nitrogen content (kg/ha): "))
    phosphorus = float(input("Enter phosphorus content (kg/ha): "))
    potassium = float(input("Enter potassium content (kg/ha): "))
    database.insert_soil(crop_id, pH, nitrogen, phosphorus, potassium)
    print("Soil data added successfully.")

def view_crops():
    crops = database.get_crops()
    for crop in crops:
        print(f"ID: {crop[0]}, Name: {crop[1]}, Planting Date: {crop[2]}, Harvest Date: {crop[3]}")

def view_soil_data():
    crop_id = int(input("Enter crop ID: "))
    soil_data = database.get_soil_for_crop(crop_id)
    if not soil_data:
        print("No soil data found for this crop.")
        return
    for data in soil_data:
        print(f"ID: {data[0]}, pH: {data[2]}, Nitrogen: {data[3]}, Phosphorus: {data[4]}, Potassium: {data[5]}")

def main():
    database.create_tables()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_crop()
        elif choice == '2':
            add_soil()
        elif choice == '3':
            view_crops()
        elif choice == '4':
            view_soil_data()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
