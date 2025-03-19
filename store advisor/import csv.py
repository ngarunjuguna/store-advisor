import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to collect sales data
def collect_sales_data():
    print("Enter the sales data: ")

    # Collect sale details
    date_str = input("Enter the date of sale (YYYY-MM-DD): ")
    item_name = input("Enter the item sold: ")
    sale_amount = float(input("Enter the sale amount: "))

    # Ensure the date format is correct
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Write data to CSV
    with open('sales_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, item_name, sale_amount])

    print(f"Sale recorded: {item_name} sold for ${sale_amount} on {date_str}")

# Function to display the sales graph
def display_sales_graph():
    try:
        # Load sales data from CSV file
        df = pd.read_csv('sales_data.csv', names=["Date", "Item", "SaleAmount"])

        # Convert the 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Group the data by date and calculate the total sales for each day
        daily_sales = df.groupby('Date')['SaleAmount'].sum()

        # Plot the graph
        plt.figure(figsize=(10, 6))
        plt.plot(daily_sales.index, daily_sales.values, marker='o', color='b', label='Total Sales')
        plt.title('Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales ($)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("No sales data found. Please add sales data first.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to display the sales report
def display_sales_report():
    try:
        # Load sales data from CSV file
        df = pd.read_csv('sales_data.csv', names=["Date", "Item", "SaleAmount"])

        # Group the data by item and calculate the total sales for each item
        item_sales = df.groupby('Item')['SaleAmount'].sum()

        # Print the sales report
        print("\nSales Report by Item:")
        for item, sales in item_sales.items():
            print(f"{item}: ${sales:.2f}")

    except FileNotFoundError:
        print("No sales data found. Please add sales data first.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to control the flow of the program
def main():
    while True:
        print("\nSales Data Management")
        print("1. Add a new sale")
        print("2. Display Sales Graph")
        print("3. Display Sales Report by Item")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            collect_sales_data()
        elif choice == '2':
            display_sales_graph()
        elif choice == '3':
            display_sales_report()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
