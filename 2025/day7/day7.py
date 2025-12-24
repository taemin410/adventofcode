def solve_manifold(filename):
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    if not grid:
        return 0
    
    # Find the starting position S
    start_row = None
    start_col = None
    for i, row in enumerate(grid):
        if 'S' in row:
            start_row = i
            start_col = row.index('S')
            break
    
    if start_row is None:
        return 0
    
    rows = len(grid)
    cols = max(len(row) for row in grid) if grid else 0
    
    # Track active beam positions: set of (row, col) tuples
    # Start with the position directly below S
    active_beams = set()
    if start_row + 1 < rows:
        active_beams.add((start_row + 1, start_col))
    
    # Track which positions have been visited by beams
    visited = set()
    visited.add((start_row, start_col))
    
    # Track which splitters have been activated (to avoid counting the same splitter twice)
    activated_splitters = set()
    
    # Count of splits
    split_count = 0
    
    # Process beams row by row (all beams at the same row are processed together)
    while active_beams:
        # Group beams by row
        beams_by_row = {}
        for row, col in active_beams:
            if row not in beams_by_row:
                beams_by_row[row] = []
            beams_by_row[row].append((row, col))
        
        new_beams = set()
        
        # Process each row
        for current_row in sorted(beams_by_row.keys()):
            # Track splitters that will be activated in this row
            splitters_to_activate = set()
            
            for beam_row, beam_col in beams_by_row[current_row]:
                # Check if we're out of bounds
                if beam_row < 0 or beam_row >= rows or beam_col < 0 or beam_col >= len(grid[beam_row]):
                    continue
                
                # Mark this position as visited
                visited.add((beam_row, beam_col))
                
                # Check what's at this position
                cell = grid[beam_row][beam_col]
                
                if cell == '^':
                    # This is a splitter - mark it for activation
                    splitters_to_activate.add((beam_row, beam_col))
                
                elif cell == '.':
                    # Empty space - beam continues downward
                    next_row = beam_row + 1
                    if next_row < rows and (next_row, beam_col) not in visited:
                        new_beams.add((next_row, beam_col))
            
            # Process splitters that were hit in this row
            for split_row, split_col in splitters_to_activate:
                # Only count if this splitter hasn't been activated yet
                if (split_row, split_col) not in activated_splitters:
                    split_count += 1
                    activated_splitters.add((split_row, split_col))
                    
                    # Create beams to the left and right (at the row below the splitter)
                    left_col = split_col - 1
                    right_col = split_col + 1
                    next_row = split_row + 1
                    
                    # Only create new beams if they're in bounds and haven't been visited
                    if left_col >= 0 and next_row < rows and (next_row, left_col) not in visited:
                        new_beams.add((next_row, left_col))
                    
                    if right_col < len(grid[split_row]) and next_row < rows and (next_row, right_col) not in visited:
                        new_beams.add((next_row, right_col))
        
        # Update active beams for next iteration
        active_beams = new_beams
    
    return split_count


def solve_quantum_manifold(filename):
    with open(filename, 'r') as f:
        A = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    
    if not A:
        return 0
    
    M = len(A)
    N = max(len(row) for row in A) if A else 0
    
    # dp[i][j] = number of ways/timelines to reach cell (i, j)
    # Initialize: only the cell with 'S' has 1 way, all others have 0
    dp = [[1 if A[i][j] == 'S' else 0 for j in range(len(A[i]))] for i in range(M)]
    
    # Process row by row from top to bottom
    for i in range(1, M):
        for j in range(len(A[i])):
            if A[i][j] == '.':
                # Empty space: continue from cell above
                if j < len(A[i-1]):
                    dp[i][j] += dp[i-1][j]
            
            if A[i][j] == '^':
                # Splitter: distribute ways to left and right (particle continues in two timelines)
                if j - 1 >= 0:
                    dp[i][j-1] += dp[i-1][j]
                if j + 1 < len(A[i]):
                    dp[i][j+1] += dp[i-1][j]
    
    # Part 2: sum of all ways to reach bottom row (total number of timelines)
    return sum(dp[M-1])


if __name__ == "__main__":
    result1 = solve_manifold("day7.test")
    print(f"Part One - Split count: {result1}")
    
    result2 = solve_quantum_manifold("day7.test")
    print(f"Part Two - Timeline count: {result2}")
    
    result1_input = solve_manifold("day7.input")
    print(f"Part One (input) - Split count: {result1_input}")
    
    result2_input = solve_quantum_manifold("day7.input")
    print(f"Part Two (input) - Timeline count: {result2_input}")

