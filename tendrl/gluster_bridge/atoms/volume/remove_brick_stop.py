import subprocess


class RemoveBrickStop(object):
    def start(self, name, brick):
        subprocess.call(['gluster', 'volume', 'remove-brick',
                         name, brick, 'stop',
                         '--mode=script'])
