"""Deadpan Forecasts for Cities That Do Not Exist.

Writes one deadpan weather line for the invented city of Sleetborough
to /output/entry.txt. Fully deterministic: the same line every run.
"""

import os

LINE = "I'm tracking one cloud over Sleetborough that has followed the mayor since March. High of 28, light snow. It has tenure now."
# 124 characters of the 160 allowed (77.5%): one invented city, one
# impossible-but-flat detail (the cloud with tenure), one deadpan verdict.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
