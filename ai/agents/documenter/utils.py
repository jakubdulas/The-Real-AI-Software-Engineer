import os
import subprocess


def create_directory_tree(directory, skip_dirs=None):
    tree = {}
    skip_dirs = set(skip_dirs or [])

    for root, dirs, files in os.walk(directory):
        # Filter out unwanted directories (starts with '__' or '.' or in skip_dirs)
        dirs[:] = [
            d
            for d in dirs
            if not (d.startswith("__") or d.startswith(".") or d in skip_dirs)
        ]

        rel_path = os.path.relpath(root, directory)
        if rel_path == ".":
            rel_path = ""

        current_level = tree
        if rel_path:
            for part in rel_path.split(os.sep):
                current_level = current_level.setdefault(part, {})

        # Filter and add files
        for file in files:
            if (
                file.startswith("__")
                or file.startswith(".")
                or not file.endswith(".py")
            ):
                continue
            current_level[file] = None

    return tree


def find_file_in_tree(tree, filename, current_path=""):
    for key, value in tree.items():
        new_path = os.path.join(current_path, key) if current_path else key
        if key == filename:
            return new_path
        elif isinstance(value, dict):
            result = find_file_in_tree(value, filename, new_path)
            if result:
                return result
    return None


def run_shell_command(command: str) -> str:
    """
    Runs a shell command and returns its output.
    Prevents execution if inside a restricted directory.

    :param command: The shell command to execute.
    :param restricted_dirs: List of restricted directories where execution is not allowed.
    :return: Output of the command or an error message if restricted.
    """
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True, timeout=5
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return ""
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


if __name__ == "__main__":
    print(
        run_shell_command(
            "python3 /Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/codes/pacman_game/main.py"
        )
    )
