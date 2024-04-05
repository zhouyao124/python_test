from threading import Thread


def task(count: int):
    for i in range(count):
        print(i, end='\n')


t1 = Thread(target=task, args=(12,))
t2 = Thread(target=task, args=(13,))

t1.start()
t2.start()

t1.join()
t2.join()

print("end process")
