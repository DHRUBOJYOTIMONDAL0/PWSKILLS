# import time
# start = time.perf_counter()

# def test_found():
#     print("Do Something")
#     print("Sleep for 1 second")
#     time.sleep(1)
#     print("Done with sleeping")
# test_found()
# test_found()
# end = time.perf_counter()
# print(f"The program finished in { round(end-start, 2)} second")   

# import time
# import multiprocessing  
# # start = time.perf_counter()

# def test_found():
#     print("Do Something")
#     print("Sleep for 1 second")
#     time.sleep(1)
#     print("Done with sleeping")
# if __name__ == "__main__":
#     start = time.perf_counter()

#     p1 = multiprocessing.Process(target=test_found)
#     p2 = multiprocessing.Process(target=test_found)
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()  # This was incorrectly p1.join() again
#     end = time.perf_counter()
#     print(f"The program finished in {round(end-start, 2)} seconds")


import time
import multiprocessing  
# start = time.perf_counter()

# def test_found():
#     print("Do Something")
#     print("Sleep for 1 second")
#     time.sleep(1)
#     print("Done with sleeping")
# if __name__ == "__main__":
#     start = time.perf_counter()
#     processes = []
#     for i in range(10):
#         p = multiprocessing.Process(target=test_found)
#         p.start()
#         processes.append(p)
#     for process in processes:
#         process.join()

#     end = time.perf_counter()
#     print(f"The program finished in {round(end-start, 2)} seconds")


def squre(num):
    result = num*num
    print(f"The squre of {num} is {result}")
if __name__ == "__main__":
    start = time.perf_counter()
    number = [1,2,3,4,6000]
    with multiprocessing.Pool() as pool:
        pool.map(squre, number)
    end = time.perf_counter()
    print(f"The program finished in {round(end-start, 2)} seconds")  