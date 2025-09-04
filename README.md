
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




## Project - 3: Rock Paper Scissor Game
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
3. Ask to enter your choice: Select the Number is 1,2,3.

4. Enter your choice: 1
   User choice is: Rock
   
5. Now it's Computer's Turn...
   Computer choice is: Paper
   Rock vs Paper
   <== Computer wins! ==>

6. Do you want to play again? (Y/N)
    
### NOTE:
    - In this game, randint() inbuilt function is used for generating random integer values within the given range.
    
7. Sample Image:
<img width="942" height="856" alt="Screenshot 2025-08-16 215251" src="https://github.com/user-attachments/assets/75d3c407-da45-401d-9736-810bf40d8b2a" />


## Project - 4: BMI Calculator
### Description:
Body Mass Index (BMI) is a widely used indicator to assess a person’s body weight in relation to their height. It’s a simple yet effective way to determine whether someone is underweight, normal weight, overweight, or obese.


### Algorithm:

1. BMI Formula:
   BMI = weight(kg)/{height(m)}**2

2. User has to  'enter your weight in kilogram:

3. User has to  'enter your height in meters:

4. Then, Display the 'your BMI is:_____'

5. BMi is diaplay has types of weights
    - Underweight: BMI less than 18.5
    - Normal weight: BMI between 18.5 and 24.9
    - Overweight: BMI between 25 and 29.9
    - Obesity: BMI of 30 or greater

6. Sample image:
<img width="977" height="418" alt="Screenshot 2025-08-24 165354" src="https://github.com/user-attachments/assets/9a8b0116-ee9b-4421-bce5-00ad768e57ee" />


## Project - 5: Water_Jug_Problem 
### Description:
Water_Jug_Problem is involed in the Artificial Intelligence. In its classic version, the problem involves two jugs, each with a different capacity.The goal is to measure a specific amount of water using these jugs while adhering to certain rules and constraints.

Let's take a simple example to illustrate the classic Water Jug Problem: You have a 3-liter jug and a 5-liter jug. The task is to measure exactly 4 liters of water.


### Algorithm:

1. It is game, It has limited time (timer) to end the game, only one player has to play game.

2. Consider a scenario where you have a 3-liter jug and a 5-liter jug, and you need to measure precisely 4 liters of water.

3. Visualize the scenario by imagining the two jugs and a water source to fill them.

4. The challenge here is to determine a sequence of actions that will allow you to reach the desired measurement of 4 liters, taking into account the constraints and capacities of the jugs.

5. 'import timer' has involed it has Time left  600sec

6.Sample image:
<img width="908" height="1026" alt="Screenshot 2025-08-24 172023" src="https://github.com/user-attachments/assets/958f4b0a-d2f5-49eb-ac4b-0c146de007e1" />
<img width="796" height="1032" alt="Screenshot 2025-08-24 172042" src="https://github.com/user-attachments/assets/5605fe9e-3c91-474f-b3a8-e3005f64b770" />
<img width="808" height="1039" alt="Screenshot 2025-08-24 172101" src="https://github.com/user-attachments/assets/c9a64498-2c00-49bb-bb4e-242c76c3f30f" />


## Project - 6: Password_generator
### Description:
A Password Generator is a tool that creates strong, random, and secure passwords to help protect your online accounts and sensitive data. Instead of relying on weak or easy-to-guess passwords, the generator uses algorithms to combine uppercase and lowercase letters, and numbers, ensuring high levels of security.


### Algorithm:

1. Input desired password length from the user.

2. Define character sets:
    - Uppercase letters (A–Z)
    - Lowercase letters (a–z)
    - Digits (0–9)

3. Combine all character sets into a single pool of characters.

4. Initialize an empty string for the password.

5. Repeat until the password length is reached:
    - Randomly select a character from the pool.
    - Append the selected character to the password.

6. Ensure the generated password contains at least one uppercase, one lowercase, one digit, and one special character (if required).
    - If not, regenerate or replace characters accordingly.

NOTE: Why use secrets instead of random?

The random module is good for simulations, games, and sampling, but it’s not secure for passwords, tokens, or cryptography because its randomness can be guessed or reproduced.

7. Sample image:
<img width="873" height="328" alt="Screenshot 2025-09-04 213920" src="https://github.com/user-attachments/assets/5a9157a4-8a28-43d3-a69b-24375dcd16e9" />




