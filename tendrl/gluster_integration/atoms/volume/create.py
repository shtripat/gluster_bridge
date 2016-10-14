import subprocess


class Create(object):
    def start(self, name, bricks):
        cmd = ['gluster', 'volume', 'create', name]
        cmd.extend(bricks)
        cmd.append('force')
        subprocess.call(cmd)
        subprocess.call(['gluster', 'volume', 'start', name])
