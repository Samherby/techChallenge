def is_length_valid(string_to_test, max_length, is_mandatory):
    if len(str(string_to_test)) > max_length:
        return False
    if is_mandatory and len(str(string_to_test)) == 0:
        return False
    return True


def is_numeric(value):
    return str(value).isnumeric()


def is_number_valid(string_to_test, max_length, is_mandatory):
    print(string_to_test)
    if not is_length_valid(string_to_test, max_length, is_mandatory):
        return False
    return is_numeric(string_to_test)


def is_character_valid(string_to_test, max_length, is_mandatory):
    if not is_length_valid(string_to_test, max_length, is_mandatory):
        return False

    return string_to_test.isalpha()
