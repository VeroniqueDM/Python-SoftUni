import self as self


class Rule:
    def check_rule(self):
        pass

class HeaderRule(Rule):
    def __init__(self):
        pass
    def check_header(self):
        pass

    def check_rule(self):
        return self.check_header()

class IntegerRule(Rule):

    def __init__(self):
        pass
    def check_int_rule(self):
        pass
    def check_rule(self):
        return self.check_int_rule()
rules = (Rule(), HeaderRule(),IntegerRule())
class RuleEngine:
    def apply(self):
        for rule in rules:
            if not rule.check_rule():
                raise ValueError

    
