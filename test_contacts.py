from contacts_manager import validate_phone, validate_email

def test_phone():
    assert validate_phone("9876543210")[0] == True
    assert validate_phone("123")[0] == False

def test_email():
    assert validate_email("test@gmail.com") == True
    assert validate_email("test@com") == False

print("All tests passed!")
