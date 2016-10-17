import subprocess


class Set(object):
    def start(self, name, option, option_value):
        subprocess.call(['gluster', 'volume', 'set',
                        name, option, option_value,
                        '--mode=script'])
