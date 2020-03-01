from django.urls import path

from markitup.views import apply_filter

urlpatterns = [
    path('preview/', apply_filter, name='markitup_preview'),
]
