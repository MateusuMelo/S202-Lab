from database import Database as Data
from writeAJson import writeAJson

class Pokedex:
    def __init__(self):
        self.dataset = Data(database="pokedex", collection="pokemons")
        self.dataset.resetDatabase()

    def getPokemonByName(self, name: str):
        data = self.dataset.collection.find({"name": "Pikachu"})
        return writeAJson(data,name)
    
    def getPokemonsByType(self,types: list):
        data = self.dataset.collection.find({"type": {"$in": types}})
        return writeAJson(data, "pokemons_by_type")
    
    def getPokemonWeaknessesByName(self,name:str):
        data = self.dataset.collection.find({"name": "Pikachu"},{"weaknesses":1})
        return writeAJson(data,name)
    
    def getPokemonByMultipliers(self, flag):
        data = self.dataset.collection.find({"multipliers": flag})
        return writeAJson(data, "getPokemonByMultipliers")
    
    def getPokemonIfHaveEvol(self):
        data = self.dataset.collection.find({"next_evolution": {"$exists": True}})
        
        
