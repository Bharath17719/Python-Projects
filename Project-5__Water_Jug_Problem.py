# Water Jug Problem

import time

# Jug capacities
jug1_capacity=3
jug2_capacity=5

# Current amounts
jug1=0
jug2=0

# Goal: measure exactly 4 liters in jug2
goal=4

# Timer countdown
timer = 600
start_time=time.time()

while True:
    # Calculate time left
    elapsed = int(time.time() - start_time)
    time_left = timer - elapsed

    if time_left <= 0:
        print("\n Time's up! You lost the game.")
        break

    print(f"\nJug1:{jug1}/{jug1_capacity},jug2:{jug2}/{jug2_capacity},Time left:{time_left}s")

    if jug2==goal:
        print(" Goal achieved! jug2 has 4 liters.")
        break
        
    # Show choices
    print("Choose action:")
    print("1. Fill Jug1")
    print("2. Fill Jug2")
    print("3. Empty Jug1")
    print("4. Empty Jug2")
    print("5. Pour Jug1 -> Jug2")
    print("6. Pour Jug2 -> Jug1")

    choice = int(input("Enter choice (1-6): "))

    if choice == 1:
        jug1 = jug1_capacity
    elif choice == 2:
        jug2 = jug2_capacity
    elif choice == 3:
        jug1 = 0
    elif choice == 4:
        jug2 = 0
    elif choice == 5:
        transfer = min(jug1, jug2_capacity - jug2)
        jug1 -= transfer
        jug2 += transfer
    elif choice == 6:
        transfer = min(jug2, jug1_capacity - jug1)
        jug2 -= transfer
        jug1 += transfer
    else:
        print("Invalid choice!")









