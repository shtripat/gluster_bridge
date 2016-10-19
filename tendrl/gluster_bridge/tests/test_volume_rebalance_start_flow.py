from mock import MagicMock
import sys

sys.modules['tendrl.gluster_bridge.atoms.volume.rebalance_start'] = MagicMock()
sys.modules['etcd'] = MagicMock()
from tendrl.gluster_bridge.flows.volume_rebalance_start \
    import VolumeRebalanceStart


class TestVolumeRebalanceStart(object):

    def test_start(object):
        flow = VolumeRebalanceStart(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRebalanceStart",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting rebalance for volume',
                "attributes": {
                    "volname": 'Volume1',
                    "force": True,
                    "fix_layout": True
                },
                "errors": {}
            })
        flow.start()
        flow.atom().start.assert_called_with(
            'Volume1',
            force=True,
            fix_layout=True
        )
        assert flow.api_job['status'] == "finished"

        flow1 = VolumeRebalanceStart(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRebalanceStart",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting rebalance for volume',
                "attributes": {
                    "volname": 'Volume1',
                    "force": True,
                    "fix_layout": False
                },
                "errors": {}
            })
        flow1.start()
        flow1.atom().start.assert_called_with(
            'Volume1',
            force=True,
            fix_layout=False
        )
        assert flow.api_job['status'] == "finished"

        flow2 = VolumeRebalanceStart(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRebalanceStart",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting rebalance for volume',
                "attributes": {
                    "volname": 'Volume1',
                    "force": False,
                    "fix_layout": False
                },
                "errors": {}
            })
        flow2.start()
        flow2.atom().start.assert_called_with(
            'Volume1',
            force=False,
            fix_layout=False
        )
        assert flow.api_job['status'] == "finished"

        flow3 = VolumeRebalanceStart(
            {
                "request_id": "49fa2adde8a6e98591f0f5cb4bc5f44d",
                "sds_type": "gluster",
                "flow": "VolumeRebalanceStart",
                "object_type": "volume",
                "status": 'new',
                "message": 'Starting rebalance for volume',
                "attributes": {
                    "volname": 'Volume1',
                    "force": False,
                    "fix_layout": True
                },
                "errors": {}
            })
        flow3.start()
        flow3.atom().start.assert_called_with(
            'Volume1',
            force=False,
            fix_layout=True)
        assert flow.api_job['status'] == "finished"
