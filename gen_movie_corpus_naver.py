import os
import json


kobis_dir = './moviedata/kobis'
naver_dir = './moviedata/naver'
watcha_dir = './moviedata/watcha'
# naver_save_file_path = './moviedata/naver/naver_corpus_for_wordvec.txt'
# watcha_save_file_path = './moviedata/watcha/watcha_corpus_for_wordvec.txt'
naver_save_file_path = './moviedata/naver_corpus_for_wordvec.txt'

file_list = os.listdir(kobis_dir)
file_list.sort()

# naver 파일 생성..
with open(naver_save_file_path, 'w', encoding="utf-8") as f_write:
    for file in file_list:
        # crawl_one_list(crawler, file)
        file_path = os.path.join(kobis_dir, file)
        naver_file_path = os.path.join(naver_dir, 'data_'+file)
        print(file_path)
        with open(file_path, 'r', encoding='utf-8-sig') as f_kobis:
          with open(naver_file_path, 'r', encoding='utf-8') as f_naver:
              list_kobis = json.load(f_kobis)
              list_naver = json.load(f_naver)
              movie_list = list_kobis["movieListResult"]["movieList"]

              for key, value in list_naver.items():
                  if value["synopsis"]:
                      f_write.write(value["synopsis"])
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


                  f_write.write("\n\n")

        # break

