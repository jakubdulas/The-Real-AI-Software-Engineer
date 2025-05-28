import os
import argparse
import difflib


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return None


def collect_files(root_path, skip_dir):
    file_map = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Modify dirnames in-place to skip directories
        dirnames[:] = [d for d in dirnames if d != skip_dir]

        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, filename), root_path)
            file_map[rel_path] = os.path.join(dirpath, filename)

    return file_map


def levenshtein_distance(a, b):
    # difflib is a decent approximation for line-based or small file differences
    seq_matcher = difflib.SequenceMatcher(None, a, b)
    return int((1 - seq_matcher.ratio()) * max(len(a), len(b)))


def compare_files(dir1, dir2, skip_dir):
    files1 = collect_files(dir1, skip_dir)
    files2 = collect_files(dir2, skip_dir)

    common_files = set(files1.keys()) & set(files2.keys())

    if not common_files:
        print("No common files found between the two directories.")
        return

    print(f"Comparing {len(common_files)} common files...\n")
    for rel_path in sorted(common_files):
        content1 = read_file(files1[rel_path])
        content2 = read_file(files2[rel_path])

        if content1 is None or content2 is None:
            continue

        distance = levenshtein_distance(content1, content2)
        print(f"{rel_path}: Levenshtein Distance = {distance}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare code files between two directories using Levenshtein distance."
    )
    parser.add_argument("dir1", help="First directory path.")
    parser.add_argument("dir2", help="Second directory path.")
    parser.add_argument(
        "--skip-dir", default=None, help="Directory name to skip (e.g., venv, .git)."
    )

    args = parser.parse_args()

    if not os.path.isdir(args.dir1) or not os.path.isdir(args.dir2):
        print("Both arguments must be valid directories.")
        exit(1)

    compare_files(args.dir1, args.dir2, args.skip_dir)
