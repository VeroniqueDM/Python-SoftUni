class Validator:
    SET_PLAYER_NAMES = set()
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_zero_or_negative(value, message):
        if value<=0:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_less_than_minimum(value, minimum, message):
        if value < minimum:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_not_in_range(value, minimum, maximum, message):
        if value < minimum or value > maximum:
            raise ValueError(message)
    @staticmethod
    def check_if_name_is_unique(name, message):
        if name in Validator.SET_PLAYER_NAMES:
            raise Exception(message)
        Validator.SET_PLAYER_NAMES.add(name)



