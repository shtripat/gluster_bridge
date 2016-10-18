from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.add_brick'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.add_volume_brick import AddVolumeBrick


class TestAddVolumeBrick(object):

    def test_start(object):
        flow = AddVolumeBrick(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "AddVolumeBrick",
                "object_type": "volume",
                "status": 'new',
                "message": 'Adding brick to volume',
                "attributes": {
                    "volname": 'Volume1',
                    "brickdetails": ["brick1", "brick2"]
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1', ["brick1", "brick2"])
        assert flow.api_job['status'] == "finished"
