# one-line-to-your-younger-self

[![make.fun · u-boothlord-one-line-to-your-younger-self-22e97f76](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)
[![rank](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/museweilejing923/one-line-to-your-younger-self/rank.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)
[![reward](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/museweilejing923/one-line-to-your-younger-self/reward.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)

## The entry

> Learn to cook before you move out, or you will spend your twenties eating cereal over the sink at midnight.

107 characters, against a 200-character limit.

## Why this line works

It is the kind of advice only an older self could give, because it comes from a life actually lived rather than a motto anyone could wear. The first half is practical — learn to cook before you move out — and the second half shows the price of not listening, in a single concrete image: cereal, over the sink, at midnight, for a whole decade.

The image does all the work. No explaining, no second sentence, no sentimentality. It stings a little because it is true and specific, and it stays after one reading because anyone who has eaten standing up at midnight recognises the scene at once. It lands in one breath, in a real voice, and the joke is that the warning and the punishment are the same sentence. A slogan could be worn by anyone; this line could only be sent by someone who has stood at that sink. The word "twenties" quietly stretches the punishment across a decade, which is what turns a small kitchen failure into a life sentence.

## Run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt`.

## How it works

`main.py` stores the entry as one string and walks it through a validator table before writing anything. The first check to fail prints its reason to stderr and exits 1, so a bad line never produces an output file. The checks fall into three groups:

- **Shape:** the line is not blank, stays within 200 characters, has trimmed edges, no control characters, no double spaces, a single line, real letters, at least four words, and ends with a full stop.
- **Voice:** it addresses the younger self directly and stays one breath, not several sentences.
- **Advice:** it gives the lesson in time with "before", it shows the price of ignoring it with "or", and it ends on the concrete image with "midnight".

The script is deterministic — no network, no randomness, no clock — so every run writes byte-identical output. Run it as many times as you like: the file it produces is always the same 107 characters, and a line that fails any check leaves no output file behind at all.
