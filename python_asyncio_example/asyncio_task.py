import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    # 코루틴을 태스크로 감싸 이벤트 루프에 등록과 동시에 실행 시작 (task1, task2 동시 실행)
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))
    
    # main 함수는 계속 실행되므로 아래 시간이 먼저 출력됨
    print(f"started at {time.strftime('%X')}")

    # task1과 task2가 완료될 때까지 대기 (병렬 실행으로 총 2초 소요)
    await task1 
    await task2

    print(f"finished at {time.strftime('%X')}")

# 1. 직접 실행하면 __name__ 은 __main__ 이라는 값을 갖게됨
# 2. 직접 실행되지 않은 import된 모듈은 모듈의 이름(파일명)을 갖게됨.
if __name__ == "__main__": 
    asyncio.run(main())
    
    
    
'''

결과 :

started at 23:00:04
hello
world
finished at 23:00:06

'''  