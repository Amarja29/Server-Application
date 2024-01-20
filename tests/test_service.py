from fizzbuzz.service import fizz_buzz_logic

def test_fizz_buzz_logic():
    result = fizz_buzz_logic(3, 3, 5, 'fizz', 'buzz')
    assert result == 'fizz'

    # Test with multiples of 5
    result = fizz_buzz_logic(25, 3, 5, 'fizz', 'buzz')
    assert result == 'buzz'

    # Test with multiples of both 3 and 5
    result = fizz_buzz_logic(15, 3, 5, 'fizz', 'buzz')
    assert result == 'fizzbuzz'

    # Test with non-multiples
    result = fizz_buzz_logic(7, 3, 5, 'fizz', 'buzz')
    assert result == '7'

    # Test with custom strings
    result = fizz_buzz_logic(6, 2, 3, 'foo', 'bar')
    assert result == 'foobar'

    # Test with larger numbers
    result = fizz_buzz_logic(105, 3, 5, 'fizz', 'buzz')
    assert result == 'fizzbuzz'