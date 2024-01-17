from django.urls import path
from . import views

app_name = 'superuser'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    
    # Images
    path('images/', views.viewImages, name="viewImages"),
    path('add-image/', views.addImage, name="addImage"),
    path('edit-image/<int:id>/', views.editImage, name='editImage'),
    path('delete-image/<int:id>', views.deleteImage, name='deleteImage'),

    # Blogs
    path('blogs/', views.viewBlogs, name="viewBlogs"),
    path('add-blog/', views.addBlog, name="addBlog"),
    path('edit-blog/<int:id>/', views.editBlog, name='editBlog'),
    path('view-blog/<int:id>/', views.viewBlog, name='viewBlog'),
    path('delete-blog/<int:id>', views.deleteBlog, name='deleteBlog'),

    # Videos
    path('videos/', views.viewVideos, name="viewVideos"),
    path('add-video/', views.addVideo, name="addVideo"),
    path('edit-video/<int:id>/', views.editVideo, name='editVideo'),
    path('delete-video/<int:id>', views.deleteVideo, name='deleteVideo'),


    path('profile/', views.profile, name="profile"),
    
    path('reset-password/', views.resetPassword, name="resetPassword"),

    path('logout/', views.user_logout, name='user_logout'),

]