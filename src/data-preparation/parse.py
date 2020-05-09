import json

f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json', 'r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

att_list = ['id', 'created_at', 'text', 'user.location']

outfile.write('id\tcreated_at\ttext\tlocation\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))

    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    user_location = obj.get('user').get('location')

    outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text + '\t' + str(user_location) + '\n')
    if (cnt>1000): break

print('done.')
