from django.urls import path
from .views import Home, Opinion, ShowOpinions

urlpatterns = [
    path("", Home.as_view(), name = 'home'),
    path("opinion",Opinion.as_view(), name= 'opinion' ),
    path("opinion/results", ShowOpinions.as_view(), name='finalResult'  )
]
