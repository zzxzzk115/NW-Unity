#!/usr/bin/env python
import optparse
from handlers import NormalHandler, GameShellHandler

def main():
    usage = "%prog -n/--name <game name>"
    parser = optparse.OptionParser(usage)
    parser.add_option('-n', '--name', dest='Name', type='string', help="Set the name of your game, default is 'Untitled-Game'.", default='Untitled-Game')
    parser.add_option('-d', '--directory', dest='Dir', type='string', help='Set the root directory of your Unity WebGL files, default is current working directory.', default='.')
    parser.add_option('--width', dest='Width', type='int', help='Set the width of your game window, default is 1024.', default=1024)
    parser.add_option('--height', dest='Height', type='int', help='Set the height of your game window, default is 768.', default=768)
    parser.add_option('--fullscreen', action='store_true', dest='FullScreen', help='Set full screen mode on, default is off.', default=False)
    parser.add_option('-p', '--platform', dest='Platform', type='string', help='Set platform, default is Normal(PC, Linux, MacOS...). Options: GameShell.', default='Normal')
    options, args = parser.parse_args()
    if options.Platform == 'Normal':
        sucessInfo = 'Done. Now you can use Nw.js to run your game!'
        handler = NormalHandler(options, args)
    else:
        sucessInfo = 'Done.'
        handler = GameShellHandler(options, args)
    ret = handler.handle()
    if ret != 0:
        print('Exit code: ' + str(ret))
    else:
        print(sucessInfo)
    return ret

if __name__ == '__main__':
    main()