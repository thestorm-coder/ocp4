import json
from tinydb import TinyDB
from tinydb.table import Document


class Manager:
    """il doit charger les données depuis json (désérialiser, transformer ces données en instances et rendre disponible
    ces instances"""
    def __init__(self, item_type):
        self.items = {}
        self.item_type = item_type
        db = TinyDB("chess.db", indent=4)
        self.table = db.table(name=self.item_type.__name__.lower()+"s")
        for item_data in self.table:
            self.create(**item_data)

    def save_item(self, id):
        """ cette class permet de sauvegarder l'item dans la base de données """
        item = self.find_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

    # def load_from_json(self, json_path):
    #     "charger le fichier json et le convertir grace au module json de python"
    #     "parcourir tous les dictionnaires de données dans la liste"
    #     "et pour chaque dicos instancier le modèle correspondant"
    #     with open(json_path) as file:
    #         data = json.load(file)
    #         for item_data in data:
    #             self.create(**item_data)

    def create(self, save=False, **data):
        """on instancie et on le stock dans nos items"""
        if "id" not in data:
            data["id"] = self.get_next_id()
        item = self.item_type(**data)
        self.items[item.id] = item
        if save:
            self.save_item(id=item.id)
        return item

    def get_next_id(self):
        try:
            return self.table.all()[-1].doc_id+1
        except IndexError:
            return 1

    def find_all(self):
        return list(self.items.values())

    def find_by_id(self, id):
        return self.items[id]
