import json

import etcd
from tendrl.gluster_bridge.atoms.volume.remove_brick_commit import RemoveBrickCommit


class RemoveBrickCommit(object):
    def __init__(self, api_job):
        super(RemoveBrickCommit, self).__init__()
        self.api_job = api_job
        self.atom = RemoveBrickCommit

    def start(self):
        attributes = json.loads(self.api_job['attributes'].decode('utf-8'))
        vol_name = attributes['volname']
        brick = attributes['brick_name']
        self.atom().start(vol_name, brick)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
