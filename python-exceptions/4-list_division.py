#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            piece_1 = my_list_1[i] if len(my_list_1) else 0
            piece_2 = my_list_2[i] if len(my_list_2) else 0

            if not isinstance(piece_1, (int, float)) or not
            isinstance(piece_2, (int, float)):
                raise TypeError("wrong type")

            if piece_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = piece_1 / piece_2
            result.append(division_result)

        except TypeError as k:
            print(k)
            result.append(0)
        except ZeroDivisionError as k:
            print(k)
            result.append(0)
        except IndexError as k:
            print(k)
            print("out of range")
            result.append(0)

        finally:
            pass

    return result
