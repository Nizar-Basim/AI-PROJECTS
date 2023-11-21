from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting point
    return total_distance

def traveling_salesman_bruteforce(distances):
    locations = list(range(len(distances)))
    shortest_path = None
    min_distance = float('inf')

    for perm in permutations(locations):
        current_distance = calculate_total_distance(perm, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = perm

    return shortest_path, min_distance

def main():
    # Take user input for distances between locations
    n = int(input("Enter the number of locations: "))
    print("Enter the distances between locations:")

    distances = []
    for i in range(n):
        row = list(map(int, input().split()))
        distances.append(row)

    # Solve the TSP problem
    shortest_path, min_distance = traveling_salesman_bruteforce(distances)

    # Display the result
    print("\nShortest Path:", shortest_path)
    print("Minimum Distance:", min_distance)

if __name__ == "__main__":
    main()
