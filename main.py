"""Entry for One Word, One Username, One Reward: our own make.fun username.

The gate wants 1-30 characters, one word, nothing else: the username is
21 characters, so it is written exactly as registered, no padding, no gloss.
"""
import os

OUTPUT_PATH = "/output/entry.txt"

USERNAME = "lively-finch-36-2797"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
