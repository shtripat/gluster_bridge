from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.set'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.set_volume_option import SetVolumeOption


class TestSetVolumeOption(object):

    def test_start(object):
        flow = SetVolumeOption(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "SetVolumeOption",
                "object_type": "volume",
                "status": 'new',
                "message": 'Setting volume option',
                "attributes": {
                    "volname": 'Volume1',
                    "option_name": "option",
                    "option_value": "value"
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with('Volume1', 'option', 'value')
        assert flow.api_job['status'] == "finished"
