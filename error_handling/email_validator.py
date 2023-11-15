class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["bg", "com", "net", "org"]

while True:
    email_address = input()
    if email_address == "End":
        break
    if "@" not in email_address:
        raise MustContainAtSymbolError("Email must contain @")
    email_name, domain_name = email_address.split("@")
    if len(email_name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = domain_name.split(".")[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
