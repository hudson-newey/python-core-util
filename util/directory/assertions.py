def pathExists(path: str) -> bool:
    from os.path import exists
    return exists(path)

def isFile(path: str) -> bool:
    pass

def isFolder(path: str) -> bool:
    pass

def hasExtension(path: str, extension: str) -> bool:
    return path.split(".").pop() == extension
