import requests
from bs4 import BeautifulSoup
import hashlib
from sha256_custom import sha256

# The URL for Book of Mark
URL = "https://quod.lib.umich.edu/cgi/r/rsv/rsv-idx?type=DIV1&byte=4697892"

# Download the page
print("Downloading text from website...")
html = requests.get(URL).text

# Extract readable text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(separator=" ", strip=True)

# Convert to bytes
data = text.encode("utf-8")

# Use your own SHA-256
print("Computing custom SHA-256...")
custom_hash = sha256(data)
print("Custom hash:", custom_hash)

# Check with Python hashlib
print("Verifying with hashlib...")
library_hash = hashlib.sha256(data).hexdigest()
print("Library hash:", library_hash)

# Save to file
with open("mark_sha256.txt", "w", encoding="utf-8") as f:
    f.write("Custom SHA-256: " + custom_hash + "\n")
    f.write("hashlib SHA-256: " + library_hash + "\n")

print("Hashes saved in mark_sha256.txt")
