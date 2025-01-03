from typing import Tuple, List, Union

# Typing Variable 
a: int = 1
b: str = 'ABCD'
c: list = [1, 2, 3]

#변수의 타입 지정방식.
some_list: List[str] = ['a', 'b', 'c']
some_tuple: Tuple[str, int, int] = ('a', 1, 2)


# Typing function
def add(a: int, b: int) -> int:
    return a - b

#input과 return 값의 변수 타입이 int 이거나 float 일 수 있음을 타입힌트를 통해 알수있다.
def n_times(a: Union[int, float], b: List[int]) -> List[Union[int, float]] :
    return [a * elem for elem in b]
