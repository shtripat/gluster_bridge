import json

import etcd
from tendrl.gluster_bridge.atoms.volume.remove_brick_commit \
    import RemoveBrickCommit


class VolumeRemoveBrickCommit(object):
    def __init__(self, api_job):
        super(VolumeRemoveBrickCommit, self).__init__()
        self.api_job = api_job
        self.atom = RemoveBrickCommit

    def start(self):
        attributes = self.api_job['parameters']
        vol_name = attributes['volname']
        brick = attributes['brick_name']
        self.atom().start(vol_name, brick)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
