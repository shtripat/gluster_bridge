import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.remove_brick_commit \
    import RemoveBrickCommit


class TestVolumeRemoveBrickCommit(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = RemoveBrickCommit()
        atom.start("vol1", 'brick1')
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'remove-brick',
                'vol1', 'brick1', 'commit',
                '--mode=script'
            ]
        )
