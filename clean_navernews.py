import json, ijson
import re
from pprint import pprint

# filename = 'raw_data/navernews/20190101_경제.json'

# Read file to memory, it takes some time.
# with open(filename) as data_file:
#     data = json.load(data_file)   # 10GB 짜리를 메모리에 한번에 올릴 수 있나??


# f = open("metadatam1.json")
# objs = ijson.items(f, '')
# see http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex
chinese = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
japanese = re.compile(u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]', re.UNICODE)

def strip(text, press):
    text = re.sub(r"\{\{\{#\!html[^\}]*\}\}\}", '', text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)  # remove html
    # text = re.sub(r"#redirect .*", '', text, flags=re.IGNORECASE)  # remove redirect
    # text = re.sub(r"\[\[분류:.*", '', text)  # remove 분류
    # text = re.sub(r"\[\[파일:.*", '', text)  # remove 파일
    # text = re.sub(r"\* 상위 문서 ?:.*", '', text)  # remove 상위문서
    text = re.sub(r"\[youtube\(\w+\)\]", '', text, flags=re.IGNORECASE)  # remove youtube
    text = re.sub(r"\[include\(([^\]|]*)(\|[^]]*)?\]", r'\1', text, flags=re.IGNORECASE)  # remove include
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]", r'\1', text)  # remove link
    text = re.sub(r"\[\*([^\]]*)\]", '', text)  # remove 각주
    text = re.sub(r"\{\{\{([^\ }|]*) ([^\}|]*)\}\}\}", r'\2', text)  # remove text color/size
    text = re.sub(r"'''([^']*)'''", r'\1', text)  # remove text bold
    text = re.sub(r"(~~|--)([^']*)(~~|--)", '', text)  # remove strike-through

    text = re.sub(r"\|\|(.*)\|\|", '', text)  # remove table

    # pattern = r"^[:print:]*%s\s[:print:]+\s기자\s" % press
    pattern = r".*%s.+기자\s" % press
    print(pattern)
    text = re.sub(pattern, '', text) # 기자이름

    pattern = r".*SUB TITLE START.+SUB TITLE END\s"
    print(pattern)
    text = re.sub(pattern, '', text)  # SUB TITLE


    # text = chinese.sub('', text)  # remove chinese
    # text = japanese.sub('', text)  # remove japanese
    return text


