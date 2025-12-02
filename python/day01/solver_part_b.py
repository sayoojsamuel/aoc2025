STARTING_POSITION = 50
TOTAL_POSITIONS = 100


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


def get_count_of_zero_hit(instructions):
    count_of_zero_hit = 0
    current_pointer = STARTING_POSITION

    for direction, count in instructions:
        if direction == Direction.LEFT:
            new_pointer = (current_pointer - count) % TOTAL_POSITIONS
        else:
            new_pointer = (current_pointer + count) % TOTAL_POSITIONS

        if new_pointer == 0:
            count_of_zero_hit += 1

        print(
            f"{current_pointer=}, {direction=}, {count=}, {new_pointer=}, {count_of_zero_hit=}"
        )

        current_pointer = new_pointer
        # input()
    return count_of_zero_hit



def get_count_of_zero_traversal_and_hit(instructions: list):
    LEFT = Direction.LEFT
    RIGHT = Direction.RIGHT

    current_pointer = STARTING_POSITION
    traversals = 0
    ending_at_zero = 0

    for direction, count in instructions:
        if direction == LEFT:
            new_pointer = current_pointer - count

            # starting at 0, increment traversals
            if current_pointer == 0:
                traversals += abs((new_pointer + TOTAL_POSITIONS) // TOTAL_POSITIONS)
            else:
                traversals += abs(new_pointer // TOTAL_POSITIONS)

        elif direction == RIGHT:
            new_pointer = current_pointer + count

            # starting at 0, increment traversals
            if current_pointer == 0:
                traversals += abs(new_pointer // TOTAL_POSITIONS)
            # ending at 0, we will be incrementing touch. only increment traversals if greater than 100
            elif new_pointer % TOTAL_POSITIONS == 0:
                traversals += abs((new_pointer - TOTAL_POSITIONS) // TOTAL_POSITIONS)
            else:
                traversals += new_pointer // TOTAL_POSITIONS

        # ending at 0, increment touch
        if new_pointer % TOTAL_POSITIONS == 0:
            ending_at_zero += 1

        print(
            f"{current_pointer=}, {direction=}, {count=}, {(new_pointer%TOTAL_POSITIONS)=}, {ending_at_zero=}, {traversals=}",
        )

        current_pointer = new_pointer % TOTAL_POSITIONS
    return ending_at_zero, traversals

if __name__ == "__main__":
    instructions = []
    # Read the input fil"e
    with open("input.txt") as input_file:
        input_lock_turns = input_file.read()
        instructions = extract_lock_turns(input_lock_turns)

    # Solve Puzzle 1
    # count_of_zero_hit = get_count_of_zero_hit(instructions)
    # print(f"Zero was hit {count_of_zero_hit} times")

    # Solve puzzle 2 testing
    ending_at_zero, zero_traversals = get_count_of_zero_traversal_and_hit()
    print(f"Sum of {ending_at_zero=} and {zero_traversals=} is {ending_at_zero+zero_traversals}")
