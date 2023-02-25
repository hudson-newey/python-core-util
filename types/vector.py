# do not use this, this is just a template for more advanced types that are not duplicates of a list
class Vector:
    vectorType: type
    content: list[vectorType]

    def __init__(self, t: type) -> type:
        self.vectorType = t
        self.content = list(self.vectorType)
        return self.content

    def append(self, item: vectorType) -> list[vectorType]:
        self.content.append(item)
        return self.content

    def pop(self) -> vectorType:
        self.content.pop()
