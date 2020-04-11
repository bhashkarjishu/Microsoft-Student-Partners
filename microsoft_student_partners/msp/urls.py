from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.msp.views import MspView

app_name = "msp"
urlpatterns = [
    path("", view=MspView.as_view()),
    path("services/",TemplateView.as_view(template_name="services.html"), name="services")
]
