from tinydb import TinyDB, Query


db = TinyDB('db.json')
index_1 = db.insert({'type': 'apple', 'count': 7})
index_2 = db.insert({'type': 'peach', 'count': 3})

print(index_1, index_2)
