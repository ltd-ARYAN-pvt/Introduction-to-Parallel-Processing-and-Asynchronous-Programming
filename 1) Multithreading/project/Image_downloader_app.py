from concurrent.futures import ThreadPoolExecutor
import os
import requests
import time

img_file_seq='img_src_seq'
img_file_mt='img_src_mt'

#--> small height and width img
# url='https://picsum.photos/200/300' 

#--> big height and width img
url='https://picsum.photos/2000/3000'

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

def download_img_multithreading(img_file, img_num, num_threads=5):
    folder=create_folder(img_file)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(download_img, url, os.path.join(folder, f"image_threaded_{i + 1}.jpg")) for i in range(img_num)]
        # for future in futures:
        #     print(future.result())

def func_run(func, img_file, img_num, tag):
    start_t=time.time()
    func(img_file, img_num)
    total_t=time.time()-start_t
    print(f"Total time take to download {img_num} images is {total_t: .2f} seconds for {tag}")

if __name__ == "__main__":
    img_num=5
    func_run(download_img_seq,img_file_seq,img_num, "sequential method")

    func_run(download_img_multithreading,img_file_mt,img_num, "multithreading method")