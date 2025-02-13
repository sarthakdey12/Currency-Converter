# Currency-Converter
The Currency Converter is a Python-based program that allows users to convert an amount from one currency to another using real-time exchange rates. The program fetches the exchange rate data from an external API and performs the conversion by multiplying the entered amount by the exchange rate. This provides the user with the equivalent amount in the target currency.

Features:
- Real-time Exchange Rates:
The converter fetches the latest exchange rates from an external API, ensuring that the rates are up-to-date.

- Supports Multiple Currencies:
You can convert between various currencies (e.g., USD to EUR, INR to GBP). The program supports any currency available from the API provider.

User Input:
- The user inputs:
   The amount they want to convert.
   The base currency (the currency they are converting from).
   The target currency (the currency they are converting to).

Accurate Conversion:
- The program multiplies the entered amount by the current exchange rate and displays the result in the target currency.

How It Works:
- API Call:
  The program uses a free currency exchange API (such as ExchangeRate-API) to get real-time exchange rates for various currencies.
  The user selects a base currency (e.g., USD) and a target currency (e.g., EUR), and the program fetches the exchange rate for that pair.

- Input from the User:
The user provides an amount to be converted, and the program retrieves the exchange rate for the specified currencies.

- Calculation:
The program performs the conversion by multiplying the entered amount by the retrieved exchange rate:
Converted Amount = Amount * Exchange Rate

- Output:
The program outputs the converted amount in the target currency.

Technologies Used:

Python: The program is written in Python, making it easy to understand and modify for beginners.
API: The program uses an external API (like ExchangeRate-API) to fetch real-time exchange rate data.
Requests Library: The requests library is used to make HTTP requests to the API and fetch the exchange rate data.

Code Overview:
Fetching Exchange Rate: The program makes an API call to retrieve the exchange rates. This is done using the requests.get() function. The base currency and target currency are used to extract the relevant exchange rate from the API response.

User Interface: The user is prompted to input:

Amount: The number of units to convert (e.g., 100 USD).
Base Currency: The currency they are converting from (e.g., USD).
Target Currency: The currency they are converting to (e.g., EUR).
Conversion Calculation: The program multiplies the entered amount by the exchange rate to calculate the converted amount.

Display Result: The final converted amount is displayed in the target currency, along with the original amount and base currency.

