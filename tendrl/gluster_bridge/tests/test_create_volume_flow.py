from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.create'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.create_volume import CreateVolume


class TestCreateVolume(object):

    def test_start(object):
        flow = CreateVolume(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "CreateVolume",
                "object_type": "volume",
                "status": 'new',
                "message": 'Creating cluster',
                "attributes": {
                    "volname": 'Volume1',
                    "brickdetails": ["mntpath"]
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1', ['mntpath'])
        assert flow.api_job['status'] == "finished"
