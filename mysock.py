from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (not recommended for production)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input URL
url = input('Enter - ')

try:
    # Fetch and read HTML content
    html = urlopen(url, context=ctx).read()
except Exception as e:
    print(f"Error fetching URL: {e}")
    exit()

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Retrieve all <span> tags
tags = soup('span')
resultsum = 0

for tag in tags:
    try:
        # Extract and convert content to integer
        number = tag.get_text(strip=True)
        number = int(number)
        resultsum += number
    except ValueError:
        # Skip non-numeric content
        print(f"Skipping non-numeric content: {tag.get_text(strip=True)}")
    except Exception as e:
        # Handle unexpected errors
        print(f"Error processing tag: {e}")

# Print the result
print(resultsum)

