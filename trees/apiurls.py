from django.urls import path

app_name = "api"

from .apiviews import SpecieAPIView, SquareAPIView, FamilyAPIView, TreeAPIView, SpeciesAPIView, SquaresAPIView, FamilysAPIView, TreesAPIView

urlpatterns = [
    path('pracas/', SquaresAPIView.as_view(), name='pracas'),
    path('familias/', FamilysAPIView.as_view(), name='familias'),
    path('especies/', SpeciesAPIView.as_view(), name='especies'),
    path('arvores/', TreesAPIView.as_view(), name='arvores'),
    path('pracas/<int:pk>/', SquareAPIView.as_view(), name='pracas'),
    path('pracas/<int:square_pk>/arvores/', TreesAPIView.as_view(), name='pracas_arvores'),
    path('pracas/<int:square_pk>/arvores/<int:tree_pk>/', TreeAPIView.as_view(), name='pracas_arvores'),
    path('familias/<int:pk>/', FamilyAPIView.as_view(), name='familias'),
    path('especies/<int:pk>/', SpecieAPIView.as_view(), name='especies'),
    path('arvores/<int:tree_pk>/', TreeAPIView.as_view(), name='arvores')
]

