import requests

# Function to get exchange rate
def get_exchange_rate(base_currency, target_currency):
    # Your API key (replace with the one you got)
    api_key = '831c6cbe32f1dab8d8d37bd0'
    
    # URL for the ExchangeRate API
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    # Make an API call
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # If the target currency exists in the response, return the exchange rate
        if target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            return "Currency not supported."
    else:
        return "Failed to get data from the API."

# Function to convert amount
def convert_currency(amount, base_currency, target_currency):
    # Get the exchange rate
    rate = get_exchange_rate(base_currency, target_currency)
    
    if isinstance(rate, float):
        # Calculate the converted amount
        converted_amount = amount * rate
        return converted_amount
    else:
        return rate

# Main program
def main():
    print("Currency Converter")
    # Get user input for amount and currencies
    amount = float(input("Enter the amount you want to convert: "))
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    # Convert the currency
    result = convert_currency(amount, base_currency, target_currency)
    
    if isinstance(result, float):
        print(f"{amount} {base_currency} is equal to {result:.2f} {target_currency}")
    else:
        print(result)

if __name__ == "__main__":
    main()
