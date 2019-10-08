import os
import json
import collections

kobis_dir = './moviedata/kobis'
naver_dir = './moviedata/naver'
watcha_dir = './moviedata/watcha'
genre_save_file_path = './moviedata/genre/corpus_for_wordvec_{}.txt'

file_list = os.listdir(kobis_dir)
file_list.sort()
d = collections.defaultdict(int)

def get_genre_from_kobis(kobis_movie_list, moviename):
    for movie in kobis_movie_list:
        if movie['movieNm'] == moviename:
            return movie['repGenreNm'].replace("/","")
    return 'NOTFOUND'
    

for file in file_list:
    file_path = os.path.join(kobis_dir, file)
    print(file_path)
    naver_file_path = os.path.join(naver_dir, 'data_' + file)
    watcha_file_path = os.path.join(watcha_dir, 'data_' + file)

    with open(file_path, 'r', encoding='utf-8-sig') as f_kobis:
        list_kobis = json.load(f_kobis)
        movie_list = list_kobis["movieListResult"]["movieList"]
        with open(naver_file_path, 'r', encoding='utf-8') as f_naver:
            list_naver = json.load(f_naver)
            for key, value in list_naver.items():
                moviename = value["movieNm"]
                genre = get_genre_from_kobis(movie_list, moviename)
                file_path_to_write = genre_save_file_path.format(genre)
                with open(file_path_to_write, 'a', encoding="utf-8") as f_write:
                    if value["synopsis"]:
                      f_write.write(value["synopsis"])
                      f_write.write("\n")
                    else:
                        continue
                    if value["reporters"]:
                      reporters = value["reporters"]
                      for report in reporters:
                          f_write.write(report["text"])
                          f_write.write("\n")
                    if value["comments"]:
                      comments = value["comments"]
                      for comment in comments:
                          f_write.write(comment["text"])
                          f_write.write("\n")
                    f_write.write('<eod>\n')

        with open(watcha_file_path, 'r', encoding='utf-8') as f_watcha:
            list_watcha = json.load(f_watcha)
            for key, value in list_watcha.items():
                moviename = value["movieName"]
                genre = get_genre_from_kobis(movie_list, moviename)
                file_path_to_write = genre_save_file_path.format(genre)
                with open(file_path_to_write, 'a', encoding="utf-8") as f_write:
                    if value["synopsis"]:
                        f_write.write(value["synopsis"])
                        f_write.write("\n")
                    else:
                        continue
                    if value["comments"]:
                        comments = value["comments"]
                        for comment in comments:
                            f_write.write(comment["comment"])
                            f_write.write("\n")
                    f_write.write('<eod>\n')

            # print(movie_list)
            # print(type(movie_list))
            # for movie in movie_list:
            #     # print(movie["repGenreNm"])
            #     if movie["repGenreNm"] is not None:
            #         d[movie["repGenreNm"]] += 1
    # break

# print(d)
'''
{'드라마': 11059, 
 '다큐멘터리': 4852, 
 '기타': 5016, 
 '가족': 229, 
 '전쟁': 183, 
 'SF': 471, 
 '성인물(에로)': 1654, 
 '액션': 2823, 
 '판타지': 351, 
 '코미디': 3014, 
 '': 3478, 
 '미스터리': 341, 
 '공포(호러)': 1568, 
 '애니메이션': 6059, 
 '뮤지컬': 101, 
 '멜로/로맨스': 3486, 
 '범죄': 721, 
 '사극': 74, 
 '스릴러': 1017, 
 '어드벤처': 306, 
 '공연': 231, 
 '서부극(웨스턴)': 23})'''
