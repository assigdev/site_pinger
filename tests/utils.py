import functools


def cases(case_list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for case in case_list:
                new_args = args + (case,)
                try:
                    func(*new_args)
                except AssertionError:
                    print("Error in case: %s" % (case,))
                    raise
            return
        return wrapper
    return decorator
