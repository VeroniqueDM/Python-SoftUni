class Catalogue:

    def __init__(self, name:str):
        self.name = name
        self.products = []
    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str)
#        if s.startswith("a"):

        self.letter_list = []
        for items in self.products:
            if items[0] == first_letter:
                self.letter_list.append(items)
        return self.letter_list
    def __repr__(self):
        result = sorted(self.products)
        res = "\n".join(result)

        return f"""Items in the {self.name} catalogue:
{res}"""



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
