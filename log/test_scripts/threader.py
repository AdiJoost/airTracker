import threading
import time

                    
def daemon(dicty):
    while not dicty["shutdown"]:
        dicty["Key"] += 1
        time.sleep(1)

   



if __name__ == '__main__':
    my_dict = {"Key": 123,
                "home": 444,
                "shutdown": False}

    damon_thread = threading.Thread(target=daemon, args=(my_dict,))
    damon_thread.start()
    for i in range(10):
        print(my_dict)
        time.sleep(1)
    my_dict["shutdown"] = True
    damon_thread.join()
    
