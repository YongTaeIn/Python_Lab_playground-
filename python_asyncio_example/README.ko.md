# Asyncio (파이썬에서 비동기 프로그래밍을 지원하는 라이브러리)

<div align="right">

[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

- **정의** : **이벤트 루프 기반** 비동기 프로그래밍을 지원하는 파이썬 표준 라이브러리
    - **이벤트 루프란?** : 비동기 프로그램에서 실행할 작업(코루틴,태스크,콜백 등)을 관리하고, 준비된 작업을 번갈아 실행하는 제어 구조(스케줄러)
- **기능** : asyncio는 단일 스레드 환경에서 여러 비동기 작업을 동시에 처리하도록 도와주는 **비동기 I/O와 동시성 처리를 위한 강력한 도구**
- **비유** : 
    - 이벤트 루프 : 스케쥴러/감독관
    - 코루틴 : 작업자들

## [왜 asynio 가 필요한가?]

- **목적** : 쓰레드를 사용으로 얻는 이점은 연산시간이 아닌 Blocking I/O 대기시간임. 즉, Blocking I/O 만 신경쓰면 되는데, 쓰레딩은 너무 많은 지식들을 요구함 → 이를 위해 asyncio가 나옴.
- **결론** : 쓰레드를 쓰지 않고도 동시성을 구현하는 방식
- **추가 용어** :
    - **연산 속도**(CPU-bound 작업) :
        - 정의 : CPU가 실제로 계산하는 데 걸리는 시간
        - 예시 : 인코딩, 곱셈 연산 등.
    - **I/O 대기 시간** (I/O-bound 작업) :
        - 정의 : CPU가 계산하는 게 아니라, 외부 장치나 네트워크의 응답을 기다리는 시간
        - 예시 : 파일을 디스크에서 읽기, DB에서 데이터 가져오기, HTTP 요청 보내고 기다리기 등등)
        - 즉 : CPU는 한가한데, 외부 자원 때문에 기다려야 하는 시간

## [기본 문법 정리]

- **async**  :
    - **정의** : 함수를 비동기로 호출하기 위한 라이브러리로, async 추가하면 이함수는 비동기가 됨. async가 적용된 함수를 **'코루틴'** 이라고 함.
    - **기능** : async def로 선언 된 함수를 호출하면, 코드가 실행 되지 않고 코루틴 **객체를 리턴하기만 할 뿐**임.
    - 예시
        
        ```python
        import asyncio
        
        async def sleep():
            await asyncio.sleep(1)
        ```
        

- **await** :
    - **정의** : await는 async def로 정의된 비동기 함수(코루틴) 내부에서만 사용할 수 있는 키워드로, 비동기 함수에서 **awaitable 작업이 끝날 때까지 대기**하는 키워드 
    (다음 코드 line으로 못넘어가고 기다히지만, 이벤트 루프의 제어권으로 들어감.)
    - **기능** : 특정 비동기 작업(코루틴, awaitable객체)이 끝날 때까지 실행을 일시 중지하고, 그동안 이벤트 루프에게 제어권을 넘겨 다른 작업(코루틴, 태스크 등)이 실행할 기회를 줌)
    - 예시
        
        ```python
        async def main():
            result1 = await sum("A", [1, 2])   # 여기서 끝날 때까지 대기
            result2 = await sum("B", [1, 2, 3])# A 끝난 후 실행 시작
            print(result1, result2)
        ```
        

- **create_task()**
    - **정의** : 코루틴을 Task로 만들어 이벤트 루프에 등록하고 + 즉시 실행함.
        - 이벤트 루프 :  관리자 (코루틴 실행 스케줄링 담당-할 일 목록을 큐로 관리)
    - **기능** : 반환된 객체를 가지고 비동기 작업 객체인 태스크를 만들고, **실행함.**
    - 예시
        
        ```python
        async def main():
        
        		# create_task를 호출하는 순간, sum("A")와 sum("B")가 동시에 이벤트 루프에 등록돼서 실행 시작됨.
            task1 = asyncio.create_task(sum("A", [1, 2]))
            task2 = asyncio.create_task(sum("B", [1, 2, 3]))
        
            result1 = await task1
            result2 = await task2
            print(result1, result2)
        
        ```
        

- **wait_for**
    - **정의** : 특정 코루틴(혹은 태스크)를 실행하면서 시간 제한(timeout)을 두는 기능
    - **기능** : 비동기 작업에 시간 제한 설정, 무한 대기 상태를 방지하는 목적
    - 예시 :
        
        ```python
        # 3초 안에 끝나면 정상적인 결과 반환, 3초 초과시 timeoutError 발생
        result = await asyncio.wait_for(코루틴, timeout=3)
        ```
        
- **run**
    - **정의** : asyncio.run() 은 비동기 프로그램을 시작하는 함수 (코루틴 실행용 진입점).
    - **기능** : 이벤트 루프를 만들고 → 코루틴을 실행하고 → 끝날 때까지 돌리고 → 결과를 반환하며 → 루프를 닫음.
    - 예시
        
        ```python
        asyncio.run(main())
        ```
        

→ 실제 코드로 이해하는거 추가하기 (https://kdw9502.tistory.com/6 참고)

## [코루틴 예시 vs 태스크 예시]

- 주의 : 
1. create_task가 있으면 await 입장에서는 수행되고 있는게 있다는걸 기억하며 기다리는거임.
2. create_task가 없으면 awiat는 진짜 그게 끝나기 전까지 line을 기다리는 거임.
3. 하지만 await 는 코드line 에서는 이동하지 않지만, cpu를 붙잡고 있는게 아니라 **제어권을 이벤트 루프에 넘겨 다른 코루틴이 실행될 수 있게 함.**

- 코루틴
    
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
    
    if __name__ == "__main__": # 직접 실행하면 __name__ 은 __main__ 이라는 값을 갖게됨
        asyncio.run(main()) # run loop를 만들어서 main()코루틴을 실행
    
        
    '''
    
    결과 :
    
    started at 22:59:51
    hello
    world
    finished at 22:59:54
    
    '''  
    ```
    

- 태스크
    
    ```python
    import asyncio
    import time
    
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)
    
    async def main():
    		# 코루틴을 태스크로 감싸 이벤트 루프에 등록과 동시에 실행 시작 됨.(task1,task2둘다)
        task1 = asyncio.create_task(
            say_after(1, 'hello'))
    
        task2 = asyncio.create_task(
            say_after(2, 'world'))
    		
    		# main 함수는 계속 실행됨으로, 아래 시간이 먼저 출력됨 (위에는 타이머걸림)
        print(f"started at {time.strftime('%X')}")
    
        
        # 위에서 수행한 task1이 return(종료) 할때 까지 task1이 있다는걸 알고있어라.(도중에 취소 방지) 
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
    ```
    

## [스레드와 asyncio 차이]

- **스레드**: GIL 때문에 CPU 연산 병렬화는 안 됨, I/O 대기 겹치기용으로만 이득 있음. 하지만 컨텍스트 스위칭 비용 크고, 레이스 컨디션·데드락 같은 문제 있음. (멀티스레드로 하여도 동일한 문제 발생)
- **asyncio**: 단일 스레드 + 이벤트 루프 기반 → 훨씬 가볍게 동시성 제공, I/O 바운드 작업에 최적화됨.

## 참고자료 출처
- https://wikidocs.net/125092
- https://kdw9502.tistory.com/6
- https://inpa.tistory.com/entry/👩‍💻-multi-process-multi-thread
