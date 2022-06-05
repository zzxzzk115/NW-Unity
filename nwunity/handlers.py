import json
import os


data_files = ['escape.js', 'gs_launcher.sh', 'jquery.min.js',
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
        for data_file in data_files:
            if not os.path.exists(os.path.join('data/', data_file)):
                print('Internal Error. Data file' + data_file + 'is missing.')
                return -2
        with open('data/package.json', 'r+') as f:
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
        self.json_data_object['name'] = self.options.Name
        self.json_data_object['window']['width'] = 320
        self.json_data_object['window']['height'] = 240
        self.json_data_object['window']['fullscreen'] = True
        self.json_data_object['window']['resizable'] = False
        self.json_data_object['window']['frame'] = False 
        self.json_data_object['window']['transparent'] = True 
        # print(self.json_data_object)
        return 0