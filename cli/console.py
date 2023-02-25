def clearConsole() -> None:
    from os import system, name
    if name == 'nt': system('cls')
    else: system('clear')

def runCommand(command: str):
    from os import system
    return system(command)
