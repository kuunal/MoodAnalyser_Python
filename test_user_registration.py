from user_registration import UserRegistrationRegex 

class TestUserRegistration:

    def test_given_first_name_when_valid_returns_object(self):
        user_registration = UserRegistrationRegex()
        is_valid = user_registration.validate_first_name("Kunal")
        assert is_valid != None

        
    def test_given_first_name_when_valid_returns_none(self):
        user_registration = UserRegistrationRegex()
        is_valid = user_registration.validate_first_name("ku")
        assert is_valid == None