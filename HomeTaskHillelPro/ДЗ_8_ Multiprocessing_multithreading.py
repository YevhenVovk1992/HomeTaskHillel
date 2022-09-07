import time

from threading import Thread
from multiprocessing import Process, Queue


part1 = [200000, 300000]
part2 = [500000, 600000]
part3 = [100000, 200000]
part4 = [800000, 900000]


class ThreadWithResult(Thread):
    """
    Change the class to display the result of the function calculation
    """
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.get_result = target(*args, **kwargs)

        super().__init__(group=group, target=function, name=name, daemon=daemon)


class MultiprocessorWithResult:
    """
    Change the class to display the result of the function calculation
    """
    def __init__(self):
        self.processes = []
        self.queue = Queue()

    @staticmethod
    def _wrapper(func, queue, args, kwargs):
        ret = func(*args, **kwargs)
        queue.put(ret)

    def run(self, func, *args, **kwargs):
        args2 = [func, self.queue, args, kwargs]
        p = Process(target=self._wrapper, args=args2)
        self.processes.append(p)
        p.start()

    def wait(self):
        rets = []
        for p in self.processes:
            ret = self.queue.get()
            rets.append(ret)
        for p in self.processes:
            p.join()
        return rets[0]


def draw_line() -> None:
    """
    Draw a line
    :return: None
    """
    print(''.join(['-' for _ in range(90)]))


def is_happy_ticket(num: int) -> bool:
    """
    Check number of the ticket
    :param num: number of the ticket
    :return: True if happy ticket
    """
    sum_left_part = sum(int(i) for i in str(num)[:3])
    sum_right_part = sum(int(i) for i in str(num)[3:])
    return True if sum_left_part == sum_right_part else False


def get_happy_ticket(limit_range: list) -> list:
    """
    Create the list of the numbers in the range
    :param limit_range: minimum and maximum of the range
    :return: list of the numbers
    """
    result = []
    for number in [i for i in range(limit_range[0], limit_range[1] + 1)]:
        if is_happy_ticket(number):
            result.append(number)
    return result


def run_4_threads_mod(*args) -> None:
    jobs = []
    start = time.time()
    for i in args:
        thread = ThreadWithResult(target=get_happy_ticket, args=(i,))
        jobs.append(thread)
        thread.start()
    for proc in jobs:
        proc.join()
    end = time.time()
    print('4 threads with result end with time:', end - start)
    for i, res in enumerate(jobs):
        print(f'In the range {args[i]} {len(res.get_result)} lucky tickets')




def run_4_threads() -> None:
    start = time.time()
    thread1 = Thread(target=get_happy_ticket, args=(part1,))
    thread2 = Thread(target=get_happy_ticket, args=(part2,))
    thread3 = Thread(target=get_happy_ticket, args=(part3,))
    thread4 = Thread(target=get_happy_ticket, args=(part4,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    end = time.time()
    print('4 threads end with time:', end - start)


def run_4_processes() -> None:
    start = time.time()
    p1 = Process(target=get_happy_ticket, args=(part1,))
    p2 = Process(target=get_happy_ticket, args=(part2,))
    p3 = Process(target=get_happy_ticket, args=(part3,))
    p4 = Process(target=get_happy_ticket, args=(part4,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end = time.time()
    print('4 processes end with time:', end - start)


def run_4_processes_mod(*args) -> None:
    jobs = []
    results = []
    start = time.time()
    for i in args:
        p = MultiprocessorWithResult()
        jobs.append(p)
        p.run(get_happy_ticket, i)
    for proc in jobs:
        results.append(proc.wait())
    end = time.time()
    print('4 threads with result end with time:', end - start)
    for i, res in enumerate(results):
        print(f'In the range {args[i]} {len(res)} lucky tickets')


def run_single_threaded(*args) -> None:
    start = time.time()
    for i in args:
        get_happy_ticket(i)
    end = time.time()
    print('single threaded end with time:', end - start)


def main():
    run_single_threaded(part1, part2, part3, part4)
    draw_line()
    run_4_threads()
    draw_line()
    run_4_threads_mod(part1, part2, part3, part4)
    draw_line()
    run_4_processes()
    draw_line()
    run_4_processes_mod(part1, part2, part3, part4)


if __name__ == '__main__':
    main()
