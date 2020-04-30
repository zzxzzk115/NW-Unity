# GameShell-Unity3D-WebGL

## How to use?
1. Copy `TemplateData`, `index.html`, `package.json`;
2. Paste at your Unity3D-WebGL game's root directory;
3. Edit `index.html` and replace this:
```
UnityLoader.instantiate("unityContainer", "Build/catmario_webgl.json");
```
to:
```
UnityLoader.instantiate("unityContainer", "Build/{YOUR GAME}.json");
```
4. Upload your game to GameShell, for example:`/home/cpi/games/Unity3D/yourgame`
5. Create a new directory at `/home/cpi/apps/Menu/`, for example `/home/cpi/apps/Menu/Unity3D_Games`
6. Create a new directory at `/home/cpi/apps/Menu/Unity3D_Games`, for example `/home/cpi/apps/Menu/Unity3D_Games/yourgame`
7. Create a new .sh script at `/home/cpi/apps/Menu/Unity3D_Games/yourgame`, for example `/home/cpi/apps/Menu/Unity3D_Games/yourgame/yourgame.sh`, the format refers to game.sh, just need to change the game folder.
8. Done! just refresh the menu and have fun!

**important**
9. Replace `nw.js-folder->lib->libffmpeg.so` with my `libffmpeg.so`. If you don't replace it, the game won't support audio!
10. DO NOT use Lima Driver!
