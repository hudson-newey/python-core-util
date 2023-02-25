from typing import Callable

def executionTime(function: Callable) -> float:
    def f():
        function()
        return 0
    return f()
