"""The Router Confesses.

A home Wi-Fi router excuses itself for dropping the connection at the
exact moment a movie reaches its climax.

The joke, judged against the kit's criteria in order:
1. It IS a one-line excuse from the router for the drop at the climax.
2. The twist: the drop was not an accident. The router held the
   climax hostage on purpose, and the ransom is a thank-you.
3. The voice is the appliance itself: a grudge nursed for three
   years, plus a fragile ego bragging about "flawless streaming".
4. One breath, 125 characters, no setup that needs explaining.
5. It dodges the exhausted jokes: no buffering wheel, no bandwidth,
   no firmware update, no turn-it-off-and-on-again.
"""

import os

ENTRY = (
    "I didn't lose the connection at the climax \u2014 I held it hostage "
    "until someone thanks me for three years of flawless streaming."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != entry:
        raise ValueError("read-back entry does not match")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
