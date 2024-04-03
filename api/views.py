from rest_framework.views import APIView
from places.models import Place, PlaceComment
from .serializers import PlaceSerializer, CommentSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PlaceDetailApiView(APIView):
    def get(self, id):
        place = Place.objects.get(id=id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)
    
    
class PlacesApiView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        place = Place.objects.get(id=id)
        serializer = PlaceSerializer(instance=place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        place = Place.objects.get(id=id)
        place.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReviewsApiView(APIView):
    def get(self, request):
        reviews = PlaceComment.objects.all()
        serializer = CommentSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        review = PlaceComment.objects.get(id=id)
        serializer = CommentSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        review = PlaceComment.objects.get(id=id)
        review.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)


class LoginApiView (APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response (serializer.data)
        return Response (serializer.errors)