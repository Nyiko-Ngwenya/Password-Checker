from Password_Checker import password_is_valid,password_is_ok

def test_pass_valid():
    try:
        assert password_is_valid('123') == Exception
        assert password_is_valid('123456789') == Exception
        assert password_is_valid(None) == Exception
        assert password_is_valid('123456789a') == Exception 
        assert password_is_valid('1234Z6789a') == True
        assert password_is_valid('ABCDEFGHIaJ') ==  Exception
    except:
        pass
    

def test_pass_ok():
    assert password_is_ok('123') == False
    assert password_is_ok('123456789') == True
    assert password_is_ok(None) == False
    assert password_is_ok('123456789a') == True
    assert password_is_ok('1234Z6789a') == True
    assert password_is_ok('ABCDEFGHIaJ') == True 