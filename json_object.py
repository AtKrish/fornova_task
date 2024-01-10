import requests
from bs4 import BeautifulSoup
import json

# Send a GET request to the Qantas website
url = 'https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-22&checkOut=2024-01-23&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity'
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the rate elements on the page
rates = soup.select('.hotel-card')

# Extract the required information for each rate
rate_list = []
for rate in rates:
    room_name = rate.select_one('.room-type').text.strip()
    rate_name = rate.select_one('.rate-name').text.strip()
    guests = rate.select_one('.guests').text.strip()
    cancellation_policy = rate.select_one('.cancellation-policy').text.strip()
    price = rate.select_one('.price').text.strip()
    top_deal = 'Top Deal' in rate.select_one('.rate-flags').text.strip()
    currency = rate.select_one('.currency').text.strip()

    # Create a JSON object for each rate and add it to the list
    rate_data = {
        'room_name': room_name,
        'rate_name': rate_name,
        'guests': guests,
        'cancellation_policy': cancellation_policy,
        'price': price,
        'top_deal': top_deal,
        'currency': currency
    }
    rate_list.append(rate_data)

# Print the extracted rates
print(json.dumps(rate_list, indent=4))