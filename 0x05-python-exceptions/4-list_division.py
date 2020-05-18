#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    results = []
    error = None
    while list_division and idx < list_length:
        try:
            results.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            error = "division by 0"
            results.append(0)
        except(TypeError, ValueError):
            error = "wrong type"
            results.append(0)
        except IndexError:
            error = "out of range"
            results.append(0)
        finally:
            if error is not None:
                print(error)
        error = None
        idx += 1
    return results
