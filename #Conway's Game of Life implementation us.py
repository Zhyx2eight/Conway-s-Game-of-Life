# Conway's Game of Life
import random
import os
from typing import List
from time import sleep


SIZE = 17


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls') 
    else:
        _ = os.system('clear')  


def make_grid(grid):
    for row in grid:
        for val in row:
            print(val, end=" ")
        print()
    print()


#set rules for dead and living cells
def neighbor_cell_count(grid: List[List[int]], row: int, col: int) -> int:
    alive = 0
    #top left
    rows = row - 1 if row - 1 is not -1 else SIZE - 1
    columns = col - 1 if col - 1 is not -1 else SIZE - 1
    if grid[rows][columns]:
        alive += 1

    #up
    rows = row - 1 if row - 1 is not -1 else SIZE - 1
    if grid[rows][col]:
        alive += 1

    #top right
    rows = row - 1 if row - 1 is not -1 else SIZE - 1
    columns = col + 1 if col + 1 is not SIZE else 0
    if grid[rows][columns]:
        alive += 1

    #left
    columns = col - 1 if col - 1 is not -1 else SIZE - 1
    if grid[row][columns]:
        alive += 1

    if alive > 3:
        return alive

    #right
    columns = col + 1 if col + 1 is not SIZE else 0
    if grid[row][columns]:
        alive += 1

    if alive > 3: 
        return alive

    #bottom left
    rows = row + 1 if row + 1 is not SIZE else 0
    columns = col - 1 if col - 1 is not -1 else SIZE - 1
    if grid[rows][columns]:
        alive += 1

    if alive > 3:
        return alive

    #below
    rows = row + 1 if row + 1 is not SIZE else 0
    if grid[rows][col]:
        alive += 1

    if alive > 3 or alive == 0:
        return alive

    #bottom right
    rows = row + 1 if row + 1 is not SIZE else 0
    columns = col + 1 if col + 1 is not SIZE else 0
    if grid[rows][columns]:
        alive += 1

    return alive


def check_rules(grid: List[List[int]], row: int, col: int) -> bool:
    live_neighbors = neighbor_cell_count(grid, row, col)
    if live_neighbors == 3:
        return True
    elif grid[row][col] and live_neighbors == 2:
        return True
    else:
        return False


def Generation_count() -> int:
    while True:
        try:
            generations = int(input("How many generations would you like to run? "))
            if generations <= 0:
                print("Please enter a positive number.")
                continue
            return generations
        except ValueError:
            print("Invalid. Please enter a valid number.")


def try_again() -> bool:
    while True:
        response = input("Restart? (yay/nay): ").lower().strip()
        if response in ['yay', 'aight', 'ong twin']:
            return True
        elif response in ['nay', 'nah', 'no way']:
            return False
        else:
            print("jus use the choices twin omg ")


def run_sim():
    # Make a game grid
    grid = [[random.choice([0, 1]) for _ in range(SIZE)] for _ in range(SIZE)]

    # Ask user for number of generations
    max_generations = Generation_count()

    # Start the game
    gen_count = 1
    while gen_count <= max_generations:
        clear_screen()
        print(f"Generation {gen_count}:")
        make_grid(grid)
        sleep(.25)

        # Working grid to track next generation for simultaneous changes
        next_grid = grid.copy()

        # Iterate over current grid, make changes to working grid
        for row in range(SIZE):
            for col in range(SIZE):
                alive_next_time = check_rules(grid, row, col)
                if alive_next_time:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0
        
        # Reset printed grid to working grid
        grid = next_grid.copy()
        gen_count += 1
    
    print(f"\nSimulation completed! Ran {max_generations} generations.")


def main():
    print("Welcome to Conway's Game of Life!")
    print("-------------------------------------")
    
    while True:
        run_sim()
        
        if not try_again():
            print("Thanks for playing! Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()