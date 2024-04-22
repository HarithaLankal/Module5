def main():
    # Ask for the number of years
    num_years = int(input("Enter number of years: "))
    
    total_rainfall = 0
    total_months = num_years * 12

    # Outer loop: iterating over the years
    for year in range(1, num_years + 1):
        # Inner loop: iterate and input rainfall for all months
        for month in range(1, 13):
            rainfall = int(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
            total_rainfall += rainfall

    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months

    # Display results
    print("")
    print("Number of months:", total_months)
    print("Total inches of rainfall:", total_rainfall)
    print(f"Average rainfall per month: {average_rainfall:.2f}")

if __name__ == "__main__":
    main()