import threading
import time

def let_sleep(sec):
    print(f"Program is sleep for {sec} seconds")
    time.sleep(sec)
    print(f"Program waked up after {sec} seconds")

start_t=time.time()
let_sleep(4)
let_sleep(3)
let_sleep(2)
end_t=time.time()
print(f"Time taken to complete above process is {end_t-start_t} sec")
# -> This will take nearly 9 secs to complete


start_t=time.time()
t1=threading.Thread(target=let_sleep, args=[4])
t2=threading.Thread(target=let_sleep, args=[3])
t3=threading.Thread(target=let_sleep, args=[2])

#--> t.start():- this will start the process and send it to the backend

t1.start()
t2.start()
t3.start()

#--> t.join():- This will tell that wait for threads to complete it's execution

t1.join()
t2.join()
t3.join()
end_t=time.time()

print(f"Time taken to complete above process is {end_t-start_t} sec")