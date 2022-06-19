from django.urls import path,include
from myimdb_watchlist.api.views import (WatchListAll,WatchListDetail,
                                        ReviewList,ReviewDetail ,ReviewCreate,ReviewByUser,
                                        StreamPlatformDetail,StreamPlatformList)


urlpatterns = [
  path('list/',WatchListAll.as_view(),name='movie-list'),
  path('<int:pk>/',WatchListDetail.as_view(),name='movie-detail'),
  
  
  path('stream/',StreamPlatformList.as_view(),name='stream-list'),
  path('stream/<int:pk>/',StreamPlatformDetail.as_view(),name='streamplatform-detail'),
  
  path('<int:pk>/review-create/',ReviewCreate.as_view(),name="review-create"),
  path('<int:pk>/reviews/',ReviewList.as_view(),name="review-list"),
  path('reviews/',ReviewByUser.as_view(),name="review-user"),
  path('review/<int:pk>/',ReviewDetail.as_view(),name="review-detail" ),

]
