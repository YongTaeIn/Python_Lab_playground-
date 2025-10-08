# Python Asyncio (Asynchronous Programming Library)

<div align="right">

[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

- **Definition**: Python standard library that supports asynchronous programming based on **event loop**
    - **What is Event Loop?**: A control structure (scheduler) that manages tasks (coroutines, tasks, callbacks, etc.) to execute in an asynchronous program and alternately runs ready tasks
- **Function**: Asyncio is a **powerful tool for asynchronous I/O and concurrency** that helps handle multiple asynchronous tasks simultaneously in a single-thread environment
- **Analogy**:
    - Event Loop: Scheduler/Supervisor
    - Coroutine: Workers

## [Why Do We Need Asyncio?]

- **Purpose**: The benefit of using threads is not computation time but blocking I/O wait time. In other words, we only need to worry about blocking I/O, but threading requires too much knowledge → asyncio was created for this purpose.
- **Conclusion**: A way to implement concurrency without using threads
- **Additional Terms**:
    - **Computation Speed** (CPU-bound tasks):
        - Definition: Time taken for CPU to actually calculate
        - Examples: Encoding, multiplication operations, etc.
    - **I/O Wait Time** (I/O-bound tasks):
        - Definition: Time waiting for external device or network response, not CPU calculation
        - Examples: Reading files from disk, fetching data from DB, sending HTTP requests and waiting, etc.
        - In other words: Time waiting for external resources while CPU is idle

## [Basic Syntax Summary]

- **async**:
    - **Definition**: A library for calling functions asynchronously. Adding async makes the function asynchronous. Functions with async are called **'coroutines'**.
    - **Function**: Calling a function declared with `async def` does not execute the code but **only returns a coroutine object**.
    - Example:
        
        ```python
        import asyncio
        
        async def sleep():
            await asyncio.sleep(1)
        ```
        

- **await**:
    - **Definition**: A keyword that can only be used inside asynchronous functions (coroutines) defined with `async def`, **waits until awaitable task completes**
    (Can't move to next code line and waits, but control is transferred to event loop)
    - **Function**: Temporarily suspends execution until specific asynchronous task (coroutine, awaitable object) completes, and gives control to event loop to allow other tasks (coroutines, tasks, etc.) to run
    - Example:
        
        ```python
        async def main():
            result1 = await sum("A", [1, 2])   # Wait here until complete
            result2 = await sum("B", [1, 2, 3])# Start execution after A completes
            print(result1, result2)
        ```
        

- **create_task()**
    - **Definition**: Creates a coroutine as a Task, registers it with event loop + executes immediately.
        - Event Loop: Manager (responsible for scheduling coroutine execution - manages to-do list as queue)
    - **Function**: Creates and **executes** a task object using the returned object.
    - Example:
        
        ```python
        async def main():
        
        		# At the moment create_task is called, sum("A") and sum("B") are simultaneously registered with event loop and start execution.
            task1 = asyncio.create_task(sum("A", [1, 2]))
            task2 = asyncio.create_task(sum("B", [1, 2, 3]))
        
            result1 = await task1
            result2 = await task2
            print(result1, result2)
        
        ```
        

- **wait_for**
    - **Definition**: Function to set time limit (timeout) while executing specific coroutine (or task)
    - **Function**: Set time limit for asynchronous tasks, purpose is to prevent infinite wait state
    - Example:
        
        ```python
        # Returns normal result if completes within 3 seconds, raises TimeoutError if exceeds 3 seconds
        result = await asyncio.wait_for(coroutine, timeout=3)
        ```
        
- **run**
    - **Definition**: asyncio.run() is a function to start asynchronous program (entry point for coroutine execution).
    - **Function**: Creates event loop → executes coroutine → runs until complete → returns result → closes loop.
    - Example:
        
        ```python
        asyncio.run(main())
        ```
        

→ Add understanding with actual code (refer to https://kdw9502.tistory.com/6)

## [Coroutine Example vs Task Example]

- Note:
1. With create_task, await remembers that something is being executed and waits for it.
2. Without create_task, await really waits for the line until it completes.
3. However, await doesn't move in code line but doesn't hold the CPU - **it gives control to event loop so other coroutines can execute.**

- Coroutine
    
    ```python
    import asyncio
    import time
    
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)
    
    async def main():
        print(f"started at {time.strftime('%X')}")
    
        await say_after(1, 'hello')
        await say_after(2, 'world')
    
        print(f"finished at {time.strftime('%X')}")
    
    asyncio.run(main())
    
    if __name__ == "__main__": # __name__ becomes __main__ when executed directly
        asyncio.run(main()) # Create run loop and execute main() coroutine
    
        
    '''
    
    Result:
    
    started at 22:59:51
    hello
    world
    finished at 22:59:54
    
    '''  
    ```
    

- Task
    
    ```python
    import asyncio
    import time
    
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)
    
    async def main():
    		# Wraps coroutine as task, registers with event loop and starts execution simultaneously (both task1, task2)
        task1 = asyncio.create_task(
            say_after(1, 'hello'))
    
        task2 = asyncio.create_task(
            say_after(2, 'world'))
    		
    		# Since main function continues execution, time below prints first (timers set above)
        print(f"started at {time.strftime('%X')}")
    
        
        # Remember that task1 exists until executed task1 returns (completes). (prevents cancellation midway)
        await task1 
        await task2
    
        print(f"finished at {time.strftime('%X')}")
    
    # 1. __name__ becomes __main__ when executed directly
    # 2. Imported modules not directly executed have module name (file name).
    if __name__ == "__main__": 
        asyncio.run(main())
        
        
        
    '''
    
    Result:
    
    started at 23:00:04
    hello
    world
    finished at 23:00:06
    
    '''  
    ```
    

## [Difference Between Threads and Asyncio]

- **Threads**: CPU computation parallelization doesn't work due to GIL, only beneficial for overlapping I/O waits. But has high context switching costs and issues like race conditions and deadlocks. (Same problems occur even with multithreading)
- **Asyncio**: Single thread + event loop based → provides concurrency much lighter, optimized for I/O-bound tasks.

## Reference Sources
- https://wikidocs.net/125092
- https://kdw9502.tistory.com/6
- https://inpa.tistory.com/entry/👩‍💻-multi-process-multi-thread

