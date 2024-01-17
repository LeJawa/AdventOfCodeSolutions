if __name__ == "__main__":
    from src.common.create_day import create_day
    from src.common.run import run_year
    from src.common.run import run_all_years
    
    print("What do you want to do?")
    while(True):
        answer = input("1. Create a new day\n2. Run a specific year\n3. Run all years\n4. Exit\n")
        if answer == "1":
            year, day = input("Enter year and day: ").split()
            create_day(year, day)
        elif answer == "2":
            year = input("Which year do you want to run? ")
            run_year(year)
        elif answer == "3":
            run_all_years()
        elif answer == "4":
            break
        else:
            print("Invalid input, try again.")
        print("What do you want to do?")
        

    
    

