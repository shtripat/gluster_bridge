from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.stop'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.stop_volume import StopVolume


class TestStopVolume(object):

    def test_start(object):
        flow = StopVolume(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "StopVolume",
                "object_type": "volume",
                "status": 'new',
                "message": 'Stoping volume',
                "attributes": {
                    "volname": 'Volume1',
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1')
        assert flow.api_job['status'] == "finished"