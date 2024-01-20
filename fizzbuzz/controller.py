from .service import fizz_buzz_logic

def fizz_buzz_controller(int1, int2, limit, str1, str2):
    results = [fizz_buzz_logic(i, int1, int2, str1, str2) for i in range(1, limit + 1)]
    return results