import logging

from tendrl.common.atoms.base_atom import BaseAtom

LOG = logging.getLogger(__name__)


class VolumeStopped(BaseAtom):
    def run(self, parameters):
        path = "/clusters/%s/Volumes/%s" %\
            (
                parameters.get("Tendrl_context.cluster_id"),
                parameters.get("Volume.vol_id")
            )
        etcd_client = parameters['etcd_client']
        volume = etcd_client.read(path)
        for el in volume.children:
            if el.key.split('/')[-1] == "status":
                status = el.value
                if status == "Stopped":
                    return True
                else:
                    LOG.error(
                        "Volume: %s not stopped for cluster: %s" %
                        (
                            parameters.get("Volume.volname"),
                            parameters.get("Tendrl_context.cluster_id")
                        )
                    )
                    return False
        return False
