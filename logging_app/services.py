from .models import LoggingModel
from .choices import *


def _list_difference(d_old: dict, d_new: dict) -> dict:
    out_dict = dict()
    for key in d_old.keys():
        if d_old[key] != d_new[key]:
            out_dict[key] = {
                'old': d_old[key],
                'new': d_new[key]
            }
    return out_dict


def create_logging_model(user, model_name, obj_id, obj_dict) -> bool:
    LoggingModel.objects.create(
        user=user,
        model_name=model_name,
        record_id=obj_id,
        data=obj_dict,
        action=CREATE
    )
    return True


def retrive_logging_model(user, model_name, obj_id, obj_dict) -> bool:
    LoggingModel.objects.create(
        user=user,
        model_name=model_name,
        record_id=obj_id,
        data=obj_dict,
        action=RETRIVE
    )
    return True


def update_logging_model(user, model_name, obj_id, obj_old_dict, obj_new_dict) -> bool:
    if obj_old_dict != obj_new_dict:
        LoggingModel.objects.create(
            user=user,
            model_name=model_name,
            record_id=obj_id,
            data=_list_difference(obj_old_dict, obj_new_dict),
            action=UPDATE
        )
    return True


def destroy_logging_model(user, model_name, obj_id, obj_dict) -> bool:
    LoggingModel.objects.create(
        user=user,
        model_name=model_name,
        record_id=obj_id,
        data=obj_dict,
        action=DESTROY
    )
    return True
