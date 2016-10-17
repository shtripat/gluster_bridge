import json

import etcd
from tendrl.gluster_bridge.atoms.peer.detach import Detach


class PeerDetach(object):
    def __init__(self, api_job):
        super(PeerDetach, self).__init__()
        self.api_job = api_job
        self.atom = Detach

    def start(self):
        attributes = self.api_job['attributes']
        peer = attributes['peer']
        self.atom().start(peer)
        self.api_job['status'] = "finished"
        etcd.Client().write(self.api_job['request_id'],
                            json.dumps(self.api_job))
