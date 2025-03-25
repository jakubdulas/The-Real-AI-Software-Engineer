    # Initialize distinct ghost types
    ghost1 = Ghost('Chaser', 5, 5)  # Aggressive chaser
    ghost2 = Ghost('Random', 7, 7)  # Random mover

    # Inside the game loop
    ghost1.move_towards(pacman.x, pacman.y, grid)  # Move ghost1 towards Pacman
    ghost2.random_move(grid)  # Move ghost2 randomly
    
    # Check collisions with both ghosts
    if (pacman.x, pacman.y) == (ghost1.x, ghost1.y) or (pacman.x, pacman.y) == (ghost2.x, ghost2.y):
        print('Game Over! The ghost caught Pac-Man!')
        running = False