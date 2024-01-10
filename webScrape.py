import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the Qantas website
url = 'https://www.qantas.com/hotels/properties/18482?adults=24&checkIn=2023-10-30&checkOut=2023-10-31&children=0&infants=0&location=London%2C%20England%20%20United%20Kingdom&page=1&payWith=cash&searchType=Hat&sortBy=popularity'
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant data from the HTML
hotel_ids = [hotel['data-hotel-id'] for hotel in soup.select('.hotel-card')]
check_in_dates = ['2023-10-30'] * len(hotel_ids)
check_out_dates = ['2023-10-31'] * len(hotel_ids)

# Write the data to a CSV file
with open('hotel_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Hotel ID', 'Check-in Date', 'Check-out Date'])
    writer.writerows(zip(hotel_ids, check_in_dates, check_out_dates))