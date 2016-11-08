import json

import etcd
from tendrl.gluster_bridge.atoms.volume.rebalance_stop import RebalanceStop


class VolumeRebalanceStop(object):
    def __init__(self, api_job):
        super(VolumeRebalanceStop, self).__init__()
        self.api_job = api_job
        self.atom = RebalanceStop

    def start(self):
        attributes = self.api_job['parameters']
        vol_name = attributes['volname']
        self.atom().start(vol_name)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
