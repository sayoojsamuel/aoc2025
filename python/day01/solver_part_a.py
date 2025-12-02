import os

class Direction:
    LEFT = "left"
    RIGHT = "right"

def extract_lock_turns(input_steps: str):
    """Get list of turn instructions
    
    Args: 
        input_steps: str - New line seperated turn instructions 

    Returns:
        List of tuple of direction and count at each step
        [(direction, count)]    
    """
    input_steps = input_steps.splitlines()

    instructions = []
    for step in input_steps:
        if step.startswith("L"):
            direction = Direction.LEFT
        else:
            direction = Direction.RIGHT
        count = int(step[1:])
        instructions.append((direction, count))
    return instructions



if __name__ == "__main__":
    
    STARTING_POSITION = 50
    TOTAL_POSITIONS = 100

    count_of_zero_hit = 0

    current_pointer = STARTING_POSITION

    instructions = []
    # Read the input fil"e
    with open("input.txt") as input_file:
        input_lock_turns = input_file.read()
        instructions = extract_lock_turns(input_lock_turns)

    for direction, count in instructions:
        if direction == Direction.LEFT:
            new_pointer = (current_pointer - count) % TOTAL_POSITIONS
        else:
            new_pointer = (current_pointer + count) % TOTAL_POSITIONS
        
        if new_pointer == 0:
            count_of_zero_hit += 1

        print(f"{current_pointer=}, {direction=}, {count=}, {new_pointer=}, {count_of_zero_hit=}")

        current_pointer = new_pointer
        # input()

    print(f"Zero was hit {count_of_zero_hit} times")

    