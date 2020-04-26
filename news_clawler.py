from newsplease import NewsPlease
import os
import json 
import pickle
from tqdm import tqdm

def get_data(path, destination):
    links_list = set()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            link = line.split()[0]
            if len(link) < 10:
                continue
            links_list.add(link)
    links_list = list(links_list)
    final_outputs = {}
    important_keys = ['authors', 'date_publish', 'description', 'image_url', 'language', 'title', 'maintext']
    for key in tqdm(links_list):
        value = NewsPlease.from_url(key, timeout=4)
        paper_data = {}
        for im_key in important_keys:
            paper_data[im_key] = value.__dict__[im_key]
        final_outputs[key] = paper_data
    pickle.dump(final_outputs, open(destination, 'wb'))

if __name__ == "__main__":
    news_links_path = 'Dataset/news_links'

    to_save_path = 'Dataset/raw_news'
    if not os.path.exists(to_save_path):
        os.mkdir(to_save_path)

    files = os.listdir(news_links_path)

    for file in files:
        print("Crawl for file: {}".format(file))
        get_data(news_links_path + '/' + file, destination=to_save_path + '/' + file[14:-4] + '.pkl')
