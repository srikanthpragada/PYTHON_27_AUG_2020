from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print("Child", i)


def print_numbers():
    for i in range(1, 20):
        print(i)


t1 = PrintThread()
t1.start()
t2 = Thread(target=print_numbers)
t2.start()

for n in range(1, 20):
    print("Main ", n)
