# Create an empty dictionary
countryDB = {

}

while True:
    print("Option 1: Add \n Option 2: Remove \n Option 3: Get capital \n Option 4: Display all capitals \n Option 5: Display all countries")
    options = int(input("Please enter the number of the option you chose"))
    if options == 1:
        country = input("What country would you like to add? ").upper()
        capital = input("What should the capital of this country be? ").upper()
        countryDB[country] = capital
        print(countryDB)
    elif options == 2:
        