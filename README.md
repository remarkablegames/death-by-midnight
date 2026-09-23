<p align="center">
  <img src="web-icon.png" width="250" alt="Death by Midnight">
</p>

# Death by Midnight

[![release](https://img.shields.io/github/v/release/remarkablegames/death-by-midnight)](https://github.com/remarkablegames/death-by-midnight/releases)
[![build](https://github.com/remarkablegames/death-by-midnight/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/death-by-midnight/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/death-by-midnight/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/death-by-midnight/actions/workflows/lint.yml)

💀 Death by Midnight.

Play in your browser:

- [remarkablegames](https://remarkablegames.org/death-by-midnight/)

Or download for desktop:

- [Windows](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/win.zip)
- [Mac](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/mac.zip)
- [Linux](https://github.com/remarkablegames/death-by-midnight/releases/latest/download/linux.tar.bz2)

## Credits

### Art

- [3DModelsCC0](https://3dmodelscc0.itch.io/)
- [Free Visual Novel Backgrounds (Mansion Pack)](https://potat0master.itch.io/free-visual-novel-backgrounds-mansion-pack)
- [Tea Stained Paper Textures](https://majcher.itch.io/tea-stained-paper-textures)
- [Visual Novel Horror Asset Pack](https://kalaverita.itch.io/visual-novel-horror-asset-pack)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)

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

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] [`icon.icns`](https://anyconv.com/png-to-icns-converter/)
- [ ] [`icon.ico`](https://anyconv.com/png-to-ico-converter/)
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

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
