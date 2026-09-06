import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def create_baseline(files, output):
    baseline = {str(Path(f)): sha256_file(f) for f in files}
    Path(output).write_text(json.dumps(baseline, indent=2) + "\n", encoding="utf-8")
    print(f"Baseline written to {output}")


def check_baseline(baseline_file):
    baseline = json.loads(Path(baseline_file).read_text(encoding="utf-8"))
    changed = []
    missing = []
    for file, expected in baseline.items():
        path = Path(file)
        if not path.exists():
            missing.append(file)
        elif sha256_file(path) != expected:
            changed.append(file)
    if not changed and not missing:
        print("FIM CHECK: PASS - no protected files changed.")
        return 0
    print("FIM CHECK: FAIL")
    for file in changed:
        print(f"  CHANGED: {file}")
    for file in missing:
        print(f"  MISSING: {file}")
    return 2


def main():
    parser = argparse.ArgumentParser(description="Simple file-integrity monitoring check for the GRC lab.")
    parser.add_argument("--baseline", default="fim_baseline.json")
    parser.add_argument("--init", action="store_true")
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()
    if args.init:
        if not args.files:
            parser.error("--init requires one or more files")
        create_baseline(args.files, args.baseline)
        return 0
    return check_baseline(args.baseline)


if __name__ == "__main__":
    raise SystemExit(main())
