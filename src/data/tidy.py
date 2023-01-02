from scrape import write_table
import dateparser
import csv

TABLE_HEADER = ['event_id', 'visit_type', 'name', 'country', 'locale', 'remarks', 'date_start', 'date_end']

def main():
    with open('../pres-travel-analysis/data/travel_raw.csv', 'r') as csv_in:
        parsed_csv = csv.reader(csv_in)
        all_rows = []
        event_id = 0
        next(parsed_csv)
        for row in parsed_csv:
            date_start, date_end = date_transform(row[5])
            row.remove(row[5])
            row.extend([date_start, date_end])
            row.insert(0, event_id)
            clean = separate_locale(row)
            event_id += 1
            all_rows.extend(clean)
        write_table('travel_tidy.csv', all_rows, TABLE_HEADER)

def date_transform(string):
    # Some dashes are not scraped correctly. This fixes the mistake in scraping.
    string = string.replace('â€“', '–')
    if len(string.split(', ')) > 2:
        return dateparser.parse(string.split("–")[0]).date(), dateparser.parse(string.split("–")[1]).date()

    date, year = string.split(', ')
    date_depart = date
    date_return = date
    if '–' in date:
        date_depart, date_return = date.split('–')
        if len(date_return.split(' ')) == 1:
            date_return = date_depart.split(" ")[0] + " " + date_return
    return dateparser.parse(date_depart + " " + year).date(), dateparser.parse(date_return + " " + year).date()

def separate_locale(array):
    city_list = []
    if len(array[4].split(', ')) > 1:
        for city in array[4].split(', '):
            new_arr = array.copy()
            new_arr.remove(array[4])
            new_arr.insert(4, city)
            city_list.append(new_arr)  
        return city_list
    return [array]
    
if __name__ == '__main__':
    main()