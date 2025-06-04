import datetime

def validate_non_empty(prompt):
    """Prompt the user and ensure the input is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def format_timestamp(dt):
    """Format a datetime object as a readable string."""
    if isinstance(dt, str):
        # Already formatted or ISO string
        try:
            dt = datetime.datetime.fromisoformat(dt)
        except ValueError:
            return dt
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def get_confirmation(prompt="Are you sure? (y/n): "):
    """Prompt the user for a yes/no confirmation."""
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")
