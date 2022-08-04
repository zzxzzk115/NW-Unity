import optparse
from nwunity.handlers import NormalHandler, GameShellHandler


def main():
    usage = "%prog -n/--name <game name> -d/--directory <target dir>"
    parser = optparse.OptionParser(usage=usage, version="%prog v0.2.23")
    parser.add_option('-n', '--name', dest='Name', type='string', help="Set the name of your game, default is 'Untitled-Game'.", default='Untitled-Game')
    parser.add_option('-d', '--directory', dest='Dir', type='string', help='Set the root directory of your Unity WebGL files, default is current working directory.', default='.')
    parser.add_option('--width', dest='Width', type='int', help='Set the width of your game window, default is 1024.', default=1024)
    parser.add_option('--height', dest='Height', type='int', help='Set the height of your game window, default is 768.', default=768)
    parser.add_option('--fullscreen', action='store_true', dest='FullScreen', help='Set full screen mode on, default is off.', default=False)
    parser.add_option('--noframe', action='store_true', dest='NoFrame', help='Hide window frame title, default is show.', default=False)
    parser.add_option('--resizable', action='store_true', dest='Resizable', help='Set resizable mode on, default is off.', default=False)
    parser.add_option('--transparent', action='store_false', dest='Transparent', help='Set transparent mode on, default is off.', default=True)
    parser.add_option('-p', '--platform', dest='Platform', type='string', help='Set platform, default is Normal(PC, Linux, MacOS...). Options: GameShell.', default='Normal')
    parser.add_option('-i', '--icon', dest='Icon', type='string', help='Set the icon of the game.', default=None)
    options, args = parser.parse_args()
    if options.Platform == 'Normal':
        handler = NormalHandler(options, args)
    else:
        handler = GameShellHandler(options, args)
    ret, success_info = handler.handle()
    if ret != 0:
        print('Error code: ' + str(ret))
    else:
        print(success_info)
    return ret