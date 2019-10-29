# https://docs.python.org/3.5/library/typing.html

# This module supports type hints as specified by PEP 484. The most fundamental support consists of the types Any, 
# Union, Tuple, Callable, TypeVar, and Generic. For full specification please see PEP 484. For a simplified 
# introduction to type hints see PEP 483.

# The function below takes and returns a string and is annotated as follows:
def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('Sam'))

def sum(a: int, b: int) -> int:
    return a + b

print('a + b = ', sum(10, 20))

def arrSum(arr: List[int]) -> List[int]:
    return arr