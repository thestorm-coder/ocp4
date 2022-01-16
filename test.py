from managers import player_manager as pm, tournament_manager as tm
from views import ListView, SelectItem


# print(list(filter(lambda x: x.rank > 2790, pm.find_all())))

# # def ma_fonction(x):
#     # return x.rank > 2790


# print(tm.find_all())
# ListView(title="List des joueurs", items=pm.find_all()).show()


print(SelectItem(title="GG", items=pm.find_all()).show())
