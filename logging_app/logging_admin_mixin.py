from .services import (
    create_logging_model,
    retrive_logging_model,
    update_logging_model,
    destroy_logging_model
)


class BaseLogModelAdminMixin():
    serializer_log_class = None
    old_obj_serialized_data = None

    def get_model_class_name(self):
        return f'{self.model._meta.app_label}.{self.model._meta.object_name}'

    def get_serializer_log_class(self):
        assert self.serializer_log_class is not None, (
            "'%s' should either include a `serializer_log_class` attribute, "
            % self.__class__.__name__
        )
        return self.serializer_log_class

    def get_object(self, request, object_id, from_field):
        obj = super().get_object(request, object_id, from_field)
        if obj:
            serializer = self.get_serializer_log_class()
            self.old_obj_serialized_data = serializer(instance=obj).data
        return obj


class CreateLogModelAdminMixin(BaseLogModelAdminMixin):
    def log_addition(self, request, object, message):
        serializer = self.get_serializer_log_class()
        create_logging_model(
            request.user,
            self.get_model_class_name(),
            object.id,
            serializer(instance=object).data,
        )
        return super().log_addition(request, object, message)


class RetriveLogModelAdminMixin(BaseLogModelAdminMixin):
    def get_object(self, request, object_id, from_field):
        obj = super().get_object(request, object_id, from_field)
        retrive_logging_model(
            request.user,
            self.get_model_class_name(),
            obj.id,
            self.old_obj_serialized_data
        )
        return obj


class UpdateLogModelAdminMixin(BaseLogModelAdminMixin):

    def log_change(self, request, object, message):
        serializer = self.get_serializer_log_class()
        update_logging_model(
            request.user,
            self.get_model_class_name(),
            object.id,
            self.old_obj_serialized_data,
            serializer(instance=object).data
        )
        return super().log_change(request, object, message)


class DestroyLogModelAdminMixin(BaseLogModelAdminMixin):
    def log_deletion(self, request, object, object_repr):
        serializer = self.get_serializer_log_class()
        destroy_logging_model(
            request.user,
            self.get_model_class_name(),
            object.id,
            serializer(instance=object).data,
        )
        return super().log_deletion(request, object, object_repr)
