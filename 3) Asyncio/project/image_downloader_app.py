import asyncio
import os
import time
import aiohttp

#--> aiohttp for asynchronous HTTP on place of requests.get()

img_file='img_src'

#--> small height and width img
url='https://picsum.photos/2000/3000' 

def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)

async def download_img(links, file_name):
    print(f"{os.path.basename(file_name)} Downloading started........")
    async with aiohttp.ClientSession() as session:
        async with session.get(links) as response:
            if response.status == 200:
                content = await response.read()
                with open(file_name, 'wb') as f:
                    f.write(content)
                print(f"{os.path.basename(file_name)} Downloaded!")
            else:
                print(f"Failed to download {file_name}. Status code: {response.status}")
            print()

async def download_img_async(img_file, img_num):
    create_folder(img_file)

    tasks = []
    for i in range(img_num):
        image_name = f"img_async_{i+1}.jpg"
        file_name = os.path.join(img_file, image_name)
        tasks.append(download_img(url, file_name))

    await asyncio.gather(*tasks)

def func_run(func, img_file, img_num, tag):
    start_t = time.time()
    asyncio.run(func(img_file, img_num))  # Run the async function
    total_t = time.time() - start_t
    print(f"Total time taken to download {img_num} images is {total_t: .2f} seconds for {tag}")

if __name__=="__main__":
    img_num = 5

    # Asynchronous method (concurrent downloads)
    func_run(download_img_async, img_file, img_num, "asyncio concurrent method")