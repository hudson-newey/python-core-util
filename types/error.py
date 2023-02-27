class ErrorType:
    _code: int
    _message: str
    _isFatal: bool

    def __init__(
        self, errorCode=1, errorMessage="Unknown error...", isFatal=True
    ) -> None:
        self.code = errorCode
        self.message = errorMessage
        self.isFatal = isFatal

    def throw(self) -> None:
        print(f"[Error] Runtime error, {self.code}")
        if self.isFatal:
            raise Exception(f"{self.message}...")
        print(self.message)

    def throwIf(self, condition) -> None:
        if condition:
            self.throw()

    def throwWhen(self, condition) -> None:
        async def observer():
            while True:
                self.throwIf(condition)

        observer()
