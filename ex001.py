# Write a Python program composed of two threads: the first must count and display 
# on the screen all numbers between 1 and 500 (in ascending order); the second must 
# count and display on the screen all numbers between 500 and 1 (in descending 
# order). As two threads must run in parallel.
import threading

# Generates a list of numbers in ascending order
def count_up():
    arr = []
    for i in range(1, 501):
        arr.append(i)
    print("Crescente:\n{}".format(", ".join(map(str, arr))))

# Generates a list of numbers in descending order
def count_down():
    arr = []
    for i in range(500, 0, -1):
        arr.append(i)
    print("Descrecente:\n{}".format(", ".join(map(str, arr))))

# Allows two threads to run at the same time
def exec_thread():
    thread1 = threading.Thread(target=count_up)
    thread2 = threading.Thread(target=count_down)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

# Initializes the program and executes functions as they are called
if __name__ == "__main__":
    exec_thread()
