from database import Database
from pokedex import Pokedex

poke = Pokedex()

poke.getPokemonByName("Pikachu")
poke.getPokemonByMultipliers(None)
poke.getPokemonWeaknessesByName("Pikachu")
poke.getPokemonIfHaveEvol()
poke.getPokemonsByType(["Ice", "fire"])