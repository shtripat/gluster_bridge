import mock
import subprocess

from tendrl.gluster_bridge.atoms.volume.rebalance_stop import RebalanceStop


class TestVolumeRebalanceStop(object):

    def test_start(object):
        subprocess.call = mock.create_autospec(
            subprocess.call,
            return_value='done'
        )
        atom = RebalanceStop()
        atom.start("vol1",)
        subprocess.call.assert_called_with(
            [
                'gluster', 'volume', 'rebalance',
                'vol1', 'stop', '--mode=script'
            ]
        )
