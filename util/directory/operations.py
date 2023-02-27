def readFile(path: str) -> str or bool:
    with open(path, "r") as fp:
        return fp.readlines()


def writeToFile(path: str, contents: str) -> None:
    with open(path, "w") as fp:
        fp.write(contents)
        fp.close()


def appendToFile(path: str, contents: str = "") -> bool:
    with open(path, "a") as fp:
        fp.write(contents)
        fp.close()


def deletePath(path: str) -> bool:
    from shutil import rmtree

    try:
        rmtree(path)
    except:
        return False
    return True


def createFolder(path: str) -> bool:
    from os import mkdir

    try:
        mkdir(path)
    except:
        return False
    return True


def stripString(string: str) -> str:
    return string.replace("\n", "").replace("\r", "")
