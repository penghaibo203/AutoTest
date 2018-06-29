from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import threading
import multiprocessing

#分解整数因子
def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def run(f, n):
    list(f(n))


numbers = [57387594, 4398598, 38587439]


# 单线程串行执行
# start_time = time.time()
# for number in numbers:
#     run(factorize, number)
#
# end_time = time.time()
# print("运行了一共%s" % str(end_time - start_time))

# 多线程并发执行
# start_time = time.time()
# threads = []
# for number in numbers:
#     thread = threading.Thread(target=run, args=(factorize, number))
#     threads.append(thread)
#     thread.start()
#
# for t in threads:
#     t.join()
#
# end_time = time.time()
# print("运行了一共%s" % str(end_time - start_time))

# 多进程并发执行
# if __name__ == "__main__":
#     start_time = time.time()
#     processes = []
#     for number in numbers:
#         process = multiprocessing.Process(target=run, args=(factorize, number))
#         processes.append(process)
#         process.start()
#
#     for t in processes:
#         t.join()
#
#     end_time = time.time()
#     print("运行了一共%s" % str(end_time - start_time))

#求两个整数的最大公约数
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


big_nums = [(87579424, 54563783), (87994524, 9833743), (97259424, 33789893)]

# 单线程串行执行
# start_time = time.time()
# # gcd((87579424, 54563783))
# # gcd((87994524, 9833743))
# # gcd((97259424, 33789893))
# #循环执行该串行动作
# for pair in big_nums:
#     gcd(pair)
#
# end_time = time.time()
# print("运行了一共%s" % str(end_time - start_time))

if __name__ == "__main__":
    start_time = time.time()
    pool = ProcessPoolExecutor(max_workers=4)
    # pool = ThreadPoolExecutor(max_workers=4)
    results = list(pool.map(gcd, big_nums))
    print(results)
    end_time = time.time()
    print("运行了一共%s" % str(end_time - start_time))
