import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils import cols, events, event_keys, years, str_to_time

import warnings
warnings.filterwarnings('ignore')

mode = 'append'
#mode = 'write'

df_name = 'athletics_IT_2.csv'
query_template = "https://www.fidal.it/graduatorie.php?anno={}&tipo_attivita={}&sesso={}&categoria=X{}&gara={}&tipologia_estrazione=2&vento=0&regione=0&nazionalita=2&limite=0&societa=&submit=Invia"
df = pd.DataFrame(columns=cols)
if mode == 'append':
    df = pd.read_csv(df_name, error_bad_lines=False, index_col=None)
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'])

for event, v in events.items():
    types = v[event_keys['type']]
    event_number = v[event_keys['event_number']]
    down_limit = str_to_time(v[event_keys['down_limit']])
    for t in types:
        for s in v[event_keys['sex']]:
            for y in years:
                full_event_name = '{} ({}) ({}) of year {}'.format(event, t, s, y)
                print('Scraping event: {}'.format(full_event_name))
                if len(df[(df.event == event) & (df.type == t) & (df.sex == s) & (df.date.dt.year == y)]) > 0:
                    print('Event skipped: already scraped')
                    continue
                y = str(y)
                query = query_template.format(y, t, s, s, event_number)
                page = requests.get(query)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find("table", {"class": "tabella"})
                if results is None:
                    print('Warning: this even has no entries')
                    continue
                elements = results.find_all("tr")
                if elements is None:
                    print('Warning: this even has no entries')
                    continue
                for el in elements:  # for each athlete
                    stats = [s.text.strip() for s in el]
                    #print(stats)
                    if len(stats) <= 2:
                        continue
                    if stats[3] is not None and len(stats[3]) > 0:
                        stats[3] = int(stats[3])
                        birth_year = stats[3] + 2000 if stats[3] < 25 else stats[3] + 1900
                    else:
                        birth_year = pd.NA  # birth year: str to int
                    try:
                        time = str_to_time(stats[0])
                    except:
                        print('Wrong time format: skipping entry')
                        continue
                    if time < down_limit:
                        print('Invalid time {} < {}: skipping entry'.format(time, down_limit))
                        continue
                    event_date = pd.to_datetime(y + '/' + stats[7], format='%Y/%d/%m').date()
                    row = {
                        cols[0]: time,  # time
                        cols[1]: stats[1],  # wind
                        cols[2]: stats[2],  # name
                        cols[3]: birth_year,  # year
                        cols[4]: stats[4].replace(",", " "),  # team
                        cols[5]: int(stats[5].split(' ')[0]),  # position in event
                        cols[6]: stats[6],  # city
                        cols[7]: event_date,  # date of event
                        cols[8]: s,  # sex
                        cols[9]: event,  # event
                        cols[10]: t,  # type
                    }
                    df = df.append(row, ignore_index=True)
                    #print(row)
                print('Added {} athletes records'.format(len(elements)))
                df['date'] = pd.to_datetime(df['date'])
                df.time = pd.to_datetime(df['time']).dt.time
                df.to_csv(df_name, index=False)
                print('Scraped {} data. Data saved to: {}'.format(full_event_name, df_name))
print('Done! Scraped {} athletes records'.format(len(df)))
