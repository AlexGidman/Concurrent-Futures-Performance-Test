# Concurrent Futures Performance Test

Tests a linear processing approach using a for loop vs using a multithreaded approach with the 
concurrent.futures module in Python.

## Tests:

• I/O Bound functions: opens file, writes to file, closes file.

• CPU Bound functions: simulated CPU tasks using sleep function

## Conclusion:

Multithreading using concurrent futures is faster that linear approaches to processing.
However, asynchronous processing can cause its own problems, and there may still be a
bottleneck on efficiency if synchronous tasks are dependent on completion of all asynchronous
tasks.
