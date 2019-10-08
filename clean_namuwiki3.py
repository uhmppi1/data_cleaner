# -*- coding: utf8 -*-
import json, ijson
import re
from pprint import pprint
from namuwiki.extractor import extract_text
try:
# python 3
	from urllib.parse import unquote_plus
except:
# python 2
	from urllib import unquote_plus




filename = '/home/pipaek/data/project/kisdi/data/namuwiki/namuwiki190312/namuwiki_20190312.json'
cleaned_file_name = './cleaned_data/namuwiki/namuwiki_20190312.txt'

with open(filename) as data_file:
  task_completed = False

  with open(cleaned_file_name, mode='w') as corpus_file:
    objs = ijson.items(data_file, 'item')
    print('### starts..')
    for i, o in enumerate(objs):
      if i % 10000 == 0:
        print('#### count = %d' % i)
      # if i > 50:
      #   break

      # print(o)
      # print(strip(o['text']))

      text = extract_text(o['text'])
      if text:
        corpus_file.write(extract_text(o['title']))
        corpus_file.write('\n')
        corpus_file.write(text)
        corpus_file.write('\n\n\n')