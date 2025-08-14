
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
Finding  Maximum and Minimum  Numbers, Where the user will enter the 3 numbers, within the 3 Numbers which one is Maximum and Minimum  going to Finds

### Algorithm:

1. Ask to 'Enter 3 number' for Better understanding purpose we Assume that suppose ( A, B, C ).

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









