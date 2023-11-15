from project_one.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration:BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        else:
            return False

    def find_by_type(self, decoration_type):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return "None"
