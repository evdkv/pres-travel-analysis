from bs4 import BeautifulSoup
import requests
import csv

WEB_HEADER = "https://history.state.gov/"
TABLE_HEADER = ['visit_type', 'name', 'country', 'locale', 'remarks', 'date']

def main():
    travel_table = []
    for person in ['president', 'secretary']:
        travel_table.extend(parse_travel(person))

    write_table('travel_raw.csv', travel_table, TABLE_HEADER)

def parse_travel(person):
    pg_main = requests.get(WEB_HEADER + "/departmenthistory/travels/" + person)
    soup = BeautifulSoup(pg_main.content, 'html.parser')

    list_div =  soup.find_all('div', attrs = {'class' : 'col-md-8'})
    subpage_links = [elem.get('href') for elem in list_div[0].select('a')]

    table = []
    for link in subpage_links:
        table.extend(get_rows(link, person))
    return table
    

def get_rows(link, person):
    all_rows = []

    pg_sub = requests.get(WEB_HEADER + link)
    soup_sub = BeautifulSoup(pg_sub.content, 'html.parser')
    current_person = soup_sub.find("h1").text.strip()
    table = soup_sub.find('table', attrs = {'class' : 'hsg-table-default'})

    for row in table.find('tbody').find_all('tr'):
        row_entries = row.find_all('td')
        entry_list = [entry.text for entry in row_entries]
        entry_list.insert(0, current_person)
        entry_list.insert(0, person)
        all_rows.append(entry_list)
    print("Travel parsed for", current_person)
    return all_rows

def write_table(name, rows, header):
    with open('../pres-travel-analysis/data/' + name, 'w') as csv_table:
        writer = csv.writer(csv_table)
        writer.writerow(header)
        writer.writerows(rows)
    print("Done writing.")

if __name__ == '__main__':
    main()