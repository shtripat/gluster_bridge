from tendrl.commons.event import Event
from tendrl.commons.message import Message
from tendrl.commons import objects
from tendrl.gluster_integration.sds_sync import \
    rebalance_status as rebal_stat


class SyncRebalanceStatus(objects.BaseAtom):
    def __init__(self, *args, **kwargs):
        super(SyncRebalanceStatus, self).__init__(*args, **kwargs)

    def run(self):
        volumes = NS.gluster.objects.Volume().load_all()
        for volume in volumes:
            if volume.vol_type == "Distribute":
                status = rebal_stat.get_rebalance_status(
                    volume.name
                )
                if status:
                    rebal_status = status.replace(" ", "_")
                else:
                    rebal_status = "not_started"
                volume.rebal_status=rebal_status
                volume.save()

        return True
