from django.urls import path
from .views import ConversionHistoryView, ConversionHistoryDeleteUpdateView, ConversionListCreateView,AdminConversionHistoryView,home,convert

urlpatterns = [
    path('',home),
    path('convert/',convert,name="convert"),
    path("history/", ConversionHistoryView.as_view(), name="conversion-history"),
    path("history/<int:pk>/", ConversionHistoryDeleteUpdateView.as_view(), name="conversion-detail"),
    path("history/all/", AdminConversionHistoryView.as_view(), name="all-history"),
    
]


