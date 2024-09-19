from concurrent.futures import ProcessPoolExecutor
import utils
import os
import requests
import time

def download_img(file_name,links=utils.url):
    print(f"{os.path.basename(file_name)} Download started ........... ")
    response=requests.get(links)
    if response.status_code == 200:
        with open(file_name,'wb') as f:
            f.write(response.content)
        print(f"{os.path.basename(file_name)} Downloaded! ")
    else:
        print(f"Failed to download the {file_name}. Status code:- {response.status_code}")
    print()

if __name__ == "__main__":
    img_file='img_src'
    img_file=utils.create_folder(img_file)

    start_t=time.time()
    with ProcessPoolExecutor() as executor:
        ls=[os.path.join(img_file,f"img-mc-{i+1}.jpg") for i in range(50)]
        results=executor.map(download_img, ls)

        for r in results:
            print(r)
    end_t=time.time()
    print("time take is",(end_t-start_t),"sec")