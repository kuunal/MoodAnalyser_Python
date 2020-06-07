import re

class UserRegistrationRegex:
    first_name_pattern = "^[A-Z][a-z]{2,}$"

    def validate_first_name(self, first_name):
        is_valid = re.match(self.first_name_pattern,first_name)
        return is_valid