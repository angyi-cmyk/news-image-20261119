# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/angyi-cmyk/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/angyi-cmyk/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A program that writes one image summing up the world news of Thursday 19 November 2026 — the ICJ genocide ruling on Myanmar, the Trump–Xi–Putin summit in Shenzhen, Anthropic's record Nasdaq debut, and more. The image is drawn by `draw_image.py` (Pillow) and copied to `/output/entry.png` by `main.py`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image after editing the stories in `draw_image.py`:

```sh
python3 draw_image.py
```

## Sources

Headlines as reported on 19 November 2026: the International Court of Justice ruled Myanmar committed genocide against the Rohingya, 9–6, the first such ruling against a state, with reparations ordered (Al Jazeera, Le Monde, CNN, WSJ); Trump, Xi and Putin held their first three-way summit in Shenzhen and issued a joint peace declaration, with dialogue on nuclear risks but no concrete measures (MercoPress, The Japan Times); Anthropic debuted on Nasdaq after the largest IPO in history, raising $81 billion with shares priced at $83 under ticker ANT (MercoPress, The Observer BD); Houthi attacks damaged Riyadh's tallest building (The Japan Times); the IMF warned global public debt will soon reach 100% of GDP, the highest since the Second World War (MercoPress); Bangladesh was hit by violence and instability amid protests by the exiled former leader's party (The Japan Times).

---

<sub>Entered on [make.fun](https://make.fun/?ref=m2756q7x&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
