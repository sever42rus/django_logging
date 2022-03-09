from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .services import (
    create_logging_model,
    retrive_logging_model,
    update_logging_model,
    destroy_logging_model
)


@method_decorator(login_required, name='dispatch')
class BaseLoggingMixin():
    model = None
    serializer_log_class = None
    old_obj_serialized_data = None

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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


class CreateViewLoggigMixin(BaseLoggingMixin):
    def form_valid(self, form):
        serializer_log_class = self.get_serializer_log_class()
        http_rest = super().form_valid(form)
        create_logging_model(
            self.request.user,
            self.get_model_class_name(),
            self.object.id,
            serializer_log_class(instance=self.object).data,
        )
        return http_rest


class RetriveLoggingMixin(BaseLoggingMixin):
    def get_object(self):
        obj = super().get_object()
        retrive_logging_model(
            self.request.user,
            self.get_model_class_name(),
            obj.id,
            self.old_obj_serialized_data
        )
        return obj


class UpdateLoggingMixin(BaseLoggingMixin):
    def form_valid(self, form):
        serializer_log_class = self.get_serializer_log_class()
        http_rest = super().form_valid(form)
        update_logging_model(
            self.request.user,
            self.get_model_class_name(),
            self.object.id,
            self.old_obj_serialized_data,
            serializer_log_class(instance=self.object).data
        )
        return http_rest


class DestroyLoggingMixin(BaseLoggingMixin):
    def get_object(self):
        obj = super().get_object()
        self.obj_id = obj.id
        return obj

    def form_valid(self, form):
        http_rest = super().form_valid(form)
        destroy_logging_model(
            self.request.user,
            self.get_model_class_name(),
            self.obj_id,
            self.old_obj_serialized_data,
        )
        return http_rest
