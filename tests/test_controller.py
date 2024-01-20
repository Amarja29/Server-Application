from fizzbuzz.controller import fizz_buzz_controller

def test_fizz_buzz_controller():
    result = fizz_buzz_controller(3, 5, 15, 'fizz', 'buzz')
    assert len(result) == 15

    # Test with custom values
    result = fizz_buzz_controller(2, 7, 20, 'foo', 'bar')
    assert len(result) == 20
    assert result == ['1', 'foo', '3', 'foo', '5', 'foo', 'bar', 'foo', '9', 'foo', '11', 'foo', '13', 'foobar', '15',
                      'foo', '17', 'foo', '19', 'foo']

    # Test with larger limit
    result = fizz_buzz_controller(3, 5, 30, 'fizz', 'buzz')
    assert len(result) == 30
    assert result == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14',
                      'fizzbuzz', '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz', '26', 'fizz',
                      '28', '29', 'fizzbuzz']

    # Test with custom strings
    result = fizz_buzz_controller(2, 5, 10, 'hello', 'world')
    assert len(result) == 10
    assert result == ['1', 'hello', '3', 'hello', 'world', 'hello', '7', 'hello', 'world', 'hello']

    # Test with prime numbers
    result = fizz_buzz_controller(17, 23, 17, 'prime', 'numbers')
    assert len(result) == 17
    assert result == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', 'prime']