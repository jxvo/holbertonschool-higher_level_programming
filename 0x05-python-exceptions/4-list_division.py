#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_results = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except:
            div = 0
        finally:
            list_results.append(div)
    return list_results
