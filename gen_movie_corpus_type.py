import os
import json
import collections

kobis_dir = './moviedata/kobis'
kobis_list_dir = './moviedata/kobis_list'
naver_dir = './moviedata/naver'
watcha_dir = './moviedata/watcha'
type_save_file_path = './moviedata/type/corpus_for_wordvec_{}.txt'

file_list = os.listdir(kobis_dir)
file_list.sort()
d = collections.defaultdict(int)


def get_type_from_kobis(kobis_movie_list, moviename, movie_type_dict):
    def __get_type_from_kobis(moviecode):
        if moviecode in movie_type_dict:
            return movie_type_dict[moviecode]
        else:
            return 'unknown'

    for movie in kobis_movie_list:
        if movie['movieNm'] == moviename:
            moviecode = movie['movieCd']
            return __get_type_from_kobis(moviecode)
    return 'notfound'


def get_movie_type_dict():
    file_list = os.listdir(kobis_list_dir)
    # file_list.sort()
    movie_type_dict = {}
    movie_type_count_dict = {}
    mismatch_count = 0

    for file in file_list:
        file_path = os.path.join(kobis_list_dir, file)
        print(file_path)
        movie_type = file.rsplit("_", 1)[0]
        print(movie_type)

        with open(file_path, 'r') as f_kobis_list:
            count = 0
            for movie_code in f_kobis_list.readlines():
                if movie_code.strip() not in movie_type_dict:
                    movie_type_dict[movie_code.strip()] = movie_type
                    count += 1
                else:
                    if movie_type_dict[movie_code.strip()] != movie_type:
                        print('#### movie_type_dict mismatch')
                        mismatch_count += 1
            print('movie count = %d' % count)
            if movie_type in movie_type_count_dict:
                movie_type_count_dict[movie_type] += count
            else:
                movie_type_count_dict[movie_type] = count

    print(movie_type_count_dict)
    print('MISMATCH COUNT = %d' % mismatch_count)
    return movie_type_dict

movie_type_dict = get_movie_type_dict()
movie_type_dict_inv = {}
for k, v in movie_type_dict.items():
    if v in movie_type_dict_inv:
        movie_type_dict_inv[v] += 1
    else:
        movie_type_dict_inv[v] = 1
print(movie_type_dict_inv)



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
                movietype = get_type_from_kobis(movie_list, moviename, movie_type_dict)
                file_path_to_write = type_save_file_path.format(movietype)
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
                movietype = get_type_from_kobis(movie_list, moviename, movie_type_dict)
                file_path_to_write = type_save_file_path.format(movietype)
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