# GameShell-Unity3D-WebGL

## How to use?
1. copy TemplateData, index.html, package.json;
2. paste at your Unity3D-WebGL game's root directory;
3. replace this:
```
UnityLoader.instantiate("unityContainer", "Build/catmario_webgl.json");
```
to:
```
UnityLoader.instantiate("unityContainer", "Build/{YOUR GAME}.json");
```
4. upload your game to GameShell, for example:/home/cpi/games/Unity3D/yourgame
5. create a new directory at /home/cpi/apps/Menu/, for example /home/cpi/apps/Menu/Unity3D_Games
6. create a new directory at /home/cpi/apps/Menu/Unity3D_Games, for example /home/cpi/apps/Menu/Unity3D_Games/yourgame
7. create a new .sh script at /home/cpi/apps/Menu/Unity3D_Games/yourgame, for example /home/cpi/apps/Menu/Unity3D_Games/yourgame/yourgame.sh, the format refers to game.sh, just need to change the game folder.
8. done.just refresh the menu and have fun!

** important **
9. replace nw.js-folder->lib->libffmpeg.so with my libffmpeg.so. If you don't replace it, the game won't support audio!
