
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import (article_list,article_detail,
ArticleAPIView,ArticleDetails,GenericAPIView,
ArticleViewSet,GenArticleViewSet)

router=DefaultRouter()
#router.register('article',ArticleViewSet,basename='article')
router.register('article',GenArticleViewSet,basename='article')
urlpatterns = [
    path('viewsets/',include(router.urls)),
    path('viewsets/<int:pk>/',include(router.urls)),
    #path(r'list/',article_list),
    path(r'list/',ArticleAPIView.as_view()),
    #path(r'detail/<int:pk>/',article_detail),
    path(r'detail/<int:pk>/',ArticleDetails.as_view()),
    path(r'generic/list/<int:id>/',GenericAPIView.as_view()),

]
