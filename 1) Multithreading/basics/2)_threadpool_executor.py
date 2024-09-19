from concurrent.futures import ThreadPoolExecutor
import time

def let_sleep(sec):
    print(f"Program is sleep for {sec} seconds")
    time.sleep(sec)
    print(f"Program waked up after {sec} seconds")

#--> Method 1 :- Creating individual threads in threadpool

def pooling():
    with ThreadPoolExecutor(max_workers=4) as executor:
        f1=executor.submit(let_sleep,4)
        f2=executor.submit(let_sleep,3)
        f3=executor.submit(let_sleep,2)
        f4=executor.submit(let_sleep,3)
        print(f1.result())
        print(f2.result())
        print(f3.result())
        print(f4.result())


#--> Method 2 :- Using map or iterator

def pooling_map():
    with ThreadPoolExecutor(max_workers=4) as executor:
        ls=[4,3,2,3]
        results=executor.map(let_sleep,ls)
        for r in results:
            print(r)

pooling_map()