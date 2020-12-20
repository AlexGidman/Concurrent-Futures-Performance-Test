import tempfile
from time import perf_counter, sleep
import concurrent.futures

def io_write_to_file(item: bytes):
    '''IO based function that writes item to file'''
    temp = tempfile.TemporaryFile()
    # f = open(temp, 'w')
    temp.write(item)
    temp.close()

def cpu_operation():
    '''Simulates CPU operations'''
    sleep(0.5)

def test_io_operations(num_of_operations: int):
    '''Tests io_operations using linear and multithreaded approaches'''
    # FOR LOOP / LINEAR APPROACH
    t1 = perf_counter()

    [io_write_to_file(b'line') for i in range(num_of_operations)]

    print(f"IO: Linear takes {perf_counter()-t1}s")


    ## CONCURRENT FUTURES / MULTITHREAD APPROACH
    t1 = perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(io_write_to_file, range(num_of_operations))

    print(f"IO: Concurrent Futures takes {perf_counter() - t1}s")

def test_cpu_operations(num_of_operations: int):
    '''Tests io_operations using linear and multithreaded approaches'''
    # FOR LOOP / LINEAR APPROACH
    t1 = perf_counter()

    [cpu_operation() for i in range(num_of_operations)]

    print(f"CPU: Linear takes {perf_counter()-t1}s")


    ## CONCURRENT FUTURES / MULTITHREAD APPROACH
    t1 = perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        [executor.submit(cpu_operation) for i in range(num_of_operations)]

    print(f"CPU: Concurrent Futures takes {perf_counter() - t1}s")


def main():
    num_of_operations = pow(10, 4)
    test_io_operations(num_of_operations)
    num_of_operations = 10
    test_cpu_operations(num_of_operations)
    

if __name__ == '__main__':
    main()