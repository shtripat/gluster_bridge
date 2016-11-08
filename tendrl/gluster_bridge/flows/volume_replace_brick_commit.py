import json

import etcd
from tendrl.gluster_bridge.atoms.volume.replace_brick_commit \
    import ReplaceBrickCommit


class VolumeReplaceBrickCommit(object):
    def __init__(self, api_job):
        super(VolumeReplaceBrickCommit, self).__init__()
        self.api_job = api_job
        self.atom = ReplaceBrickCommit

    def start(self):
        attributes = self.api_job['parameters']
        vol_name = attributes['volname']
        brick = attributes['source_brick']
        new_brick = attributes['destination_brick']
        self.atom().start(vol_name, brick, new_brick)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
