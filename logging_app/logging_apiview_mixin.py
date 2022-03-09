from rest_framework.permissions import IsAuthenticated

from .services import (
    create_logging_model,
    retrive_logging_model,
    update_logging_model,
    destroy_logging_model
)


class BaseAPILoggingMixin():
    model = None
    serializer_log_class = None
    old_obj_serialized_data = None
    permission_classes = [IsAuthenticated, ]

    def get_model_class_name(self):
        model_class = self.get_model_class()
        return f'{model_class._meta.app_label}.{model_class._meta.object_name}'

    def get_model_class(self):
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            % self.__class__.__name__
        )
        return self.model

    def get_serializer_log_class(self):
        assert self.serializer_log_class is not None, (
            "'%s' should either include a `serializer_log_class` attribute, "
            % self.__class__.__name__
        )
        return self.serializer_log_class

    def get_object(self):
        obj = super().get_object()
        serializer = self.get_serializer_log_class()
        self.old_obj_serialized_data = serializer(instance=obj).data
        return obj


class CreateAPILoggingMixin(BaseAPILoggingMixin):
    def perform_create(self, serializer):
        serializer_log_class = self.get_serializer_log_class()
        obj = serializer.save()
        create_logging_model(
            self.request.user,
            self.get_model_class_name(),
            obj.id,
            serializer_log_class(instance=obj).data,
        )


class RetriveAPILoggingMixin(BaseAPILoggingMixin):
    def get_object(self):
        obj = super().get_object()
        retrive_logging_model(
            self.request.user,
            self.get_model_class_name(),
            obj.id,
            self.old_obj_serialized_data
        )
        return obj


class UpdateAPILoggingMixin(BaseAPILoggingMixin):
    def perform_update(self, serializer):
        serializer_log_class = self.get_serializer_log_class()
        obj = serializer.save()
        update_logging_model(
            self.request.user,
            self.get_model_class_name(),
            obj.id,
            self.old_obj_serialized_data,
            serializer_log_class(instance=obj).data
        )


class DestroyAPILoggingMixin(BaseAPILoggingMixin):
    def perform_destroy(self, instance):
        serializer_log_class = self.get_serializer_log_class()
        destroy_logging_model(
            self.request.user,
            self.get_model_class_name(),
            instance.id,
            serializer_log_class(instance=instance).data
        )
        return super().perform_destroy(instance)


class RetrieveUpdateDestroyAPILoggingMixin(
        RetriveAPILoggingMixin, UpdateAPILoggingMixin, DestroyAPILoggingMixin):
    pass
