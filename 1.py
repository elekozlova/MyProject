import json

def write_file(city) -> None:
    with open("db.json","r", encoding='utf-8') as db_file:
        db = json.load(db_file)
    db.append(city)
    with open("db.json", 'w', encoding='utf-8') as db_file:
        json.dump(db,db_file )

   


write_file("Лондон")
write_file("Минск")
write_file("Москва")



