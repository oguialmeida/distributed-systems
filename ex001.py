import threading

def count_up():
    arr = []
    for i in range(1, 501):
        arr.append(i)
    print(arr)


def count_down():
    arr = []
    for i in range(500, 0, -1):
        arr.append(i)
    print(arr)

def exec_thread():
    thread1 = threading.Thread(target=count_up)
    thread2 = threading.Thread(target=count_down)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    exec_thread()