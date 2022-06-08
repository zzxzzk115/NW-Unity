import json
import os
import shutil


data_files = ['escape.js', 'game_launcher_template.sh', 'jquery.min.js',
    'libffmpeg.so', 'package.json', 'style.css']
file_full_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(file_full_path, 'data')

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
            if not os.path.exists(os.path.join(data_path, data_file)):
                print('Internal Error. Data file [' + data_file + '] is missing.')
                return -3
        shutil.copy(os.path.join(data_path, 'escape.js'), os.path.join(self.dir, 'escape.js'))
        shutil.copy(os.path.join(data_path, 'jquery.min.js'), os.path.join(self.dir, 'jquery.min.js'))
        shutil.copy(os.path.join(data_path, 'style.css'), os.path.join(self.dir, 'style.css'))
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
        with open(os.path.join(data_path, 'package.json') , 'r') as f:
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

        shutil.copy(os.path.join(data_path, 'libffmpeg.so') , os.path.join(self.nw_lib_path, 'libffmpeg.so'))

        unity_games_path = os.path.join(self.games_path, 'Unity')
        if not os.path.exists(unity_games_path):
            os.makedirs(unity_games_path)
        game_path = os.path.join(unity_games_path, self.Name)
        if not os.path.exists(game_path):
            os.makedirs(game_path)
        with open(os.path.join(data_path, 'game_launcher_template.sh'), 'r') as f:
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