from project_one.decoration.ornament import Ornament
from project_one.decoration.plant import Plant


class DecorationFactory:
    decoration_types={
        'Ornament': Ornament,
        'Plant': Plant,
    }
    @staticmethod
    def create_decoration( decoration_type: str):
        if decoration_type in DecorationFactory.decoration_types:
            return DecorationFactory.decoration_types[decoration_type]()
        return "Invalid decoration type."


