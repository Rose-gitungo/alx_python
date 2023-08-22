def raise_exception_msg(message=""):
    try:
        message="C is fun"
    except NameError as message:
        print(message)

    return