# Buatlah program yang dapat mengambil daftar kabupaten di Indonesia di Wikipedia dan
# dikonversi ke sebuah file csv.
# Link daftar kabupaten di Indonesia di Wikipedia adalah sebagai berikut:
# https://id.wikipedia.org/wiki/Daftar_kabupaten_di_Indonesia

# get api from wikipedia
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_di_Indonesia"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# get table
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")

# get header
header = rows[0].find_all("th")
header = [h.text.strip() for h in header]

# get data
data = []
for row in rows[1:]:
    cols = row.find_all("td")
    cols = [c.text.strip() for c in cols]
    data.append(cols)

# create dataframe
df = pd.DataFrame(data, columns=header)
df.to_csv("kabupaten.csv", index=False)
print("File kabupaten.csv berhasil dibuat")
