from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.start'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.start_volume import StartVolume


class TestStartVolume(object):

    def test_start(object):
        flow = StartVolume(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "StartVolume",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting volume',
                "attributes": {
                    "volname": 'Volume1',
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1')
        assert flow.api_job['status'] == "finished"
