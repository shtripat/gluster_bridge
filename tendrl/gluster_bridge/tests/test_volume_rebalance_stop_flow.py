from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.rebalance_stop'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.volume_rebalance_stop \
    import VolumeRebalanceStop


class TestVolumeRebalanceStop(object):

    def test_start(object):
        flow = VolumeRebalanceStop(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRebalanceStop",
                "object_type": "volume",
                "status": 'new',
                "message": 'Stopping rebalance for volume',
                "attributes": {
                    "volname": 'Volume1',
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1')
        assert flow.api_job['status'] == "finished"
