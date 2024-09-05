
from .models import Category, Post, Reyting, Banner, Settings,Comment
from .serializers import CategorySerializer, PostSerializer, ReytingSerializer,BannerSerializer,SettingsSerializer,CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# category

# class CategoryList(APIView):
#     def get(self,request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
    
# class CategoryDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         category = get_object_or_404(Category, id=kwargs["id"])
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    

# # POST

# class PostList(APIView):
#     def get(self,request,):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
# class PostDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         post = get_object_or_404(Post, id=kwargs["id"])
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
# # Reyting

# class ReytingList(APIView):
#     def get(self,request,):
#         reytings = Reyting.objects.all()
#         serializer = ReytingSerializer(reytings, many=True)
#         return Response(serializer.data)
    

# class ReytingDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         reyting = get_object_or_404(Reyting, id=kwargs["id"])
#         serializer = ReytingSerializer(reyting)
#         return Response(serializer.data)
    

# # Banner

# class BannerList(APIView):
#     def get(self,request,):
#         banners = Banner.objects.all()
#         serializer = BannerSerializer(banners, many=True)
#         return Response(serializer.data)
    

# class BannerDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         banner = get_object_or_404(Banner, id=kwargs["id"])
#         serializer = BannerSerializer(banner)
#         return Response(serializer.data)

# # Setting

# class SettingsList(APIView):
#     def get(self,request,):
#         settings = Settings.objects.all()
#         serializer = SettingsSerializer(settings, many=True)
#         return Response(serializer.data)
    

# class SettingsDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         settings = get_object_or_404(Settings, id=kwargs["id"])
#         serializer = SettingsSerializer(settings)
#         return Response(serializer.data)
    
# # Comment

# class CommentList(APIView):
#     def get(self,request,):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# class CommentDetail(APIView):
#     def get(self,request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs["id"])
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
    


    
class categorylist(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Categorydetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    











# Create your views here.

# def category(request):
#     categor = Category.objects.all()
#     serializer = CategorySerializer(categor,many=True)
#     # x = []
#     # for i in categories:
#     #     x.append({"id": i.id, "name": i.name})
#     return JsonResponse(serializer.data, safe=False)
# def post(request):
#     posts = Post.objects.all()
#     s = PostSerializer(posts, many=True)
# #     x = []
# #     for i in posts:
# #         x.append({"title": i.title, "descripsen": i.descripsen, "image": i.image, "created_at": i.created_at, "updated_at": i.updated_at,"author": i.author,"valus": i.valus})
#     return JsonResponse(s.data, safe=False)