# text = '2일 검찰 고발 “퇴직 공무원 공무 비밀 엄수해야” 신재민 “내부고발한 것 추가로 영상 올리겠다” 구윤철 기획재정부 2차관과 신재민 전 기재부 사무관. 구 차관은 지난달 31일 긴급 브리핑에서 “법적 검토를 거쳐서 요건에 해당한다면 적절한 조치를 취하겠다”고 말했다. 신 전 사무관은 “내부고발한 이상 정부의 재발 방지 사과 듣고 그리고 제가 잘 되는게 도리”라고 밝혔다. 연합뉴스 신 전 사무관 유튜브 세종 이데일리 최훈길 기자 기획재정부가 신재민 전 기재부 사무관을 공무상 비밀을 누설한 혐의로 검찰에 고발하기로 했다. 신 전 사무관은 자신은 내부고발자라며 정부의 사과를 요구했다. 필요하다면 언론과도 접촉하겠다며 추가 폭로를 예고했다. 폭로내용을 둘러싼 진실공방이 실정법 위반 논란으로 확산하는 양상이다. ◇기재부 “자료 편취해 공개 심각한 문제” 기재부는 1일 밤 보도참고자료에서 “신재민 전 사무관에 대해서 내일 검찰에 고발조치할 계획”이라고 밝혔다. 기재부는 “공무원이었던 자가 직무상 취득한 비밀을 누설하는 것은 금지돼 있다”며 “특히 소관 업무가 아닌 자료를 편취해 이를 대외 공개하는 것은 더욱 심각한 문제”라고 밝혔다. 기재부는 관련된 혐의로 업무상 비밀 누설죄와 공무상 비밀 누설죄를 검토 중이다. 국가공무원법 60조 은 “공무원은 재직 중은 물론 퇴직 후에도 직무상 알게 된 비밀을 엄수 嚴守 하여야 한다”고 규정돼 있다. 형법 제127조에 따르면 공무원 또는 공무원이었던 자가 법령에 의한 직무상 비밀을 누설한 때에는 2년 이하의 징역이나 금고 또는 5년 이하에 자격정지에 처한다. 기재부 관계자는 통화에서 “내부 문건을 유출해 언론사 MBC 에 제보한 점 지난 달부터 유튜브·고려대 커뮤니티 고파스 에 게시물을 올린 행위 모두 공무상 비밀을 누설한 것으로 의심된다”고 말했다. 기재부는 이날 자료를 통해 적자국채의 추가 발행을 검토한 경위를 구체적으로 설명했다. 앞서 신 전 사무관은 청와대와 김동연 전 경제부총리가 연간 수천억원의 이자 부담에도 나랏빚인 적자성 국채 발행을 지시했다고 주장했다. 현 정권에 대한 정치적 잇속을 위해 박근혜정부 말기인 2017년의 국채 발행 규모를 이른바 ‘분식회계’ 하듯이 부풀리려고 했다는 게 신 전 사무관의 주장이다. 이에 기재부는 “각 방안별 장·단점이 있어 기재부 내부 논의 및 관련기관과 많은 협의가 있었다. 그 결과 8.7조원 전액을 발행하지 않기로 결정했다”며 “미리 국가채무 규모를 줄이는 것이 더 바람직하다고 판단했기 때문”이라고 밝혔다. 국채를 추가 발행하면 경기 대응을 위한 실탄 재정 을 확보하는 장점이 있다. 이 때문에 정무적 판단을 하는 청와대가 일자리 경기 대응 등을 고려해 국채 발행을 선호할 수 있다. 반면 국채 발행을 하면 이자 비용이 발생하는 단점이 있다. ‘나라 곳간지기’ 기재부로서는 국가채무 증가에 난색을 표할 수밖에 없다. 당시에는 ‘세수 풍년’이라는 말이 나올 정도로 세수 여건이 좋았기 때문에 토론 결과 국채를 발행하지 않기로 했다는 게 기재부 입장이다. ◇신재민 “朴정부 대비 정치적 고려” Vs 기재부 “사실무근” 특히 기재부는 “4조원 적자국채 추가발행을 통해 박근혜정부의 국가채무 비율을 높이려 했다는 지적은 전혀 사실이 아니다”고 강조했다. 기재부는 “4조원의 적자국채를 추가 발행해도 GDP 국내총생산 대비 국가채무 비율은 38.3%에서 38.5%로 약 0.2% 포인트 증가에 그쳐 크게 의미 있는 수준이 아니다”고 설명했다. 기재부는 “설사 추가 발행을 통해 2017년 국가채무비율을 높인다 해도 이는 박근혜 정부의 국가채무 비율이 되는 것이 아니라 문재인 정부 첫해 국가채무 비율이 되는 것이어서 그럴 이유도 없었다”며 “청와대도 의견을 제시했으나 강압적 지시는 전혀 없었다”고 밝혔다. 신 전 사무관은 당시 홍장표 경제수석이 적자국채 발행 입장이었다고 주장했다. 기재부는 신 전 사무관이 1일 공개한 ‘국가채무 비율을 덜 줄이려고 했다’는 카카오톡 메시지와 관련해서는 “중기재정 계획 논의 과정에서 국가채무의 큰 흐름을 짚어보는 과정에서 나온 의견”이라고 밝혔다. 기재부 관계자는 “조규홍 당시 차관보의 카톡 메시지는 맞다”며 “기재부 내부적으로 검토하는 과정에서 나온 여러 의견 중 하나”라고 설명했다. 기재부는 재작년 11월14일 국고채 조기상환 바이백 이 취소된 경위에 대해서는 “그 당시 적자국채 추가발행 여부 논의 국채시장에 미치는 영향 연말 국고자금 상황 등을 종합적으로 고려해 불가피하게 결정된 것”이라고 해명했다. 앞서 신 전 사무관은 김동연 전 부총리 청와대 지시에 따라 고의로 적자국채를 늘리려고 한 것이라며 “국민 기만 어처구니 없는 지시”라고 주장했다. 한편 신 전 사무관은 1일 고파스에 “내부고발한 이상 정부의 재발 방지 사과 듣고 그리고 제가 잘 되는 게 도리”라며 “영상도 다시 올리고 필요하다면 언론 접촉도 하겠다”고 밝혔다. 신 전 사무관은 제보 경위에 대해 “청와대가 민간기업 인사에 개입하지 않고 국가가 좀 더 나아지길 바라서 제보를 한 것”이라며 “비밀 엄수 위반으로 처벌하신다면 처벌을 받겠다”고 덧붙였다. 그는 “기자회견은 모레 3일 정도에 진행하려 한다”며 “내일 공간 구하고 일정 다시 올리겠다”고 밝혔다.'
# press = '이데일리'
# print(strip(text, press))

# text = '2일 검찰 고발 “퇴직 공무원 공무 비밀 엄수해야” 신재민 “내부고발한 것 추가로 영상 올리겠다” 구윤철 기획재정부 2차관과 신재민 전 기재부 사무관. 구 차관은 지난달 31일 긴급 브리핑에서 “법적 검토를 거쳐서 요건에 해당한다면 적절한 조치를 취하겠다”고 말했다. 신 전 사무관은 “내부고발한 이상 정부의 재발 방지 사과 듣고 그리고 제가 잘 되는게 도리”라고 밝혔다. 연합뉴스 신 전 사무관 유튜브 세종 이데일리 최훈길 기자 기획재정부가 신재민 전 기재부 사무관을 '
# press = '이데일리'
# print(text)
# print(strip(text, press))

filename = 'raw_data/navernews/20190101_경제.json'
cleaned_file_name = './cleaned_data/navernews/navernews_경제.txt'

with open(filename) as data_file:
    task_completed = False

    with open(cleaned_file_name, mode='w') as corpus_file:
        objs = ijson.items(data_file, 'articles')
        print('starts..')
        for i, o in enumerate(objs):
            print(i)
            if i > 5:
                break

            print(o)
            print(strip(o['contents']))
            text = strip(o['contents'])
            if text:
                # corpus_file.write(extract_text(o['title']))
                # corpus_file.write('\n')
                corpus_file.write(text)
                corpus_file.write('\n\n\n')


# data is list of articles
# # Let's see how many articles in the database
# print("number of articles:", len(objs))
#
# # Let's see the first article
# print("The first article is:")
# print(objs[0])

