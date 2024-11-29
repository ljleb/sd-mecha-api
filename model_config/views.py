from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.response import Response

from core.views import ApiView
from model_config.models import ModelConfig


class ModelConfigView(ApiView):
    def get(self, request, *, id):
        try:
            config = ModelConfig.objects.get(id=id).value
        except ObjectDoesNotExist as e:
            return Response('Model config not found', 404)
        except ValidationError as e:
            return Response(e.message % e.params, 422)
        except Exception as e:
            return Response('Bad request', 400)

        return Response({'yaml': config.value}, 200)
