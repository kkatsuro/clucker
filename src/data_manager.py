import json

global_config = None
CONFIG_FILE = 'config.json'

# @todo: Is this a proper way of handling config?
def load_config():
    global global_config
    with open(CONFIG_FILE, 'r') as f:
        global_config = json.loads(f.read())

def save_config():
    global global_config
    with open(CONFIG_FILE, 'w') as f:
         f.write(json.dumps(global_config, indent=4))

def colorscheme():
    global global_config
    return global_config['colorschemes'].get(global_config['colorscheme'], '')

load_config()
