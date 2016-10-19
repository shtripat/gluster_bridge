import json

import etcd
from tendrl.gluster_bridge.atoms.volume.rebalance_start import RebalanceStart


class VolumeRebalanceStart(object):
    def __init__(self, api_job):
        super(VolumeRebalanceStart, self).__init__()
        self.api_job = api_job
        self.atom = RebalanceStart

    def start(self):
        attributes = self.api_job['attributes']
        vol_name = attributes['volname']
        v_fix_layout = attributes.get('fix_layout')
        v_force = attributes.get('force')
        self.atom().start(
            vol_name,
            force=v_force,
            fix_layout=v_fix_layout
        )
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
