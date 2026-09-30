<p align="center">
  <img src="web-icon.png" width="250" alt="Death by Midnight">
</p>

# Death by Midnight

[![release](https://img.shields.io/github/v/release/remarkablegames/death-by-midnight)](https://github.com/remarkablegames/death-by-midnight/releases)
[![build](https://github.com/remarkablegames/death-by-midnight/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/death-by-midnight/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/death-by-midnight/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/death-by-midnight/actions/workflows/lint.yml)

🕛 **Death by Midnight** is a time-loop murder mystery. You're a detective hired to read a dead man's will at midnight—but when something terrible happens, the night resets. Trapped in an endless cycle, you must uncover the truth, stop the murders, and escape the loop.

Play in your browser:

- [itch.io](https://remarkablegames.itch.io/death-by-midnight)
- [Wavedash](https://wavedash.com/games/death-by-midnight)
- [remarkablegames](https://remarkablegames.org/death-by-midnight/)

Or download for desktop:

- [Windows](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/win.zip)
- [Mac](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/mac.zip)
- [Linux](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/linux.tar.bz2)

## Features

- An in-game clock where every action advances time
- Point-and-click exploration
- Interact with characters and unlock new dialogue
- Collect and use inventory items
- Multiple endings, including good, bad, and true endings
- Estimated playtime: 15–30 minutes (3,000+ words)

## Warnings

- Jumpscares
- Depictions of death, murder, and suicide
- Blood

## Credits

### Art

- [3DModelsCC0](https://3dmodelscc0.itch.io/)
- [Free Visual Novel Backgrounds (Mansion Pack)](https://potat0master.itch.io/free-visual-novel-backgrounds-mansion-pack) by [Potat0Master](https://potat0master.itch.io/)
- [Vector Books Icon Pack](https://vedasir.itch.io/vector-books-icon-pack)
- [Visual Novel Horror Asset Pack](https://kalaverita.itch.io/visual-novel-horror-asset-pack) by [Kalaverita](https://kalaverita.itch.io/)

### Audio

- [Free music pack](https://sinetient.itch.io/free-music-pack) by [Sinetient](https://sinetient.itch.io/)
- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- [Love & Terror [BGM Pack - Vol 01]](https://melancholy-marionette.itch.io/love-terror-vol-01-bgm-pack) by [Melancholy Marionette](https://melancholy-marionette.itch.io/)
- [Sound effects from Pixabay](https://pixabay.com/sound-effects/)
- [Text/Dialogue Bleeps Pack](https://dmochas-assets.itch.io/dmochas-bleeps-pack)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/death-by-midnight.git
cd death-by-midnight
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -type f -name '*.rpyc' -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```
