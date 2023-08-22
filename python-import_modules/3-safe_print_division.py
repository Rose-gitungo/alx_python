def safe_print_division(a,b,result):
    try:
        print(a)
    except:
        b
    finally:
        print("inside result:",a/b)
        print('{:d}/{:d}={}'.format(a,b,result))
