import sys
import json
import html2text
import csv
import random

ROW_COUNT = 10000

new_rows = []

csv.field_size_limit(sys.maxsize)
with open('./data/deep.csv', 'r') as f:
    r = csv.DictReader(x.replace('\0', '') for x in f)
    data = [row for row in r]

    new_data = []
    for datum in random.sample(data, ROW_COUNT):
        new_data.append({
            'id': datum['id'],
            'text': html2text.html2text(datum['text']) if datum['text'].find('<body>') != -1 else datum['text'],
            'publisher': datum['publisher'],
            'published_date': datum['published_date'],
            'title': datum['title'],
        })

    json_data = json.dumps(new_data)
    print(json_data)
