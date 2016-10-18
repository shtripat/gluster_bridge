import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.create import Create


class TestCreateVolume(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = Create()
        atom.start("vol1", ['brick1', 'brick2'])
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'start',
                'vol1', '--mode=script'
            ]
        )
