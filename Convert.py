'''
Convert Yelp Academic Dataset from JSON to CSV

Requires Pandas (https://pypi.python.org/pypi/pandas)

By Paul Butler, No Rights Reserved
'''

'''import json
import pandas as pd
from glob import glob
import codecs
global df
global s
global count

def convert(x):
    ob = json.loads(x)
    for k, v in ob.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob


s = ""
count = 0
for json_filename in glob('*.json'):
    csv_filename = '%s.csv' % json_filename[:-5]
    print('Converting %s to %s' % (json_filename, csv_filename))
    with open('yelp_dataset_challenge_round9.json','rb') as f: #open in binary mode
        for line in f:
            for cp in ('cp1252', 'cp850'):
                try:
                    if count is 0:
                        count = 1
                    else:
                        #s = str(line.decode(cp))
                        s = str(line.decode('utf-8'))
                except UnicodeDecodeError:
                    pass
    df = pd.DataFrame([convert(s)])
    df.to_csv(csv_filename, encoding='utf-8', index=False)'''




import json
import pandas as pd

cuisines = ["American (Traditional)", "American (New)", "Latin American", "Italian", "Thai",
            "Chinese", "Japanese", "Turkish", "French", "Mexican", "German", "Polish", "Greek",
            "Pakistani", "Ethiopian", "Taiwanese", "Middle Eastern", "Indian", "Korean", "Vietnamese", "Canadian", ]
list = []
lines = open("yelp_academic_dataset_business.json",encoding='utf-8').readlines()
for line in lines:
    cat = None
    star = None
    cuis = "other"
    line_list = []
    jline = json.loads(line)
    for k, v in jline.items():
        if k == "categories":
            cat = v
        if k == "stars":
            star = v
    if(cat!= None):
        for cuisine in cuisines:
            if cuisine in cat:
                cuis = cuisine
                cat.remove(cuisine)
                break

    if (cat != None):
        if ("restaurants" in cat) or ("Restaurants" in cat):
            if star!= None:
                line_list.append(cat)
                line_list.append(star)
                list.append(line_list)

my_df = pd.DataFrame(list)
my_df.to_csv('business.csv', index=False, header=False)


list = []
lines1 = open("yelp_academic_dataset_review.json",encoding='utf-8').readlines()
for line in lines1:
    text = None
    star = None
    line_list = []
    jline = json.loads(line)
    for k, v in jline.items():
        if k == "text":
            text = v
        if k == "stars":
            star = v

    if text != None:
        if star!= None:
            line_list.append(text)
            line_list.append(star)
            list.append(line_list)

my_df1 = pd.DataFrame(list)
my_df1.to_csv('review.csv', index=False, header=False)

