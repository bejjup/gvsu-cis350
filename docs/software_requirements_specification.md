# Functional Requirements

1. General
    1. The game shall have multiple levels.
    2. The game shall have a coin system.
    3. The game shall count up coins based on the correct placement of flags.
       
2. Flags
    1. Flags shall be interactable/placable by the player.
    2. Flags shall be removedable by the player.
    3. Flags shall have a set amount.
    4. The amount of flags shall decrement after being placed down.

3. Grid
    1. Squares on grid shall be proportional to each other.
    2. Grid squares shall not show the mines underneath.
    3. 2 mines shall not appear on the same square at the same time.

4. Endgame/Shop
   1. The endgame shall display a shop menu.
   2. The endgame shall occur after a level is completed.
   3. The shop shall take away a players coin count once an item is purchased.
   4. The shop menu must disappear when the next level is called.
   5. The shop menu must not be accessible during the game.

# Non-Functional Requirements
1. General
   1. The system shall scale easily to accommodate more potential items in the shop.
   2. The system shall prevent players from accessing the game's code.
   3. The system should be able to handle a large grid size without noticable lag.
   4. The game should respond to multiple screen sizes.
   5. Any text created by the game shall be in a font that is readable.
   6. The code shall be well documented.
   7. The game shall be avaliable 99% of the time.
   8. The game shall load within 2 seconds of starting.
   
2. Flags
    1. Flags shall be a different color than numbers.
    2. Flags shall not tell the user if there is a mine under it.
    3. The total flag amount shall not be able to be edited by the player.
       
3. Grid
   1. Grid shall be a neutral color for the players comfortability on the eyes.
   2. Numbers shall have clear color contrasts between elements in the game (including the numbers on the board, cleared vs uncleared spaces, and flags) to ensure players can visually understand distinctions between game elements allowing for ease of play.
   3. The background color shall be different than the grid color.
  
4. Endgame/Shop
   1. The endgame screen must be a different color than the background.
   2. The shop must have a different screen from the shop.
   
