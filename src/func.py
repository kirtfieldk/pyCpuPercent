from tapestry import log_stats
import threading


def rando():
    for i in range(0, 1000):
        i += i
        i += 23


def randos(num):
    for i in range(1, num):
        i += i
        i += 23


@log_stats
def main():
    x = threading.Thread(target=randos, args=(10000,))
    y = threading.Thread(target=rando)
    y.start()
    x.start()
    y.join()
    x.join()


if __name__ == "__main__":
    try:
        main()
    except TypeError:
        print("Failed")
