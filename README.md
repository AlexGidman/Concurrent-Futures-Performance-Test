# Concurrent Futures Performance Test
- Initally tests the speed for writing to a text file using a for loop vs using concurrent.futures: I/O Bound functions.
- It then adds a 'sleep' function to simulate CPU Bound functions. 
## Conclusion:
• In the case of file I/O a for loop seems faster
• In the case of CPU Bound tasks, concurrent futures is much faster
