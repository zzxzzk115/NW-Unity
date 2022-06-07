# NW-Unity

![PyPI - Wheel](https://img.shields.io/pypi/wheel/nwunity) ![version](https://img.shields.io/badge/version-0.2.5-yellow)

NW-Unity is a tool for auto packing your Unity WebGL output files to a NW.js executable file.

## Quick Usage

Install by pip on Windows:
```powershell
pip install nwunity
```

Install by pip on Linux:
```bash
sudo pip install nwunity
```

Pack your game:
```bash
# Package your Unity WebGL game(resolution is 320*240, full screen mode is on) on PC, Linux, or MacOS.
nwunity -d /path/to/UnityWebGLDir -n 'MyGame' --width 320 --height 240 --fullscreen

# Package your Unity WebGL files on GameShell.
nwunity -d /path/to/UnityWebGLDir -n 'MyGame' -p GameShell
```

## How to use

NW-Unity is easy to use. You can install  it by pip.

### Install by pip

```bash
python -m pip install nwunity
```

### Parameters

You can use `nwunity -h` or `nwunity --help` to get help.

| Format           | Parameter Explain                                            |
| ---------------- | ------------------------------------------------------------ |
| -d   --directory | Set the root directory of your Unity WebGL files, default is current working directory. |
| -n   --name      | Set the name of your game, default is 'Untitled-Game'.       |
| --width          | Set the width of your game window, default is 1024.          |
| --height         | Set the height of your game window, default is 768.          |
| --fullscreen     | Set full screen mode on, default is off.                     |
| --noframe        | Hide window frame title, default is show.                    |
| --resizable      | Set resizable mode on, default is off.                       |
| --transparent    | Set transparent mode on, default is off.                     |
| -p   --platform  | Set platform, default is normal(PC, Linux, MacOS...). Options: GameShell. |

### GameShell tips

Make sure the OS version of your GameShell is 0.5 or newer.

Switch the GPU Driver of your GameShell to Lima if it's not.

## License

The project is under the [MIT](./LICENSE) license.

