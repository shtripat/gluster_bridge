from tendrl.commons.config import load_config
from tendrl.commons.etcdobj.etcdobj import Server as etcd_server
from tendrl.commons.persistence.etcd_persister import EtcdPersister
from tendrl.gluster_integration.persistence.sync_objects import SyncObject

config = load_config(
    "gluster-integration",
    "/etc/tendrl/gluster-integration/gluster-integration.yaml"
)


class GlusterIntegrationEtcdPersister(EtcdPersister):
    def __init__(self):
        etcd_kwargs = {
            'port': int(config["configuration"]["etcd_port"]),
            'host': config["configuration"]["etcd_connection"]
        }
        self._store = etcd_server(etcd_kwargs=etcd_kwargs)
        super(GlusterIntegrationEtcdPersister, self).__init__(
            self._store.client
        )

    def update_sync_object(self, updated, cluster_id, data):
        self._store.save(
            SyncObject(
                updated=updated,
                cluster_id=cluster_id,
                data=data
            )
        )

    def update_peer(self, peer):
        self._store.save(peer)

    def update_volume(self, vol):
        self._store.save(vol)

    def update_brick(self, brick):
        self._store.save(brick)

    def update_volume_options(self, vol_options):
        self._store.save(vol_options)

    def save_events(self, events):
        for event in events:
            self._store.save(event)

    def update_tendrl_context(self, context):
        self._store.save(context)

    def update_tendrl_definitions(self, definition):
        self._store.save(definition)
