# GameShell Tips

Make sure the OS version of your GameShell is 0.5 or newer.

Switch the GPU Driver of your GameShell to Lima if it's not.

## 1. Upgrade graphics

Following instructions are from https://github.com/zzxzzk115/GameShell-Scripts :

If you are in China, please run this command on GameShell first:

```bash
sudo sh -c "sed -i \"/# GitHub520 Host Start/Q\" /etc/hosts && curl https://raw.hellogithub.com/hosts >> /etc/hosts"
```

Upgrade graphics:

```bash
bash <(curl -s https://raw.githubusercontent.com/zzxzzk115/GameShell-Scripts/main/upgrade_graphics.sh)
```

## 2. Switch to WebGL project

`File->BuildSettings`

![](./images/1_switch_to_webgl.png)

## 3. Setup Project Settings

`Edit->Project Settings`

![](./images/2_setup_project_settings.png)

Select 'Minimal' template.

## 4. Fix stuck 90% when loading

Unity WebGL use Brotli to compress files by default, it has a bug: stuck at 90% when loading a game.

So, we have to change the default settings:

![](./images/3_fix_loading_bug.png)

## 5. Build

Build, and wait.

## 6. Upload to GameShell

Upload the built output folder to GameShell

## 7. Use NW-Unity to auto packing

```bash
# Install NW-Unity by pip.
sudo pip3 install nwunity

# Package your Unity WebGL files on GameShell.
nwunity -d '/path/to/UnityWebGLDir' -n 'MyGame' -p GameShell
```

