from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SearchListAPIView,PostViewSet, PostListAPIView,CategoryListAPIView,FilterListAPIView,ContributorListView,SingleListAPIView

from django.conf.urls.static import static
from django.conf import settings

router = SimpleRouter()
router.register('', PostViewSet, basename='post'),
urlpatterns = router.urls

urlpatterns += [
    # path('v1/list-filter/', PostListAPIView.as_view()),
    # path('category', CategoryListAPIView.as_view()),
    # path('',PostListAPIView.as_view()),
    path('v1/search/',SearchListAPIView.as_view()),
    path('v1/filter/', FilterListAPIView.as_view()),
    path('category', CategoryListAPIView.as_view()),
    path('contributor/', ContributorListView.as_view()),
    # path('<int:pk>/',SingleListAPIView.as_view()),
    # path('category/<int:pk>', FilterListView.as_view(), name='post-category')
    # path('video', VideoListAPIView.as_view())
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
                 # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                 # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)