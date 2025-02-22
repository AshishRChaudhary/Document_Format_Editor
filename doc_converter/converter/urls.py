from django.urls import path
from .views import ConversionHistoryView, ConversionHistoryDeleteUpdateView, ConversionListCreateView

urlpatterns = [
    path("history/", ConversionHistoryView.as_view(), name="conversion-history"),
    path("history/<int:pk>/", ConversionHistoryDeleteUpdateView.as_view(), name="conversion-detail"),
    path("convert/", ConversionListCreateView.as_view(), name="convert"),
    
]


