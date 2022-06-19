from rest_framework import serializers
from myimdb_watchlist.models import Review, WatchList,StreamPlatform

    
    
#Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
  reviewer=serializers.StringRelatedField(read_only=True)
  class Meta:
    model=Review
    exclude=('watchlist',)  
  
#WatchList Serializer
class WatchListSerializer(serializers.ModelSerializer ):
  # reviews=ReviewSerializer(many=True,read_only=True)
  platform=serializers.CharField(source='platform.name')
  class Meta:
    model=WatchList
    fields='__all__'



    
class StreamPlatformSerializer(serializers.ModelSerializer):
  watchlist=WatchListSerializer(read_only=True,many=True)
  

  class Meta:
    model=StreamPlatform
    fields='__all__'
  
  
