import etcd
import logging

from tendrl.gluster_integration.config import TendrlConfig

LOG = logging.getLogger(__name__)
config = TendrlConfig()


class NamedVolumeExists(object):
    def run(self, parameters):
        path = "/clusters/%s/Volumes" %\
            parameters.get('Tendrl_context.cluster_id')
        etcd_kwargs = {
            'host': config.get("common", "etcd_connection"),
            'port': int(config.get("common", "etcd_port"))
        }
        client = etcd.Client(**etcd_kwargs)
        volumes = client.read(path)
        for volume in volumes.children:
            volumeIns = client.read(volume.key)
            ret_val = False
            for el in volumeIns.children:
                if el.key.split('/')[-1] == "name":
                    if el.value == parameters.get("Volume.volname"):
                        ret_val = True
                if el.key.split('/')[-1] == "deleted" and el.value == "True":
                    ret_val = ret_val and False
            if ret_val:
                return True

        LOG.error(
            "Volume: %s does not exist for cluster: %s" %
            (
                parameters.get("Volume.volname"),
                parameters.get("Tendrl_context.cluster_id")
            )
        )
        return False
