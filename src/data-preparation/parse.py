import json

f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json', 'r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

# att_list = ['id', 'created_at', 'text', 'user.location']

outfile.write('id\ttext\tlocation\n')

cnt = 0
nohashtag_cnt = 0
noloc_cnt = 0
for line in con:
    if len(line) <= 5:
        continue

    obj = json.loads(line.replace('\n',''))

    text = obj.get('text')

    text = text.replace('\t', '')

    text = text.replace('\n', '')

    user_location = obj.get('user').get('location')

    if not user_location:
        noloc_cnt += 1
        continue

    user_location = user_location.replace('\n', '')
    user_location = user_location.replace('\t', '')
    user_location = user_location.replace('\"', '')

    # dataset info: num_total: 63856, num_withoutCorona: 3265, num_onlyContainWhiteHouse:
    # ['#coronavirus', '#DonaldTrump', '#Trump', '#PresidentTrump',
    # '#PressBriefing', '#WhiteHouse', '#PressConference', '#Whitehousebriefing',
    # '#reopenamerica', and '#coronavirustaskforce']

    # filtering the tweet via hashtag
    # ht_filter = ['PressBriefing', 'WhiteHouse', 'PressConference', 'Whitehousebriefing',
    # 'reopenamerica', 'DonaldTrump']

    ht_filter = ['Covid_19', 'covid19', 'Covid19', 'COVID19', 'Coronavirus', 'CoronaVirus', 'CORONAVIRUS',
                 'coronavirus', 'coronavirustaskforce', 'DonaldTrump', 'Trump', 'trump', 'TRUMP', 'PresidentTrump',
                 'PressBriefing', 'WhiteHouse', 'PressConference', 'Whitehousebriefing', 'reopenamerica']
    obj_ht = obj.get('entities')['hashtags']
    filter_flag = False
    for h in obj_ht:
        if h['text'] in ht_filter:
            filter_flag = True
    if filter_flag:
        outfile.write(obj.get('id_str')+'\t' + text + '\t' + str(user_location) + '\n')
        cnt += 1
        print(str(cnt) + ' parsed')
    else:
        nohashtag_cnt += 1


# 19989 tweets preserved
# 23237 records have been cleaned because they lack location information
# 20630 records have been cleaned because of incorrect hashtag

print(str(noloc_cnt) + ' records have been cleaned because they lack location information')
print(str(nohashtag_cnt) + ' records have been cleaned because of incorrect hashtag')
print('Parsing done.')
