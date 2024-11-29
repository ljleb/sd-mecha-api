from django.urls import path

from model_config.views import ModelConfigView


urlpatterns = [
    path('model-configs/<str:id>', ModelConfigView.as_view()),
]
