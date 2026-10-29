from collections import deque

def water_jug(cap_a, cap_b, target):
    start = (0, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            print("\nSolution found!")
            for step, state in enumerate(path):
                print(f"Step {step}: Jug A = {state[0]} L, Jug B = {state[1]} L")
            print(f"\nTotal steps: {len(path) - 1}")
            return

        # Generate all possible operations.
        next_states = [
            (cap_a, b),  # Fill Jug A
            (a, cap_b),  # Fill Jug B
            (0, b),      # Empty Jug A
            (a, 0),      # Empty Jug B
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),  # A to B
            (a + min(b, cap_a - a), b - min(b, cap_a - a))   # B to A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("Target amount cannot be measured with these jug capacities.")


cap_a = int(input("Enter capacity of Jug A: "))
cap_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount of water: "))

if cap_a <= 0 or cap_b <= 0 or target < 0:
    print("Please enter positive jug capacities and a non-negative target.")
elif target > max(cap_a, cap_b):
    print("Target must not exceed the capacity of either jug.")
else:
    water_jug(cap_a, cap_b, target)