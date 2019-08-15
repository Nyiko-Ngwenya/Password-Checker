from Password_Checker import password_is_valid,password_is_ok
import pytest
def test_pass_valid():
    with pytest.raises(Exception):
        assert password_is_valid('12345') == Exception('Password is not longer than 8 characters')
        assert password_is_valid('123') == Exception('Password is not longer than 8 characters')
        assert password_is_valid('123456789') == Exception('Password doesnt contain a small letter')
        assert password_is_valid(None) == Exception('Password is null')
        assert password_is_valid('123456789a') == Exception('Password doesnt contain a capital letter')
        assert password_is_valid('1234Z6789a') == True
        assert password_is_valid('ABCDEFGHIaJ') ==  Exception('Password doesnt contain a number')

def test_pass_ok():
    assert password_is_ok('123') == False
    assert password_is_ok('123456789') == True
    assert password_is_ok(None) == False
    assert password_is_ok('123456789a') == True
    assert password_is_ok('1234Z6789a') == True
    assert password_is_ok('ABCDEFGHIaJ') == True 