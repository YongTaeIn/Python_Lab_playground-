# Python 데코레이터 (Decorator) 이해하기

## 📚 개요

이 폴더는 Python의 **데코레이터(Decorator)** 개념을 단계별로 이해하기 위한 예제 코드를 포함하고 있습니다.

## 🎯 데코레이터란?

데코레이터는 **기존 함수의 코드를 수정하지 않고** 새로운 기능을 추가할 수 있게 해주는 Python의 강력한 기능입니다.

### 핵심 개념
- 함수를 입력으로 받아서, 새로운 기능이 추가된 함수를 반환
- 코드의 재사용성과 가독성을 높임
- `@` 기호를 사용하여 간단하게 적용 가능

## 📝 학습 순서

### 1단계: 기본 함수 이해
```python
def hello():
    print("hello")
```
- 가장 단순한 함수
- "hello"를 출력하는 기능만 수행

### 2단계: 데코레이터 함수의 원리
```python
def deco(fn):
    def deco_hello():
        print("*" * 20)  # 전처리
        fn()             # 원래 함수 실행
        print("*" * 20)  # 후처리
    return deco_hello

deco_hello = deco(hello)
deco_hello()
```

**작동 원리:**
1. `deco()` 함수는 다른 함수(`fn`)를 매개변수로 받음
2. 내부에 새로운 함수(`deco_hello`)를 정의
3. 새로운 함수는 원래 함수의 앞뒤에 추가 기능을 붙임
4. 새로운 함수를 반환

**결과:**
```
********************
hello
********************
```

### 3단계: @ 문법 사용
```python
@deco
def hello2():
    print("hello 2")

hello2()
```

**이해하기:**
- `@deco`는 `hello2 = deco(hello2)`와 완전히 동일
- 함수 정의 위에 `@데코레이터이름`을 붙이면 자동으로 적용
- 더 깔끔하고 읽기 쉬운 코드

## 💡 실제 사용 예시

### 실행 시간 측정
```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"실행 시간: {end - start}초")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("작업 완료")

slow_function()
# 출력:
# 작업 완료
# 실행 시간: 2.001초
```

### 로그 기록
```python
def logger(func):
    def wrapper():
        print(f"[LOG] {func.__name__} 함수 실행 시작")
        func()
        print(f"[LOG] {func.__name__} 함수 실행 종료")
    return wrapper

@logger
def process_data():
    print("데이터 처리 중...")

process_data()
# 출력:
# [LOG] process_data 함수 실행 시작
# 데이터 처리 중...
# [LOG] process_data 함수 실행 종료
```

### 권한 체크
```python
def require_admin(func):
    def wrapper(user):
        if user.get("role") == "admin":
            func(user)
        else:
            print("관리자 권한이 필요합니다.")
    return wrapper

@require_admin
def delete_user(user):
    print(f"{user['name']} 삭제 완료")
```

## 🔑 핵심 정리

| 항목 | 설명 |
|------|------|
| **목적** | 함수에 추가 기능을 붙이기 |
| **장점** | 코드 재사용, 가독성 향상, 관심사 분리 |
| **문법** | `@decorator_name` |
| **원리** | 함수를 감싸는(wrap) 고차 함수 |



## 📂 파일 구조

```
decorator/
├── README.md           # 영어 문서
├── README.ko.md        # 한글 문서 (이 파일)
└── example_1.ipynb     # 기본 데코레이터 예제
```

## 🔗 참고 자료
- [위키독스 - 데코레이터](https://wikidocs.net/160127)
- [Python 공식 문서 - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 - Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

**학습 팁:** 각 예제를 직접 실행해보고, 데코레이터를 제거했을 때와 비교해보면 이해가 더 잘 됩니다! 🎓

