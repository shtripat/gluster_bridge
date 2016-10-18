import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.rebalance_start import RebalanceStart


class TestVolumeRebalanceStart(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = RebalanceStart()

        atom.start("vol1", True, True)
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'rebalance',
                'vol1', 'fix-layout', 'start',
                'force', '--mode=script'
            ]
        )

        atom.start("vol1", True, False)
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'rebalance',
                'vol1', 'start', 'force',
                '--mode=script'
            ]
        )

        atom.start("vol1", False, False)
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'rebalance',
                'vol1', 'start', '--mode=script'
            ]
        )

        atom.start("vol1", False, True)
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'rebalance',
                'vol1', 'fix-layout', 'start',
                '--mode=script'
            ]
        )
