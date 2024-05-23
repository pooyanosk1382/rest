from django.urls import path, include
#  from .views import movie_list, movie_detail
from .views import ReviewCreate, ReviewDetail, ReviewList, WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAv


urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('list/<int:pk>', WatchDetailAV.as_view(), name="movie-detail"),
    path('stream/', StreamPlatformAV.as_view(), name="stream"),
    path('stream/<int:pk>', StreamPlatformDetailAv.as_view(), name="stream-detail"),
    path('stream/<int:pk>/review', ReviewList.as_view(), name="review-list"),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name="review-create"),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
]
