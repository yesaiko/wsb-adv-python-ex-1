from car import Car
from services.collection import Collection
from services.save import Save

mycar = Car("Ford", 2006, 240000)
notmycaranymore = Car("Mazda", 2002, 320000)
othercar = Car("VW", 2010, 130000)
_collection = Collection()
_collection.add(mycar)
_collection.add(notmycaranymore)
_collection.add(othercar)

_save = Save("", "cars.data")
_save.serialize(_collection)

_collection_deserialized = _save.deserialize()

print("It shows all cars deserialized from cars.data pickle file")
_collection_deserialized.show()

[_collection_deserialized.delete(car) for car in _collection_deserialized.cars if car.mileage > 300000]

print("It will show all cars with mileage under 300k because we deleted all cars with mileage over 300k")
_collection_deserialized.show()