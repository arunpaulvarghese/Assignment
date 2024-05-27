# Function to calculate average stock price
def calculate_average_price(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)

# Function to calculate percentage change between two prices
def calculate_percentage_change(start_price, end_price):
    if start_price == 0:
        return "undefined (start price is zero)"
    return ((end_price - start_price) / start_price) * 100

# Main function to perform stock price calculations
def main():
    # Example stock prices (for simplicity)
    stock_prices = [150, 152, 148, 153, 155, 149, 151]
    
    # Calculate average stock price
    average_price = calculate_average_price(stock_prices)
    print(f"Average Stock Price: ${average_price:.2f}")
    
    # Calculate percentage change from first to last price
    start_price = stock_prices[0]
    end_price = stock_prices[-1]
    percentage_change = calculate_percentage_change(start_price, end_price)
    print(f"Percentage Change from ${start_price} to ${end_price}: {percentage_change:.2f}%")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()