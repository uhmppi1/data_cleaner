import json, ijson
import re
from pprint import pprint

filename = '/home/pipaek/data/corpus/hangul/namuwiki/namuwiki190312/namuwiki_20190312.json'

# Read file to memory, it takes some time.
# with open(filename) as data_file:
#     data = json.load(data_file)   # 10GB 짜리를 메모리에 한번에 올릴 수 있나??


# f = open("metadatam1.json")
# objs = ijson.items(f, '')
# see http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex
chinese = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
japanese = re.compile(u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]', re.UNICODE)

def strip(text):
    text = re.sub(r"\{\{\{#\!html[^\}]*\}\}\}", '', text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)  # remove html
    text = re.sub(r"#redirect .*", '', text, flags=re.IGNORECASE)  # remove redirect
    text = re.sub(r"\[\[분류:.*", '', text)  # remove 분류
    text = re.sub(r"\[\[파일:.*", '', text)  # remove 파일
    text = re.sub(r"\* 상위 문서 ?:.*", '', text)  # remove 상위문서
    text = re.sub(r"\[youtube\(\w+\)\]", '', text, flags=re.IGNORECASE)  # remove youtube
    text = re.sub(r"\[include\(([^\]|]*)(\|[^]]*)?\]", r'\1', text, flags=re.IGNORECASE)  # remove include
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]", r'\1', text)  # remove link
    text = re.sub(r"\[\*([^\]]*)\]", '', text)  # remove 각주
    text = re.sub(r"\{\{\{([^\ }|]*) ([^\}|]*)\}\}\}", r'\2', text)  # remove text color/size
    text = re.sub(r"'''([^']*)'''", r'\1', text)  # remove text bold
    text = re.sub(r"(~~|--)([^']*)(~~|--)", '', text)  # remove strike-through
    text = re.sub(r"\[\[분류:.*", '', text)  # remove 분류

    text = re.sub(r"\|\|(.*)\|\|", '', text)  # remove table

    text = chinese.sub('', text)  # remove chinese
    text = japanese.sub('', text)  # remove japanese
    text = text.strip()
    return text

cleaned_file_name = './cleaned_data/namuwiki/namuwiki_20190312.txt'
# namuwiki_save_file_path =

#total count = 661031
# with open(filename) as data_file:
#     with open(cleaned_file_name, 'w', encoding="utf-8") as f_write:
#         objs = ijson.items(data_file, 'item')
#
#         for i, o in enumerate(objs):
#             if i % 10000 == 0:
#                 print('#### count = %d' % i)
#
#
#
#     # print(sum(1 for x in objs))
#     print('total count = %d' % i)

with open(filename) as data_file:
    task_completed = False

    with open(cleaned_file_name, mode='w') as corpus_file:
        objs = ijson.items(data_file, 'item')
        print('### starts..')
        for i, o in enumerate(objs):
            if i % 10000 == 0:
                print('#### count = %d' % i)
            if i > 5:
                break

            # print(o)
            # print(strip(o['text']))
            corpus_file.write(strip(o['text']))


# data is list of articles
# # Let's see how many articles in the database
# print("number of articles:", len(objs))
#
# # Let's see the first article
# print("The first article is:")
# print(objs[0])

