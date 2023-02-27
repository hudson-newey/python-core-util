from typing import Callable


def call(function: Callable):
    return function()


def doesFail(function: Callable) -> list[bool,]:
    try:
        functionReturnValue = function()
    except:
        return [False, False]
    return [True, functionReturnValue]
