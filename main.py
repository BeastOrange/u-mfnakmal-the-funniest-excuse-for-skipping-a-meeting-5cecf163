import os
from pathlib import Path

# The funniest excuse for skipping a meeting: razor-sharp, relatable, and tight.
EXCUSE: str = (
    "I can't attend: I promised my therapist I'd stop joining meetings where five seconds of awkward silence is counted as unanimous consent."
)


def main() -> None:
    # Print the line to stdout
    print(EXCUSE)

    # Write to output/entry.txt relative to repository root
    repo_root = Path(__file__).resolve().parent
    local_output_path = repo_root / "output" / "entry.txt"
    local_output_path.parent.mkdir(parents=True, exist_ok=True)
    local_output_path.write_text(EXCUSE + "\n", encoding="utf-8")

    # Attempt to write to /output/entry.txt (skip silently if unavailable)
    try:
        root_output_path = Path("/output/entry.txt")
        root_output_path.parent.mkdir(parents=True, exist_ok=True)
        root_output_path.write_text(EXCUSE + "\n", encoding="utf-8")
    except Exception:
        pass


if __name__ == "__main__":
    main()
