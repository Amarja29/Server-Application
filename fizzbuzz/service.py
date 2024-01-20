def fizz_buzz_logic(number, int1, int2, str1, str2):
    result = ""
    if number % int1 == 0:
        result += str1
    if number % int2 == 0:
        result += str2
    return result or str(number)