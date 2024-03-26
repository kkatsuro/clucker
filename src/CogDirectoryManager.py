from PySide6.QtCore import QFileSystemWatcher

from data_manager import global_config

import os

'''
List of all cog directories, and is watching for new cogs.
We need this to not to have watcher for each instance window.
'''

# @todo: Currently this function is not certain, we probably should add some way of better identification.
# For example, __init__.py common for a python package, but __init__ with:
# `def setup(bot):
#     bot.add_cogs(our_cog)`
# is not.
def is_cog_path(path):
    '''Checks if directory is (probably) a cog directory.'''
    # info.json may not be needed for cog to be loaded, but it is standard file too.
    return '__init__.py' in os.listdir(path)

# this should not be imported, import CogDirManager
class __CogDirectoryManager:
    # this needs to be inited by hand, at start of everything - gui.py
    def init(self):
        self.watcher = QFileSystemWatcher()

        self.directories = global_config['cog-directories']

        for path in self.directories:
            self.watcher.addPath(path)

    def get_cogs(self):
        cogs_list = set()
        for directory in self.directories:
            try:
                cogs_list |= { node.path for node in os.scandir(directory) if
                               node.is_dir() and is_cog_path(node.path) }
            except Exception as e:
                print(f'error: something wrong when listing {directory}')  # @debug statement
                print(e)
                continue

        return list(cogs_list)
    
    # @todo: look at the name
    def add_directory_dont_use_it_because_it_needs_to_update_too_and_it_does_not(self, directory):
        self.cog_directories.append(directory)

# CDM sounds like a great name
CogDirManager = __CogDirectoryManager()
