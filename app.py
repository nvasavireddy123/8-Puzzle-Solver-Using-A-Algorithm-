import heapq

# -------------------------------------------------------
# GOAL STATE
# -------------------------------------------------------

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# 0 represents the blank space


# -------------------------------------------------------
# DISPLAY PUZZLE
# -------------------------------------------------------

def display(state):
    print("+---+---+---+")

    for i in range(0, 9, 3):
        row = ""

        for j in range(i, i + 3):
            if state[j] == 0:
                row += "|   "
            else:
                row += f"| {state[j]} "

        row += "|"

        print(row)
        print("+---+---+---+")


# -------------------------------------------------------
# MANHATTAN DISTANCE
# -------------------------------------------------------

def manhattan_distance(state):

    distance = 0

    for index in range(9):

        tile = state[index]

        # Ignore blank
        if tile == 0:
            continue

        # Current position
        current_row = index // 3
        current_col = index % 3

        # Goal position
        goal_index = tile - 1

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        # Manhattan distance
        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# -------------------------------------------------------
# GENERATE NEIGHBOURS
# -------------------------------------------------------

def get_neighbors(state):

    neighbors = []

    blank_position = state.index(0)

    row = blank_position // 3
    col = blank_position % 3

    # Possible movements
    movements = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for row_change, col_change in movements:

        new_row = row + row_change
        new_col = col + col_change

        # Check boundaries
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank_position], new_state[new_position] = \
                new_state[new_position], new_state[blank_position]

            neighbors.append(tuple(new_state))

    return neighbors


# -------------------------------------------------------
# A* ALGORITHM
# -------------------------------------------------------

def a_star(start):

    # Priority queue
    # (f_cost, g_cost, state, path)
    priority_queue = []

    h = manhattan_distance(start)

    heapq.heappush(
        priority_queue,
        (h, 0, start, [start])
    )

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        # Goal reached
        if current == GOAL:
            return path

        if current in visited:
            continue

        visited.add(current)

        # Generate next states
        for neighbor in get_neighbors(current):

            if neighbor in visited:
                continue

            new_g = g + 1

            new_h = manhattan_distance(neighbor)

            new_f = new_g + new_h

            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_f, new_g, neighbor, new_path)
            )

    return None


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

print("====================================")
print("       8-PUZZLE SOLVER USING A*")
print("====================================")

# Example starting state

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

print("\nInitial State:")
display(start)

print("\nGoal State:")
display(GOAL)

# Solve puzzle
solution = a_star(start)


# -------------------------------------------------------
# DISPLAY SOLUTION
# -------------------------------------------------------

if solution:

    print("\nSolution Found!")
    print("----------------------------")

    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for step, state in enumerate(solution):

        print("\nStep", step)

        display(state)

else:

    print("\nNo solution found.")