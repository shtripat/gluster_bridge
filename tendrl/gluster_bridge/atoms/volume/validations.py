

def volume_not_exists(
    volname,
    brickdetails,
    stripe_count=None,
    replica_count=None,
    arbiter_count=None,
    disperse_count=None,
    disperse_data_count=None,
    redundancy_count=None,
    transport=[],
    force=False
):
    # TODO implement the actual logic to check etcd for and make sure volume
    # getting created doesnt exist already
    return True


def volume_exists(volname):
    # TODO implement the actual logic to check etcd for existence of volume
    return True


def valid_create_data(
    volname,
    brickdetails,
    stripe_count=None,
    replica_count=None,
    arbiter_count=None,
    disperse_count=None,
    disperse_data_count=None,
    redundancy_count=None,
    transport=[],
    force=False
    ):
    if volname == "":
        return False
    if len(brickdetails) == 0:
        return False
    if stripe_count and not isinstance(stripe_count, int):
        return False
    if replica_count and not isinstance(replica_count, int):
        return False
    if arbiter_count and not isinstance(arbiter_count, int):
        return False
    if disperse_count and not isinstance(disperse_count, int):
        return False
    if disperse_data_count and not isinstance(disperse_data_count, int):
        return False
    if redundancy_count and not isinstance(redundancy_count, int):
        return False
    if len(transport) > 0:
        for value in transport:
            if value not in ['tcp', 'rdma']:
                return False

    return True


def valid_delete_data(volname):
    return valid_volume_name(volname)


def valid_start_data(volname):
    return valid_volume_name(volname)


def volume_stopped(volname):
    # TODO implement the actual logic to check etcd for state of the volume
    return True


def valid_stop_data(volname):
    return valid_volume_name(volname)


def volume_started(volname):
    # TODO implement the actual logic to check etcd for state of volume
    return True


def volume_exists_for_set(volname, option_name, option_value):
    return volume_exists(volname)


def valid_set_option_data(volname, option_name, option_value):
    if volname == "" or option_name == "" or option_value is None:
        return False
    return True


def volume_exists_for_add_brick(volname, brickdetails):
    return volume_exists(volname)


def valid_brick_details(volname, brickdetails):
    if not isinstance(brickdetails, list):
        return False
    if len(brickdetails) == 0:
        return False
    return True


def volume_exists_for_remove_brick(volname, brick_name):
    return volume_exists(volname)


def valid_brick_detail(volname, brick_name):
    if volname == "":
        return False
    if brick_name == "":
        return False
    return True


def valid_volume_state_for_remove_brick(volname, brick_name):
    # TODO check etcd to find if there are any active opertaions on the volume
    # If operations like rebalance etc running, remove brick shouldnt be
    # allowed
    return True


def remove_brick_running(volname, brick_name):
    # TODO check etcd to find if actually there is a remove brick running on
    # volume for the said brick
    return True


def remove_brick_completed(volname, brick_name):
    # TODO check etcd to find if the remove brick operation is completed on
    # the volume for said brick
    return True


def volume_exists_for_replace_brick(volname, source_brick, destination_brick):
    return volume_exists(volname)


def valid_brick_detail_for_replace(volname, source_brick, destination_brick):
    if volname == "" or source_brick == "" or destination_brick == "":
        return False
    return True


def valid_replace_brick_state(volname, source_brick, destination_brick):
    # TODO check etcd to find if valid replace brick operation available for
    # volume for commit
    return True


def volume_exists_for_rebalance(volname, fix_layout=False, force=False):
    return volume_exists(volname)


def valid_rebalance_data(volname, fix_layout=False, force=False):
    return valid_volume_name(volname)


def rebalance_not_started(volname, fix_layout=False, force=False):
    # TODO check etcd to find if rebalance is not already running for volume
    # If running return False
    return True


def valid_rebalance_stop_data(volname):
    return valid_volume_name(volname)


def rebalance_started(volname):
    # TODO check etcd to find if rebalance is already running for volume. If
    # not return False
    return True


def valid_volume_name(volname):
    if volname == "":
        return False
    return True
