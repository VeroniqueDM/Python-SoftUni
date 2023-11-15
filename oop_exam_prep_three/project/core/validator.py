class Validator:

    @staticmethod
    def raise_if_empty_string(value, message):
        if value == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_less_or_equal_than_zero(value, message):
        if value <= 0:
            raise ValueError(message)