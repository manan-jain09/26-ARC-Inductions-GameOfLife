#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Checks all 8 surrounding cells (3x3 box minus the center)
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue  
            n_row, n_col = row + d_row, col + d_col

            if 0 <= n_row < rows and 0 <= n_col < cols:
                alive_count += grid[n_row][n_col]

    return alive_count


    # TODO: Implement your neighbor-counting logic here!

    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)
            is_alive = grid[row][col] == 1

            if is_alive and neighbors in (2, 3):
                next_grid[row][col] = 1   # Survival
            elif not is_alive and neighbors == 3:
                next_grid[row][col] = 1   # Reproduction
            else:
                next_grid[row][col] = 0   # Underpopulation / Overpopulation / stays dead

    return next_grid