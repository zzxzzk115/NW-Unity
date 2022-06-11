# GameShell Tips

Make sure the OS version of your GameShell is 0.5 or newer.

Switch the GPU Driver of your GameShell to Lima if it's not.

## 1. Switch to WebGL project

`File->BuildSettings`

![](./images/1_switch_to_webgl.png)

## 2. Setup Project Settings

`Edit->Project Settings`

![](./images/2_setup_project_settings.png)

Select 'Minimal' template.

## 3. Fix stuck 90% when loading

Unity WebGL use Brotli to compress files by default, it has a bug: stuck at 90% when loading a game.

So, we have to change the default settings:

![](./images/3_fix_loading_bug.png)

## 4. Build

Build, and wait.

## 5. Upload to GameShell

Upload the built output folder to GameShell

## 6. Use NW-Unity to auto packing

```bash
# Install NW-Unity by pip.
sudo pip3 install nwunity

# Package your Unity WebGL files on GameShell.
nwunity -d '/path/to/UnityWebGLDir' -n 'MyGame' -p GameShell
```

