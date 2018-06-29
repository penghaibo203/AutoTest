import threading
import multiprocessing
import time
from os import getpid
from multiprocessing import Pool

def word():
    for i in range(1, 9):
        print("正在工作写文档%d，进程ID为%d" % (i, getpid()))
        time.sleep(1)


def music():
    for i in range(1, 5):
        print("正在听歌%d，进程ID为%d" % (i, getpid()))
        time.sleep(1)


# if __name__ == "__main__":
#     start_time = time.time()
#     word()
#     music()
#     end_time = time.time()
#     print("运行了一共%s" % str(end_time - start_time))


# if __name__ == "__main__":
#     threads = []
#     tw = threading.Thread(target=word)
#     threads.append(tw)
#
#     tm = threading.Thread(target=music)
#     threads.append(tm)
#
#     start_time = time.time()
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
#
#     end_time = time.time()
#     print("运行了一共%s" % str(end_time - start_time))


# if __name__ == "__main__":
#     processes = []
#     tw = multiprocessing.Process(target=word)
#     processes.append(tw)
#
#     tm = multiprocessing.Process(target=music)
#     processes.append(tm)
#
#     start_time = time.time()
#     for t in processes:
#         t.start()
#
#     for t in processes:
#         t.join()
#
#     end_time = time.time()
#     print("运行了一共%s" % str(end_time - start_time))

def output(i):
    print("now is %d" % i)
    time.sleep(3)
    print("%d had a snap" % i)




if  __name__ == "__main__":
    pool = Pool(processes=4)
    start_time = time.time()
    for i in range(10):
        #异步调用
        pool.apply_async(output, (i,))

    print("using Pool")
    pool.close()
    pool.join()
    end_time = time.time()
    print("运行了一共%s" % str(end_time - start_time))




