#!/usr/bin/env python
import optparse
import json
import os
import shutil


data_files = ['escape.js', 'game_launcher_template.sh', 'jquery.min.js',
    'libffmpeg.so', 'package.json', 'style.css']


class BaseHandler:
    def __init__(self, options, args):
        self.options = options
        self.args = args
        return

    def handle(self):
        # print('Options = ' + str(self.options))
        dir = os.path.abspath(self.options.Dir)
        if not os.path.exists(dir):
            print('Error. Target directory is not exists.')
            return -1
        self.dir = dir
        indexFilePath = os.path.join(dir, 'index.html')
        if not os.path.exists(indexFilePath):
            print('Error. index.html is not found.')
            return -2
        for data_file in data_files:
            if not os.path.exists(os.path.join('data/', data_file)):
                print('Internal Error. Data file [' + data_file + '] is missing.')
                return -3
        shutil.copy('data/escape.js', os.path.join(self.dir, 'escape.js'))
        shutil.copy('data/jquery.min.js', os.path.join(self.dir, 'jquery.min.js'))
        shutil.copy('data/style.css', os.path.join(self.dir, 'style.css'))
        with open(indexFilePath, 'r') as f:
            data = f.read()
            data = data.replace('</head>', '''
  <script src="jquery.min.js"></script>
  <script src="escape.js"></script>
  <link rel="stylesheet" href="style.css">
  </head>
            ''')
        with open(indexFilePath, 'w') as f:
            f.write(data)
        with open('data/package.json', 'r') as f:
            json_data_string = f.read()
            self.json_data_object = json.loads(json_data_string)
        return 0

    
    def write_package_json(self, output):
        with open(output, 'w') as f:
            f.write(json.dumps(self.json_data_object, indent=4))
        return


class NormalHandler(BaseHandler):
    def __init__(self, options, args):
        BaseHandler.__init__(self, options, args)
        return

    def handle(self):
        ret = super().handle()
        if ret != 0:
            return ret
        
        self.json_data_object['name'] = self.options.Name
        self.json_data_object['window']['width'] = self.options.Width
        self.json_data_object['window']['height'] = self.options.Height
        self.json_data_object['window']['fullscreen'] = self.options.FullScreen
        self.json_data_object['window']['resizable'] = self.options.Resizable
        self.json_data_object['window']['frame'] = not self.options.NoFrame 
        self.json_data_object['window']['transparent'] = self.options.Transparent 
        # print(self.json_data_object)
        super().write_package_json(os.path.join(self.dir, 'package.json'))
        return 0


class GameShellHandler(BaseHandler):
    def __init__(self, options, args):
        BaseHandler.__init__(self, options, args)
        return

    def handle(self):
        ret = super().handle()
        if ret != 0:
            return ret

        self.home_path = os.path.expanduser('~')
        self.apps_path = os.path.join(self.home_path, 'apps')
        self.games_path = os.path.join(self.home_path, 'games')
        if not os.path.exists(self.apps_path) or not os.path.exists(self.games_path):
            print('Error. ~/apps or ~/games not found! Please run nwunity on GameShell!')
            return - 4

        self.nw_root_path = os.path.join(self.apps_path, 'nwjs-sdk-v0.27.6-linux-arm')
        if not os.path.exists(self.nw_root_path):
            print('Error. ~/apps/nwjs-sdk-v0.27.6-linux-arm not found! You may need to fix it by reinstalling clockwork os.')
            return -5
        
        self.nw_lib_path = os.path.join(self.nw_root_path, 'lib')
        if not os.path.exists(self.nw_lib_path):
            print('Error. ~/apps/nwjs-sdk-v0.27.6-linux-arm/lib not found!')
            return -6

        shutil.copy('data/libffmpeg.so', os.path.join(self.nw_lib_path, 'libffmpeg.so'))

        unity_games_path = os.path.join(self.games_path, 'Unity')
        if not os.path.exists(unity_games_path):
            os.makedirs(unity_games_path)
        game_path = os.path.join(unity_games_path, self.Name)
        if not os.path.exists(game_path):
            os.makedirs(game_path)
        with open('data/game_launcher_template.sh', 'r') as f:
            launcher_template_data = f.read()
        menu_path = os.path.join(self.apps_path, 'Menu')
        game_menu_path = os.path.join(menu_path, 'UnityGames')
        if not os.path.exists(game_menu_path):
            os.makedirs(game_menu_path) 
        with open(os.path.join(game_menu_path, self.Name + '.sh')) as f:
            game_launcher = launcher_template_data.replace('{GAME_NAME}', self.Name)
            f.write(game_launcher)
        
        self.json_data_object['name'] = self.options.Name
        self.json_data_object['window']['width'] = 320
        self.json_data_object['window']['height'] = 240
        self.json_data_object['window']['fullscreen'] = True
        self.json_data_object['window']['resizable'] = False
        self.json_data_object['window']['frame'] = False 
        self.json_data_object['window']['transparent'] = True 
        # print(self.json_data_object)
        super().write_package_json(os.path.join(self.dir, 'package.json'))
        shutil.copy(self.dir, game_path)
        return 0


def main():
    usage = "%prog -n/--name <game name> -d/--directory <target dir>"
    parser = optparse.OptionParser(usage)
    parser.add_option('-n', '--name', dest='Name', type='string', help="Set the name of your game, default is 'Untitled-Game'.", default='Untitled-Game')
    parser.add_option('-d', '--directory', dest='Dir', type='string', help='Set the root directory of your Unity WebGL files, default is current working directory.', default='.')
    parser.add_option('--width', dest='Width', type='int', help='Set the width of your game window, default is 1024.', default=1024)
    parser.add_option('--height', dest='Height', type='int', help='Set the height of your game window, default is 768.', default=768)
    parser.add_option('--fullscreen', action='store_true', dest='FullScreen', help='Set full screen mode on, default is off.', default=False)
    parser.add_option('--noframe', action='store_true', dest='NoFrame', help='Hide window frame title, default is show.', default=False)
    parser.add_option('--resizable', action='store_true', dest='Resizable', help='Set resizable mode on, default is off.', default=False)
    parser.add_option('--transparent', action='store_false', dest='Transparent', help='Set transparent mode on, default is off.', default=True)
    parser.add_option('-p', '--platform', dest='Platform', type='string', help='Set platform, default is Normal(PC, Linux, MacOS...). Options: GameShell.', default='Normal')
    options, args = parser.parse_args()
    if options.Platform == 'Normal':
        sucessInfo = 'Done. Now you can use NW.js to run your game!'
        handler = NormalHandler(options, args)
    else:
        sucessInfo = 'Done.'
        handler = GameShellHandler(options, args)
    ret = handler.handle()
    if ret != 0:
        print('Error code: ' + str(ret))
    else:
        print(sucessInfo)
    return ret

if __name__ == '__main__':
    main()