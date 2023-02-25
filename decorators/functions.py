from typing import Callable

def void(function: Callable) -> None:
    def f():
        function()
        return None
    return f

def noError(function: Callable):
    def f():
        try: return function()
        except: pass
    return f()

def returnType(function: Callable, t: type):
    def f() -> t:
        return function()
    return f()

def recurseNTimes(function: Callable, times: int):
    global i
    i = 0

    def f():
        i += 1
        return function(function if i <= times else None)
    return f()
