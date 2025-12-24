def solve_worksheet(filename, part_two=False):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Remove trailing newlines and filter out empty lines
    lines = [line.rstrip('\n') for line in lines if line.strip()]
    
    if not lines:
        return 0
    
    max_len = max(len(line) for line in lines) if lines else 0
    lines = [line.ljust(max_len) for line in lines]
    
    # The last line contains the operations
    operations_line = lines[-1]
    number_lines = lines[:-1]
    
    # Find all operations and their column positions
    operations = []
    for col in range(len(operations_line)):
        char = operations_line[col]
        if char in ['+', '*']:
            operations.append((col, char))
    
    # Find separator columns (columns that are all spaces across all lines)
    separator_cols = set()
    for col in range(max_len):
        is_separator = True
        for line in lines:
            if col < len(line) and line[col] != ' ':
                is_separator = False
                break
        if is_separator:
            separator_cols.add(col)
    
    grand_total = 0
    
    # Process each problem (each operation)
    for op_idx, (op_col, operation) in enumerate(operations):
        # Find the column range for this problem
        start_col = 0
        if op_idx > 0:
            prev_op_col = operations[op_idx - 1][0]
            for col in range(prev_op_col + 1, op_col):
                if col in separator_cols:
                    start_col = col + 1
                    break
            else:
                start_col = prev_op_col + 1
        
        end_col = max_len
        if op_idx < len(operations) - 1:
            next_op_col = operations[op_idx + 1][0]
            for col in range(op_col + 1, next_op_col):
                if col in separator_cols:
                    end_col = col
                    break
            else:
                end_col = next_op_col
        
        if part_two:
            # Part Two: Read numbers right-to-left, column by column
            # Each number occupies ONE column with digits stacked vertically.
            # Most significant digit is at the top, least significant at the bottom.
            # Numbers are separated by columns that are all spaces.
            
            numbers = []
            
            # Process columns from right to left
            col = end_col - 1
            
            while col >= start_col:
                if col in separator_cols:
                    col -= 1
                    continue
                
                # Check if this column has any digits
                col_digits = []
                for line in number_lines:
                    if col < len(line) and line[col].isdigit():
                        col_digits.append(int(line[col]))
                
                # Check if this column is all spaces in number lines (separator between numbers)
                is_num_separator = True
                for line in number_lines:
                    if col < len(line) and line[col] != ' ':
                        is_num_separator = False
                        break
                
                if not is_num_separator and col_digits:
                    # This column contains a number
                    # Read digits from top to bottom (most significant to least significant)
                    num = 0
                    for digit in col_digits:
                        num = num * 10 + digit
                    numbers.append(num)
                
                col -= 1
            
            # Reverse numbers since we read right-to-left
            numbers.reverse()
            
        else:
            # Part One: Extract numbers normally (left-to-right)
            numbers = []
            for line in number_lines:
                segment = line[start_col:end_col]
                parts = segment.split()
                for part in parts:
                    try:
                        num = int(part)
                        numbers.append(num)
                    except ValueError:
                        pass
        
        # Calculate result for this problem
        if numbers:
            if operation == '+':
                result = sum(numbers)
            else:  # operation == '*'
                result = 1
                for num in numbers:
                    result *= num
            grand_total += result
            if len(numbers) <= 5:  # Only print for small problems
                print(f"Problem: {numbers} {operation} = {result}")
    
    return grand_total

# Test with the example
if __name__ == "__main__":
    # Test Part One
    print("Part One:")
    result1 = solve_worksheet("day6.test", part_two=False)
    print(f"Grand total: {result1}\n")
    
    # Test Part Two with example
    print("Part Two (example):")
    result2_example = solve_worksheet("../../input.txt", part_two=True)
    print(f"Grand total: {result2_example}\n")
    
    # Part Two with actual input
    print("Part Two (actual):")
    result2 = solve_worksheet("day6.test", part_two=True)
    print(f"Grand total: {result2}")
