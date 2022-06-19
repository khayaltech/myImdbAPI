from myimdb_watchlist.api.serializers import (WatchListSerializer,
                                              StreamPlatformSerializer,
                                              ReviewSerializer)
from myimdb_watchlist.models import WatchList,StreamPlatform,Review
from rest_framework import generics
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser
from myimdb_watchlist.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
# from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from myimdb_watchlist.api.throttling import ReviewCreateThrottle,ReviewListThrottle
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from myimdb_watchlist.api.paginations import WatchListPagination



class WatchListAll(generics.ListCreateAPIView):
  # throttle_classes=[UserRateThrottle,AnonRateThrottle]
  queryset=WatchList.objects.all()
  serializer_class=WatchListSerializer
  pagination_class=WatchListPagination

  #For Filtering(Exact match)
  # filter_backends = [DjangoFilterBackend] 
  # filterset_fields=['title','platform__name']


  #For Searching
  # filter_backends = [filters.SearchFilter]
  # search_fields=['title','platform__name']

  #For Ordering
  filter_backends = [filters.OrderingFilter]
  ordering_fields=['title','platform__name']
  ordering=['-avg_rating']


      
class WatchListDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset=WatchList.objects.all()
  serializer_class=WatchListSerializer
  permission_classes=[AdminOrReadOnly]
  throttle_scope='movie-detail'
  throttle_classes=[ScopedRateThrottle]



class ReviewList(generics.ListAPIView):
  serializer_class=ReviewSerializer  
  permission_classes=[IsAuthenticated]
  throttle_classes=[ReviewListThrottle]
  
  def get_queryset(self):
    pk=self.kwargs['pk']
    print(pk)
    return Review.objects.filter(watchlist=pk)
  
class ReviewByUser(generics.ListAPIView):
  serializer_class=ReviewSerializer
  # permission_classes=[IsAuthenticated]


  # path('reviews/',ReviewByUser.as_view(),name="review-user"),  --- For this path
  # def get_queryset(self):
  #   username=self.kwargs['username']
  #   return Review.objects.filter(reviewer__username=username)

  # path('reviews/',ReviewByUser.as_view(),name="review-user"), --- For this path
  def get_queryset(self):
    username=self.request.query_params.get('username',None)
    if username is not None:
      query=Review.objects.filter(reviewer__username=username)
      
    return query

  
class ReviewCreate(generics.CreateAPIView):
  serializer_class=ReviewSerializer
  # throttle_classes=[ReviewCreateThrottle]

  def get_queryset(self):
    return Review.objects.all()
  
  def perform_create(self,serializer):
    pk=self.kwargs['pk']
    movie=WatchList.objects.get(pk=pk)
    reviewer=self.request.user
    review=Review.objects.filter(watchlist=movie,reviewer=reviewer)
    if review.exists():
      raise  ValidationError('You have already reviewed!')
    if movie.number_of_rating==0:
       movie.avg_rating=serializer.validated_data['rating']
    else:
      movie.avg_rating=(movie.avg_rating+serializer.validated_data['rating'])/2
      
    movie.number_of_rating+=1
    movie.save()
      
    serializer.save(watchlist=movie,reviewer=reviewer)

   
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer  
  permission_classes=[ReviewUserOrReadOnly]


class StreamPlatformList(generics.ListCreateAPIView):
  queryset=StreamPlatform.objects.all()
  serializer_class=StreamPlatformSerializer
  throttle_scope='movie-detail'
  throttle_classes=[ScopedRateThrottle]


class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes=[AdminOrReadOnly]


  
  
