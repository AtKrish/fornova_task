import requests
from bs4 import BeautifulSoup

url = "https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-22&checkOut=2024-01-23&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and extract the required fields
    room_names = [item.text for item in soup.select(".property-card-title")]
    rate_names = [item.text for item in soup.select(".property-card-rate-name")]
    guest_counts = [item.text for item in soup.select(".property-card-max-guests")]
    cancellation_policies = [item.text for item in soup.select(".property-card-cancellation-policy")]
    prices = [item.text for item in soup.select(".property-card-price")]
    top_deals = [bool(item.select_one(".property-card-top-deal")) for item in soup.select(".property-card")]
    currencies = [item.text for item in soup.select(".property-card-currency")]

    # Print or further process the extracted data
    for i in range(len(room_names)):
        print("Room Name:", room_names[i])
        print("Rate Name:", rate_names[i])
        print("Number of Guests:", guest_counts[i])
        print("Cancellation Policy:", cancellation_policies[i])
        print("Price:", prices[i])
        print("Is Top Deal:", top_deals[i])
        print("Currency:", currencies[i])
        print("----------------------")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)

    '''Make sure you have the requests and beautifulsoup4 libraries installed in
      your Python environment (pip install requests beautifulsoup4) before running this code.
        The code sends a GET request to the provided URL, extracts the required fields 
        using BeautifulSoup, and prints them out for demonstration purposes.
Please note that website scraping may be subject to legal and ethical considerations.
 Make sure to review the website's terms of service and consult with legal advisors before scraping any website.'''