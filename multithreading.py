#Single Threading Code
#import time
# start = time.perf_counter()

# def test_found():
#     print("Do Something")
#     print("Sleep for 1 second")
#     time.sleep(1)
#     print("Done with sleeping")
# test_found()
# end = time.perf_counter()
# print(f"The Program finished in {round(end - start)} seconds")



# import time
# import threading
# start = time.perf_counter()

# def test_found():
#     print("Do Something ")
#     print("Sleep for 1 second")
#     time.sleep(1)
#     print("Done with sleeping ")
# t1 = threading.Thread(target= test_found)
# t2 = threading.Thread(target = test_found)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.perf_counter()
# print(f" The program is finished {round(end-start, 2)} seconds")


import time
import threading
start = time.perf_counter()

def test_found():
    print("Do Something")
    print("Sleep for 1 second")
    time.sleep(1)
    print("Done with sleeping")
threads =  []
for i in range(10):
    t = threading.Thread(target= test_found)
    t.start()
for thread in threads:
    thread.join()
end = time.perf_counter()
print(f"The program is finished round{(end-start, 2)} seconds")