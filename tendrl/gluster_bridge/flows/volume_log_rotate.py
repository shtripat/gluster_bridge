import json

import etcd
from tendrl.gluster_bridge.atoms.volume.log_rotate import LogRotate


class VolumeLogRotate(object):
    def __init__(self, api_job):
        super(VolumeLogRotate, self).__init__()
        self.api_job = api_job
        self.atom = LogRotate

    def start(self):
        attributes = self.api_job['attributes']
        vol_name = attributes['volname']
        self.atom().start(vol_name)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
