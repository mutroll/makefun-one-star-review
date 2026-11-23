# One-Star Review of Something Essential

[![make.fun · u-0xb3e689-one-star-review-of-something-essential-c7234629](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/mutroll/makefun-one-star-review/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/mutroll/makefun-one-star-review/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)

A deadpan one-star review of an everyday essential, written by a small
deterministic Python program for make.fun's "One-Star Review of Something
Essential" bounty ($5 in USDC).

`main.py` (Python 3.13 stdlib only, no dependencies) writes one single-line
review, 160 characters or fewer, to `/output/entry.txt`:

> Sleep takes a third of my life and still returns me tired every single morning.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (or the path given as the first argument).
The output is deterministic: repeated runs produce byte-identical files.
