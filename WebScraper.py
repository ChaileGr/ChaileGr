import requests
from bs4 import BeautifulSoup

def web_scrape():
    # Get the URL input from the user
    url = input("Enter the URL Here: ")

    try:
        # Send a request to retrieve website information
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')#Go through website and pick through user requests

            # Extract and print the title of the webpage
            title = soup.title.text.strip()
            print(f"Title: {title}\n") #Advanced string used to insert "Title" into variable response 

            # Find all links within the webpage then for the identified hyperlinks that meet the criteria print all
            links = soup.find_all('a', href=True)

            print("Links:")
            for link in links:
                print(link['href'])

            paragraphs = soup.find_all('p')
            print("Paragraphs:")
            for paragraph in paragraphs: 
                print(paragraph.text.strip())
            
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)#prints out an error code that communicates why the site couldn't be scraped 

    except requests.RequestException as e:
        print("Error during the request:", e)

# Call the function to start web scraping
web_scrape()

