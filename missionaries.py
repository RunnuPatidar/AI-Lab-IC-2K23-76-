from collections import deque

def is_valid(m, c):
    # No negative numbers or more than 3 people of either group.
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries must not be outnumbered on either bank.
    left_safe = (m == 0 or m >= c)

    right_m = 3 - m
    right_c = 3 - c
    right_safe = (right_m == 0 or right_m >= right_c)

    return left_safe and right_safe


def missionaries_cannibals():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat passenger combinations.
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found!\n")

            for step, (m, c, b) in enumerate(path):
                left_bank = f"{m}M, {c}C"
                right_bank = f"{3-m}M, {3-c}C"
                boat_side = "Left" if b == 0 else "Right"

                print(
                    f"Step {step}: Left Bank [{left_bank}] | "
                    f"Right Bank [{right_bank}] | Boat: {boat_side}"
                )

            print(f"\nTotal crossings: {len(path) - 1}")
            return

        for move_m, move_c in moves:

            if boat == 0:
                # Boat moves from left to right.
                new_state = (
                    m - move_m,
                    c - move_c,
                    1
                )
            else:
                # Boat moves from right to left.
                new_state = (
                    m + move_m,
                    c + move_c,
                    0
                )

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    print("No solution found.")


missionaries_cannibals()