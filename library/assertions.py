def pipInstalled(name) -> bool:
    try:
        eval(f"import {name}")
    except:
        return False
    return True
