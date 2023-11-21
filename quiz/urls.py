from  django.urls import path
from .views import QuestionsViewSet


urlpatterns = [
    path('test/', QuestionsViewSet.as_view({'get': 'list'})),
]