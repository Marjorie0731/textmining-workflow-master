import pandas as pd
import os

data = pd.read_csv('../../gen/data-preparation/output/dataset.csv', delimiter = '\t')

data.head()

print("state-analysis begins")

# Blue/Red state classification function
# Last update: May.24,2020
# reference: https://www.270towin.com/maps/consensus-2020-electoral-map-forecast
def get_BR(state):
    blue_state = ["CA", "CO", "CT", "DC", "DE", "HI", "IL", "ME", "MD", "MA", "MN", "NV", "NH", "NJ", "NM", "NY",
                  "OR", "RI", "TX",  "VT", "VA", "WA", ]

    red_state = ["AL", "AR", "ID", "MT", "WY", "UT", "ND", "SD", "NE", "KS", "MO", "OK",
                 "LA", "IN", "MS", "TN", "KY", "WV", "GA", "SC", "OH", "AK", "IA", ]

    Tossup_state = ["AZ", "WI", "MI", "PA",  "NC", "FL"]

    if state in blue_state:
        return 'B'
    if state in red_state:
        return 'R'
    if state in Tossup_state:
        return 'T'
    return 'O'


state_ab = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "other"]


column = ['state', 'tweet_cnt', 'avg_polarity', 'B/R']

tweet_cnt = [0 for i in range(52)]
avg_polarity = [0 for i in range(52)]
BR = [0 for i in range(52)]

# Blue/Red state classify
for idx in range(len(BR)):
    BR[idx] = get_BR(state_ab[idx])


for i, j in data.iterrows():
    print(str(i) + ' in processing')

# state
    try:
        state = j['state']
        idx = state_ab.index(state)
        tweet_cnt[idx] += 1
        avg_polarity[idx] += j['polarity']
    except:
        print('error occur')

# polarity mean calculation
for p in range(len(avg_polarity)):
    if tweet_cnt[p]!=0:
        avg_polarity[p] = avg_polarity[p]/tweet_cnt[p]
    else:
        avg_polarity[p] = 0
data.head()

dt = {
    'state':state_ab,
    'tweet_cnt':tweet_cnt,
    'avg_polarity':avg_polarity,
    'BR':BR
}
state_dt = pd.DataFrame(dt)

os.makedirs('../../gen/analysis/temp/', exist_ok=True)

state_dt.to_csv('../../gen/analysis/temp/state-analysis.csv', index = False, sep='\t')