from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Video
from .serializers import VideoSerializer

def test(request):
    return render(request,'test.html',{})

class ListVideo(APIView):
    def get(self,request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True)
        return Response(video_json.data)
