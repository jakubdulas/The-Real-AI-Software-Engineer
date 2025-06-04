from game_loop import GameLoop

def main():
    # All main configuration for the window and grid
    CELL_SIZE = 20
    GRID_WIDTH = 20
    GRID_HEIGHT = 20
    BG_COLOR = (0, 0, 0)
    GRID_COLOR = (40, 40, 40)
    WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
    WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
    MOVE_DELAY = 120

    config = {
        'cell_size': CELL_SIZE,
        'grid_width': GRID_WIDTH,
        'grid_height': GRID_HEIGHT,
        'window_width': WINDOW_WIDTH,
        'window_height': WINDOW_HEIGHT,
        'bg_color': BG_COLOR,
        'grid_color': GRID_COLOR,
        'move_delay': MOVE_DELAY
    }
    game = GameLoop(config)
    game.run()

if __name__ == "__main__":
    main()
