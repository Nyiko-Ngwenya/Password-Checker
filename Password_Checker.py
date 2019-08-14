import re

def password_is_valid(password):
    if password is not None :
        if len(password) > 8:
            pattern = re.compile(r'[a-z]')
            if pattern.search(password):
                pattern = re.compile(r'[A-Z]')
                if pattern.search(password):
                    pattern = re.compile(r'\d')
                    if pattern.search(password):
                        return True 
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
def password_is_ok(password):
    ok_count = 0
    if password is not None :
        ok_count+=1
    else:
        return False
    if len(password) > 8:
        ok_count+=1
    else:
        return False
    pattern = re.compile(r'[a-z]')
    if pattern.search(password):
        ok_count+=1
    pattern = re.compile(r'[A-Z]')
    if pattern.search(password):
        ok_count+=1
    pattern = re.compile(r'\d')
    if pattern.search(password):
        ok_count+=1
    if ok_count >= 3:
        return True
    else:
        return False
    