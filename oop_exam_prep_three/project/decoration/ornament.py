from project_one.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self):
        super().__init__(1, 5)


# ornament = Ornament()
# print(ornament.price)
# print(ornament.__class__.__name__)