import multiprocessing
import time
import utils
import os


if __name__=="__main__":
    img_file='img_src'
    img_num=5
    start_t=time.time()
    utils.download_img_seq(img_file, img_num)
    int_t=time.time()
    print(f"Time taken for single core to download {img_num} images is {int_t-start_t} sec")

    start_t=time.time()
    processes=[]
    for i in range(img_num):
        img_file=utils.create_folder(img_file)
        file_name=os.path.join(img_file,f"img-mc-{i+1}.jpg")

        p=multiprocessing.Process(target=utils.download_img, args=[utils.url,file_name])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    end_t=time.time()
    print(f"Time taken for multicore to download {img_num} images is {end_t-start_t} sec")