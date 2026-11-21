# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/genahjasa/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/genahjasa/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

This repo holds my submission for a make.fun bounty: a single original
joke about sharing the keyboard with an AI coding agent. A small
Python 3.13 script — standard library only, no network calls, same
result every run — drops that joke into `/output/entry.txt`.

## The joke

> Working beside an AI coding agent is great: it writes the code, I review
> the code, and together we blame the code — until it reviews itself and
> files a bug report against both of us.

## How to run it

```sh
python3 main.py
```

That writes `/output/entry.txt`. Point the output somewhere else by
setting `MAKEFUN_OUTPUT_DIR` first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/jokedemo-out python3 main.py
```

## How to check it

```sh
python3 -m py_compile main.py
MAKEFUN_OUTPUT_DIR=/tmp/jokedemo-out python3 main.py
wc -m /tmp/jokedemo-out/entry.txt   # 182 characters plus the newline (185 in a C locale, where wc -m counts bytes)
```

Before writing anything, the script makes sure the joke is not empty,
fits on one line, and sits inside the bounty's 1–280 character window.

## License

MIT — see [LICENSE](LICENSE).
