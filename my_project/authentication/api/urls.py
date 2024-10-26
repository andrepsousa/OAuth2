from django.urls import path
from authentication.views import ProtectedView

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
]
