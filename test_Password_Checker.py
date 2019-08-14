from Password_Checker import password_is_valid,password_is_ok

def test_pass_valid():
    assert password_is_valid('123') == False
    assert password_is_valid('123456789') == False
    assert password_is_valid(None) == False
    assert password_is_valid('123456789a') == False 
    assert password_is_valid('1234Z6789a') == True
    assert password_is_valid('ABCDEFGHIaJ') == False

def test_pass_ok():
    assert password_is_ok('123') == False
    assert password_is_ok('123456789') == True
    assert password_is_ok(None) == False
    assert password_is_ok('123456789a') == True
    assert password_is_ok('1234Z6789a') == True
    assert password_is_ok('ABCDEFGHIaJ') == True 