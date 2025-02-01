from django.urls import path
from .views import PublicInfoView

urlpatterns = [
    path('', PublicInfoView.as_view(), name='public-info'),
]
