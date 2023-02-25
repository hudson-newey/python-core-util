def throwError(errorCode = 1, errorMessage = "An unknown error has occurred..."):
    raise Exception(f"[ERROR] {errorCode}: {errorMessage}")
