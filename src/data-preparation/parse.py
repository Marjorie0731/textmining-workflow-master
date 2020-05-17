import json

f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json', 'r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

# att_list = ['id', 'created_at', 'text', 'user.location']

outfile.write('id\tcreated_at\ttext\tlocation\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue


    obj = json.loads(line.replace('\n',''))

    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    user_location = obj.get('user').get('location')

    cnt_retweet = obj.get('retweet_count')

    # dataset info: num_total: 63856, num_withoutCorona: 3265, num_onlyContainWhiteHouse:
    # ['#coronavirus', '#DonaldTrump', '#Trump', '#PresidentTrump',
    # '#PressBriefing', '#WhiteHouse', '#PressConference', '#Whitehousebriefing',
    # '#reopenamerica', and '#coronavirustaskforce']

    # filtering the tweet via hashtag
    # ht_filter = ['PressBriefing', 'WhiteHouse', 'PressConference', 'Whitehousebriefing', 'reopenamerica', 'DonaldTrump']
    ht_filter = ['DonaldTrump', 'Trump', 'PresidentTrump','PressBriefing', 'WhiteHouse', 'PressConference', 'Whitehousebriefing', 'reopenamerica']
    obj_ht = obj.get('entities')['hashtags']
    filter_flag = False
    for h in obj_ht:
        if h['text'] in ht_filter:
            filter_flag = True
    if filter_flag:
        outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text + '\t' + str(user_location) + str(cnt_retweet)+'\n')
        cnt += 1
        print(str(cnt) + ' parsed')
    # if (cnt>1000): break

print('Parsing done.')
