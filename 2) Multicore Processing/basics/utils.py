import requests
import os

url='https://picsum.photos/200/300'

def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
    return name

def download_img(links, file_name):
    response=requests.get(links)
    if response.status_code == 200:
        with open(file_name,'wb') as f:
            f.write(response.content)
        print(f"{os.path.basename(file_name)} Downloaded! ")
    else:
        print(f"Failed to download the {file_name}. Status code:- {response.status_code}")
    print()

def download_img_seq(img_file, img_num):
    folder=create_folder(img_file)

    for i in range(img_num):
        image_name=f"img-{i+1}.jpg"
        file_name=os.path.join(folder,image_name)
        download_img(url,file_name)