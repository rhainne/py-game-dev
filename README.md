# Python Game Development

Repository to hold all my progress with the book Beginning Python Games Development, 2nd Edition by Harrison Kinsley and Will McGugan.

This repository also contains a couple of simple games that help to check the structure of a finished game:
- A version of the classic Tetris, made by Laria Carolin Chabowski
- A simple text based RPG made by Francesco Balducci

I will develop some little scripts to implement the lessons I learn and could be usefull in the future to make little games.

### Next Steps:
- Implement Item grabbing functionality
- Implement Inventory graphically
- Implement a basic Battle system
- Implement Battle HUD
- Implement Shopping HUD
- Implement and In-Game Menu (The classic character stats, wear, )
- Implement Shop.py and NPCs
- Implement Game Saving
- Add a Main Menu (Start Game, Load Game, Options, Quit)
- Implement the behaviour of Load Game
- Add Combat Skills in a file similar to Regions or Bestiary)
- Add NPCs to start working with some usable data


### Done tasks:

- Implement the behaviour of Quit, with confirmation (Done in MainMenu.py (method raise_warning_on_exit()))
- Implement the behaviour of Start Game(Done in MainMenu.py)
- Implement Map_data (Dictionary of Maps, using Map class structure) (Done in GlobeMaps.py)
- Implement Map system, maybe making each region clickable and zoomable (MapCollection.py and Map.py)
- Implement Colission system thinking also in reusability (Character.py implements collision check on move method
- Implement Inventory and Item classes (Done in Inventory.py)
- Precalculation of direction vectors in key_vector_movement.py script (Done in key_vector_mvmnt_opt.py)
- Classic movement of a sprite to the target using rotation and direction from source to target(mouse position)
- Think on reusable Stage maker(Stage, Shop, Location, Battleground)


### Resources
- Tiled Map Editor: http://www.mapeditor.org/
- Pygame tutorial by Eli Bendersky: http://eli.thegreenplace.net/tag/pygame-tutorial
- Character Sprite Generation: http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator/
