class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_zero_or_negative(value, message):
        if value<=0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number, min_val, max_val, message):
        if number<min_val or number>max_val:
            raise ValueError(message)