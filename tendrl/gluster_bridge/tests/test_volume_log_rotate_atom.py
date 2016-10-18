import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.log_rotate import LogRotate


class TestVolumeLogRotate(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = LogRotate()
        atom.start("vol1")
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'log',
                'rotate', 'vol1', '--mode=script'
            ]
        )
