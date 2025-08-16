
# Python-project




## Project - 1: Random Number Guessing Game
### Description: 
This is a number guessing game where the player has to guess a randomly selected number between 1 and 100 within a limited number of attempts based on the chosen difficulty level.

#### Algorithm:

1. Generate a random number between 1 and 100.

2. Ask the player to choose a difficulty level ('EASY' or 'HARD').
- EASY: Player gets 10 attempts.

- HARD: Player gets 5 attempts.

3. Loop until the player runs out of attempts:

- Prompt the player to guess the number.

- Decrement the number of remaining attempts.
- Check the player's guess:
    - If the guess is correct, print a success message and end the game.
    - If the guess is too high, prompt the player to guess lower.
    - If the guess is too low, prompt the player to guess higher.

4. If the player uses all attempts without guessing correctly, print a failure message.

<img width="674" height="684" alt="Screenshot 2025-08-13 180243" src="https://github.com/user-attachments/assets/1c6195d2-bee0-4cfd-bf68-913d32fd0f98" />

<img width="582" height="395" alt="Screenshot 2025-08-13 180252" src="https://github.com/user-attachments/assets/22a6c14d-7f08-44dc-a06d-b9d572de827e" />



## Project - 2: Find Maximum and Minimum Number 
## Descriptive:
Finding  Maximum and Minimum numbers, Where the user enter the 3 numbers, within the 3 Numbers which one is Maximum and Minimum.

### Algorithm:

1. Ask to Enter 3 number Assume that ( A, B, C ).
    - Display A value:

    - Display B value:

    - Display C value:

2. From Above user want to enter the A,B,C values.

3. It compares  Entered 3 values using the AND operator.
 
  To Display Maximum Number:
  
    - If(a>b) AND (a>c) then display Maximum value is 'A'.
    - elif (b>a) AND (b>c) then display Maximum value is 'B'.
    - else display Maximum value is 'C'.
    
  To Display Minimum Number:
  
    - If(a<b) AND (a<c) then display Minimum value is 'A'.
    - elif (b<a) AND (b<c) then display Minimum value is 'B'.
    - else display Minimum value is 'C'.
4. Special Case is occured, When user entered twice the same number suppose A=33, B=33, C=45. 'It Display the Maximum : 45 ,Two Number are equal 33,33'.

5. Sample Images: 
<img width="948" height="503" alt="Screenshot 2025-08-14 075734" src="https://github.com/user-attachments/assets/043ffb2e-9e45-4ef9-aa75-991a75f34583" />

<img width="953" height="489" alt="Screenshot 2025-08-14 080510" src="https://github.com/user-attachments/assets/0143d59b-b904-40ff-b727-ccf50372d518" />




## Project - 1: Rock Paper Scissor Game
### Description: 
This is a Rock Paper Scissor Game where the one player has to play and opponent computer. Additionaly number of time to play Game.

### Algorithm:

1. Winning rules of the game ROCK PAPER SCISSORS are:
    - Rock vs Paper -> Paper wins
       
    - Rock vs Scissors -> Rock wins
    
    - Paper vs Scissors -> Scissors wins

2. It display in screen is :

    - Enter your choice
    - 1 -Rock 
    - 2 -Paper 
    - 3 -Scissors
4. Ask to enter your choice: Select the Number is 1,2,3.

6. Enter your choice: 1
   User choice is: Rock
   
8. Now it's Computer's Turn...
   Computer choice is: Paper
   Rock vs Paper
   <== Computer wins! ==>

9. Do you want to play again? (Y/N)
    
### NOTE:
    - In this game, randint() inbuilt function is used for generating random integer values within the given range.
    
10. Sample Image:
<img width="942" height="856" alt="Screenshot 2025-08-16 215251" src="https://github.com/user-attachments/assets/75d3c407-da45-401d-9736-810bf40d8b2a" />











