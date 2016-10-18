from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.remove_brick_start'] = \
    MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.volume_remove_brick_start \
    import VolumeRemoveBrickStart


class TestVolumeRemoveBrickStart(object):

    def test_start(object):
        flow = VolumeRemoveBrickStart(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRemoveBrickStart",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting remove brick for volume',
                "attributes": {
                    "volname": 'Volume1',
                    "brick_name": "brick1"
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1', 'brick1')
        assert flow.api_job['status'] == "finished"
