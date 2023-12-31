import requests
from bs4 import BeautifulSoup

url = "https://nordvpn.com/blog/nordvpn-introduces-a-warrant-canary/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the lines containing the required information
    target_lines = []
    for paragraph in soup.find_all('p'):
        if "As of" in paragraph.get_text():
            target_lines.append(paragraph.get_text())
            break

    for paragraph in soup.find_all('li'):        
        if "National Security letters;" in paragraph.get_text():
            target_lines.append(paragraph.get_text())

        if "gag orders;" in paragraph.get_text():
            target_lines.append(paragraph.get_text())

        if "warrants from any government organization." in paragraph.get_text():
            target_lines.append(paragraph.get_text())
            break

#    for paragraph in soup.find_all('ul'):
#        if ";" in paragraph.get_text():
#            target_lines.append(paragraph.get_text())

    # Print the extracted lines
    for line in target_lines:
        print(line)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

