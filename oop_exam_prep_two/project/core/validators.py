class Validator:
    @staticmethod
    def raise_if_string_shorter_than_value(string, value, message):
        if len(string) < value:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_not_in_range(value, min_value, max_value, message):
        if value < min_value or value > max_value:
            raise ValueError(message)

    # @staticmethod
    # def raise_if_string_is_empty_or_whitespace(string, message):
    #     if string.strip() == '':
    #         raise ValueError(message)