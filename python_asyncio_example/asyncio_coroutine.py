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

if __name__ == "__main__": # 직접 실행하면 __name__ 은 __main__ 이라는 값을 갖게됨
    asyncio.run(main()) # run loop를 만들어서 main()코루틴을 실행

    
'''

결과 :

started at 22:59:51
hello
world
finished at 22:59:54

'''  