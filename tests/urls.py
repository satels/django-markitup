from django.urls import include, path

urlpatterns = [
    path('markitup/', include('markitup.urls')),
]
