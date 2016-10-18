import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.set import Set


class TestSetVolumeOption(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = Set()
        atom.start("vol1", 'option', 'value')
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'set',
                'vol1', 'option', 'value',
                '--mode=script'
            ]
        )
