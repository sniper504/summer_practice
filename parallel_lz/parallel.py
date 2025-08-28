import threading
import multiprocessing
import time
import random
import sys

def work(counter, arr, operations):
    for _ in range(operations):
        with counter.get_lock():
            idx = counter.value
            counter.value += 1
            arr[idx] = counter.value


class ParallelLab4:
    # Задание 1 
    def sync_counter(self):
        print("Задание 1: Синхронизированный счётчик")

        counter = 0
        lock = threading.Lock()

        def worker():
            nonlocal counter
            for _ in range(1000):
                with lock:
                    counter += 1

        threads = []
        for _ in range(10):
            t = threading.Thread(target=worker)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("Синхронизированный счётчик:", counter)

        # Без потоков
        counter2 = 0
        for _ in range(10 * 1000):
            counter2 += 1
        print("Обычный счётчик:", counter2)
        print()

    # Задание 2
    def shared_memory(self):
        print("Задание 2: Разделяемая память с Value и Array")

        num_processes = random.randint(2, 10)
        ops_list = [random.randint(100, 1000) for _ in range(num_processes)]
        total_ops = sum(ops_list)

        counter = multiprocessing.Value('i', 0)
        arr = multiprocessing.Array('i', total_ops)

        processes = [
            multiprocessing.Process(target=work, args=(counter, arr, ops))
            for ops in ops_list
        ]

        for p in processes:
            p.start()
        for p in processes:
            p.join()

        print("Количество процессов:", num_processes)
        print("Суммарное число операций:", total_ops)
        print("Итоговое значение счётчика:", counter.value)
        print()

    # Задание 3 
    def timeout_task(self):
        print("Задание 3: Ограничение времени выполнения (3 секунды)")

        stop_flag = {"stop": False}

        def timeout_handler():
            if not stop_flag["stop"]:
                print("Время выполнения превысило 3 секунды")
                sys.exit(1)

        timer = threading.Timer(3, timeout_handler)
        timer.start()

        try:
            time.sleep(random.randint(1, 5))
            stop_flag["stop"] = True
            print("Операция завершена вовремя")
        finally:
            timer.cancel()
