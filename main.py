import os
from pathlib import Path

# The funniest excuse for skipping a meeting: razor-sharp, relatable, and tight.
EXCUSE: str = (
    "I can't attend: I'm currently drafting the email explaining why this meeting shouldn't exist, and showing up would ruin the surprise."
)


def main() -> None:
    # Print the line to stdout
    print(EXCUSE)

    makefun_output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    primary_written = False

    if makefun_output_dir:
        # Explicit MAKEFUN_OUTPUT_DIR: create directory if needed, write entry.txt there
        try:
            target_dir = Path(makefun_output_dir)
            target_dir.mkdir(parents=True, exist_ok=True)
            (target_dir / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")
            primary_written = True
        except Exception:
            pass
    else:
        # Default primary path is /output
        try:
            output_dir = Path("/output")
            if output_dir.is_dir():
                (output_dir / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")
                primary_written = True
        except Exception:
            pass

    # If MAKEFUN_OUTPUT_DIR is unset and /output is not writable, fall back to best-effort repo-local write
    if not makefun_output_dir and not primary_written:
        try:
            repo_root = Path(__file__).resolve().parent
            local_path = repo_root / "output" / "entry.txt"
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_text(EXCUSE + "\n", encoding="utf-8")
        except Exception:
            pass


if __name__ == "__main__":
    main()
