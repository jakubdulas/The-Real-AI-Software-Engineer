import os
import argparse


def count_lines_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return 0


def count_lines_in_directory(root_path, skip_dir):
    total_lines = 0
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Modify dirnames in-place to skip directories
        dirnames[:] = [d for d in dirnames if d != skip_dir and not d.startswith("__")]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_lines += count_lines_in_file(filepath)

    return total_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count total lines of code in a directory, skipping specified directory."
    )
    parser.add_argument("path", help="Root directory to start scanning.")
    parser.add_argument(
        "--skip-dir", default=None, help="Name of the directory to skip."
    )

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a valid directory.")
        exit(1)

    total = count_lines_in_directory(args.path, args.skip_dir)
    print(f"Total lines of code (excluding '{args.skip_dir}' directories): {total}")
