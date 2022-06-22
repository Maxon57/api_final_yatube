from api import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r"posts/(?P<post_id>\d+)/comments",
                views.CommentsViewSet,
                basename='comments'
                )
router.register(r'follow', views.FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
]
