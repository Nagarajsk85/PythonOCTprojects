# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the base URL and parameters for the hotel search
base_url = "https://www.booking.com/searchresults.html"
params = {
    "ss": "Bangalore",  # Search string for Bangalore
    "checkin": "2024-04-08",  # Check-in date
    "checkout": "2024-04-09",  # Check-out date
    "group_adults": "1",  # Number of adults
    "no_rooms": "1",  # Number of rooms
    "group_children": "0",  # Number of children
    "selected_currency": "INR",  # Selected currency
    "offset": 0  # Start with the first page
}

# Define the user-agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# Initialize an empty list to store hotel details
hotel_results = []

# Loop through 5 pages of hotel listings (you can adjust this number)
for page in range(5):
    # Update the offset parameter for pagination
    params["offset"] = page * 25  # Each page displays 25 results
    
    # Send a GET request to the URL with the updated parameters and headers
    response = requests.get(base_url, params=params, headers=headers)
    
    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract hotel details from each property card on the page
    for hotels in soup.find_all("div", {"data-testid": "property-card"}):
        # Extract and format rating and reviews
        rating_text = hotels.find("div", {"data-testid": "review-score"}).text
        rating, *reviews = rating_text.split()
        reviews = ' '.join(reviews)
        
        # Create a dictionary to store the extracted hotel details
        item = {
            "Name": hotels.find("div", {"data-testid": "title"}).text,  # Hotel name
            "Location": hotels.find("span", {"data-testid": "address"}).text,  # Hotel location
            "Pricing": hotels.find("span", {"data-testid": "price-and-discounted-price"}).text,  # Hotel pricing
            "Rating": rating,  # Hotel rating
            "Reviews": reviews  # Hotel reviews
        }
        
        # Append the dictionary to the hotel_results list
        hotel_results.append(item)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(hotel_results)

# Save the DataFrame to an Excel file
df.to_excel("hotel_results.xlsx", index=False)

# Print a message to indicate that the data has been saved to the Excel file
print("Data saved to hotel_results.xlsx")
