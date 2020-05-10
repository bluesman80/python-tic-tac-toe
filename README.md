# python-tic-tac-toe
Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

THIS LITTLE PYTHON CODE IS WRITTEN AS THE FINAL TASK OF "TIC-TAC-TOE" PROJECT IN JETBRAINS ACADEMY.

The program does the following.
1. Prints an empty field at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is OK.
3. Ends the game when someone wins or there is a draw.

## Example
The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
<pre>
---------
|       |
|       |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: > 2 2
This cell is occupied! Choose another one!
Enter the coordinates: > two two
You should enter numbers!
Enter the coordinates: > 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: > 1 3
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: > 3 1
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: > 1 2
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: > 1 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: > 3 2
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: > 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins
</pre>
