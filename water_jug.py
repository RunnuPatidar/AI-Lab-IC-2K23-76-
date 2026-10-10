
from collections import deque

def water_jug(capacity_a, capacity_b, target):
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {(0, 0): None}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            state = (a, b)

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("Solution Found:")
            for step, (x, y) in enumerate(path):
                print(f"Step {step}: Jug A = {x}L, Jug B = {y}L")
            return

        transfer_ab = min(a, capacity_b - b)
        transfer_ba = min(b, capacity_a - a)

        next_states = [
            (capacity_a, b),             # Fill A
            (a, capacity_b),             # Fill B
            (0, b),                      # Empty A
            (a, 0),                      # Empty B
            (a - transfer_ab, b + transfer_ab),  # Pour A to B
            (a + transfer_ba, b - transfer_ba)   # Pour B to A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)

    print("No solution exists.")

water_jug(4, 3, 2)
