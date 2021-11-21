import json


class Manager:
    """il doit charger les données depuis json (désérialiser, transformer ces données en instances et rendre disponible
    ces instances"""
    def __init__(self, item_type):
        self.items = {}
        self.item_type = item_type

    def load_from_json(self, json_path):
        "charger le fichier json et le convertir grace au module json de python"
        "parcourir tous les dictionnaires de données dans la liste"
        "et pour chaque dicos instancier le modèle correspondant"
        with open(json_path) as file:
            data = json.load(file)
            for item_data in data:
                self.create(item_data)

    def create(self, data):
        """on instancie et on le stock dans nos items"""
        item = self.item_type(**data)
        self.items[item.id] = item
        return item

    def find_all(self):
        return list(self.items.values())

    def find_by_id(self, id):
        return self.items[id]
