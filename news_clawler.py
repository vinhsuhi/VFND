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
    outputs = NewsPlease.from_urls(links_list, timeout=6)
    final_outputs = {}
    important_keys = ['authors', 'date_publish', 'description', 'image_url', 'language', 'title', 'maintext']
    for key, value in tqdm(outputs.items()):
        paper_data = {}
        for im_key in important_keys:
            paper_data[im_key] = value.__dict__[im_key]
        final_outputs[key] = paper_data

    pickle.dump(open(destination, 'wb'), final_outputs)

if __name__ == "__main__":
    news_links_path = 'Dataset/news_links'

    to_save_path = 'Dataset/raw_news'
    if not os.path.exists(to_save_path):
        os.mkdir(to_save_path)

    files = os.listdir(news_links_path)

    get_data(news_links_path + '/' + files[0], destination=to_save_path + '/' + files[0][14:-4] + '.pkl')
