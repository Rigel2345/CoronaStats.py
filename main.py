from bs4 import BeautifulSoup as bs
from requests import get

# get url from internet
url = 'https://www.nytimes.com/interactive/2021/us/alabama-covid-cases.html'
response = get(url)

# parse the webpage
soup = bs(response.text, 'html.parser')

dictList = []

table = soup.find('table', attrs={'class':'g-table super-table withchildren'})

parent_body = table.find('tbody', class_='parent super')
child_body = table.find('tbody', class_='children')

parent_rows = parent_body.find_all('tr')
child_rows = child_body.find_all('tr')

for row in parent_rows:
    # get all the elements
    county_name = row.find('td', class_='name').text
    cases_daily_avg = row.find('td', class_='bignum cases show-mobile').text
    cases_per_100k = row.find('td', class_='num cases show-mobile').text
    change_14_days = row.find('td', class_='chart cases wider td-end show-mobile').text
    
    # replace all unicode formatting
    county_name = county_name.replace('Ala.', '')
    cases_daily_avg = cases_daily_avg.replace(',', '')
    cases_daily_avg = cases_daily_avg.replace('\n\t', '')
    change_14_days = change_14_days.replace('\n\n', '')
    change_14_days = change_14_days.replace('–', '-')

    # create dictionary with all values and append to a list
    dictList.append(dict(name = county_name, daily_case_avg = int(cases_daily_avg), cases_100k = int(cases_per_100k), change_per_14=change_14_days))

for row in child_rows:
    # same as the parent class, but with each individual county
    county_name = row.find('td', class_='name').find('a').text
    cases_daily_avg = row.find('td', class_='bignum cases show-mobile').text
    cases_per_100k = row.find('td', class_='num cases show-mobile').text
    change_14_days = row.find('td', class_='chart cases wider td-end show-mobile').text
    
    county_name = county_name.replace('\xa0›', '')
    cases_daily_avg = cases_daily_avg.replace('\n\t', '')
    change_14_days = change_14_days.replace('\n\n', '')
    change_14_days = change_14_days.replace('–', '-')

    dictList.append(dict(name = county_name, daily_case_avg = int(cases_daily_avg), cases_100k = int(cases_per_100k), change_per_14=change_14_days))

# writing dictionaries to a .csv to transport data to streamlit app
with open('counties.csv', 'w') as f:
    for i in dictList:
        print(i)
        for j, v in i.items():
           f.write(j + ", " + str(v))
           f.write('\n')

    f.write("name, Madison\n")
    f.write("daily_case_average, 195\n")
    f.write("cases_100k, 52\n")
    f.write("change per 14, -19%\n")

    f.write("name, Jackson\n")
    f.write("daily_case_average, 39\n")
    f.write("cases_100k, 75\n")
    f.write("change per 14, -1%\n")

    f.write("name, Limestone\n")
    f.write("daily_case_average, 64\n")
    f.write("cases_100k, 64\n")
    f.write("change per 14, -16%")
