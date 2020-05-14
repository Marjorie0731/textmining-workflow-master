import requests
import os

if not os.path.exists('../../data/team13_covid19_briefing_usa.zip'):
    print('Downloading raw data... please wait.')

    data = requests.get('https://uvt-public.s3.eu-central-1.amazonaws.com/data/rsm2020/team13_covid19_briefing_usa.zip')

    print('Writing raw data to file')

    os.makedirs('../../data', exist_ok=True)

    f = open('../../data/team13_covid19_briefing_usa.zip', 'wb')

    f.write(data.content)

    f.close()

    print('Done.')
else:
    print('Raw data is downloaded already, skip to next step')
