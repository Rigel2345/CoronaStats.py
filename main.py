from bs4 import BeautifulSoup as bs
from requests import get

url = 'https://www.nytimes.com/interactive/2021/us/alabama-covid-cases.html'
response = get(url)

soup = bs(response.text, 'html.parser')

parent_data = []
child_data = []
table = soup.find('table', attrs={'class':'g-table super-table withchildren'})

parent_body = table.find('tbody', class_='parent super')
child_body = table.find('tbody', class_='children')

parent_rows = parent_body.find_all('tr')
child_rows = child_body.find_all('tr')

with open("test.txt", "w") as f:
    f.write(str(child_rows[0]))
'''
for row in parent_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    parent_data.append([ele for ele in cols if ele]) # Get rid of empty values

    print(cols)

for row in parent_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    child_data.append([ele for ele in cols if ele]) 
'''
    
