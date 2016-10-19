import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.replace_brick_commit \
    import ReplaceBrickCommit


class TestVolumeReplaceBrickCommit(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = ReplaceBrickCommit()
        atom.start("vol1", 'brick1', 'new-brick')
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'replace-brick',
                'vol1', 'brick1', 'new-brick',
                'commit', 'force', '--mode=script'
            ]
        )
