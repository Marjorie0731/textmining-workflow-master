import pandas as pd
from textblob import TextBlob
import os

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t', error_bad_lines=False)
data.head()


def str_match(s, l):
    # s = str.upper(s)
    # l = str.upper(l)
    if s in l:
        return True
    else:
        return False


def get_stateidx(location, statelist):
    for state in statelist:
        if str_match(state, location):
            return statelist.index(state)
    return False


def get_state(location):
    '''
    :param location: city of user
    :return state:  state of user
    '''
    state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
                  "Connecticut", "Washington", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
                  "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
                  "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                  "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
                  "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                  "Utah", "Vermont", "Virginia", "Washington","West Virginia", "Wisconsin", "Wyoming"]

    state_ab = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    stateidx = get_stateidx(location, state_list)
    if stateidx:
        return state_ab[stateidx]
    else:
        stateidx = get_stateidx(location[-3:], state_ab)
        if stateidx:
            return state_ab[stateidx]
        else:
            return 'other'
    return 'other'


other_cnt = 0
usa_cnt = 0
print('textmining and state classification begins')
for i, j in data.iterrows():
    print(str(i) + ' in processing')

# Textblob mining
    try:
        blob = TextBlob(j['text'])
        data.loc[i, 'polarity'] = blob.sentiment.polarity
        data.loc[i, 'subjectivity'] = blob.sentiment.subjectivity

    except:
        data.loc[i, 'polarity'] = ''
        data.loc[i, 'subjectivity'] = ''

# State classification
    try:
        location = j['location']
        state = get_state(location)
        data.loc[i, 'state'] = state
        if state == 'other':
            other_cnt += 1
        else:
            usa_cnt += 1

    except:
        data.loc[i, 'state'] = ''

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)


print('textmining and state classification done.')
print(str(usa_cnt) + ' records in USA')
print(str(other_cnt) + ' records in other nations')
