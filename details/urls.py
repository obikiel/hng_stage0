from django.urls import path
from .views import PublicInfoView

urlpatterns = [
    path('info/', PublicInfoView.as_view(), name='public-info'),
]