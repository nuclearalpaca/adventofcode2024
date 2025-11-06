class FilterModule(object):
    def filters(self):
        return {
            'find_obstruction_positions': find_obstruction_positions
        }


def find_obstruction_positions(input_file_content, directions, guard_position, map_width, map_height, visited_positions):
    # Convert input_file_content into a list of lists (mutable)
    original_grid = [list(row) for row in input_file_content]
    
    # Initialize the loop count for revisiting a position with the same direction
    loop_counter = 0

    for position in visited_positions:
        row, col = position
        grid = [row.copy() for row in original_grid]
        # Modify the grid by replacing the character at the position with '#'
        grid[row][col] = '#'
        
        # Now, let's simulate the guard's movement with the initial direction [-1, 0] (up)
        current_row, current_col = guard_position
        direction_idx = 0  # Initial direction index (up)
        visited_positions_with_direction = set()  # Set to store visited positions with direction
        
        # Simulate guard's movement
        while True:
            # Calculate the next position based on the current direction
            direction = directions[direction_idx]
            next_row = current_row + direction[0]
            next_col = current_col + direction[1]
            
            # Check if the next position is within bounds
            if not (0 <= next_row < map_height and 0 <= next_col < map_width):
                break  # Exit if the guard moves out of bounds
            
            # Check if the guard encounters an obstacle (a #)
            if grid[next_row][next_col] == '#':
                # Change direction to the next one in the directions list (right turn)
                direction_idx = (direction_idx + 1) % len(directions)
                continue  # Continue to check the new direction
            
            # Check if the guard has visited this position with the same direction
            if (next_row, next_col, direction_idx) in visited_positions_with_direction:
                loop_counter += 1
                break  # Break the loop since the guard is stuck

            # Add the current position and direction to the set of visited positions with direction
            visited_positions_with_direction.add((next_row, next_col, direction_idx))
            
            # Update the current position
            current_row, current_col = next_row, next_col
    
    # Return the total count of loops encountered
    return loop_counter
