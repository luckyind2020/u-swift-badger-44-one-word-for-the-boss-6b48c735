"""One Word for the Boss — entry runner.

Reads the single-word entry from entry.txt next to this file,
checks it is exactly one word of at most 30 characters, and
prints it on its own line. Nothing else is printed: the word
is the whole entry.
"""

from pathlib import Path


def load_entry() -> str:
    path = Path(__file__).resolve().parent / "entry.txt"
    return path.read_text(encoding="utf-8").strip()


def validate_entry(word: str) -> str:
    """A valid entry is one plain word, letters only, at most 30 chars."""
    if not word:
        raise SystemExit("entry.txt is empty: it must hold exactly one word")
    if len(word.split()) != 1:
        raise SystemExit("entry.txt must hold exactly one word, not a phrase")
    if len(word) > 30:
        raise SystemExit("entry must be at most 30 characters")
    if not word.isalpha():
        raise SystemExit("entry must be a single plain word with letters only")
    return word


def main() -> None:
    print(validate_entry(load_entry()))


if __name__ == "__main__":
    main()
