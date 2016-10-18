import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.replace_brick_start \
    import ReplaceBrickStart


class TestVolumeReplaceBrickStart(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = ReplaceBrickStart()
        atom.start("vol1", 'brick1', 'new-brick')
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'replace-brick',
                'vol1', 'brick1', 'new-brick',
                'start', '--mode=script'
            ]
        )
