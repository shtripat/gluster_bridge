import subprocess


class RebalanceStart(object):
    def start(self, name, force=False, fix_layout=False):
        cmd = ['gluster', 'volume', 'rebalance', name]
        if fix_layout:
            cmd.append('fix-layout')
        cmd.append('start')
        if force:
            cmd.append('force')
        cmd.append('--mode=script')
        subprocess.call(cmd)
