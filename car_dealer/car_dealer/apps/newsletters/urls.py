from django.urls import path

from .views import NewNewLetterView, SuccessTemplateView

app_name = 'newsletters'

urlpatterns = [
    path(
        'new/',
        NewNewLetterView.as_view(),
    ),
    path(
        'success/',
        SuccessTemplateView.as_view(),
    ),
]
