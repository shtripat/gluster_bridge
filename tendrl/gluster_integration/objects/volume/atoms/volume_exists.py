import logging

from tendrl.common.atoms.base_atom import BaseAtom
from tendrl.gluster_integration.objects.volume import volume

LOG = logging.getLogger(__name__)


class VolumeExists(BaseAtom):
    def run(self, parameters):
        vol = volume.Volume(
            "",
            parameters.get("Volume.vol_id"),
            parameters.get("Tendrl_context.cluster_id")
        )
        vol.refresh()

        if vol.deleted == "" or vol.deleted == "False":
            return True

        LOG.error(
            "Volume: %s does not exist for cluster: %s" %
            (
                parameters.get("Volume.volname"),
                parameters.get("Tendrl_context.cluster_id")
            )
        )
        return False
