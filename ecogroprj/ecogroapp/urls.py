from django.urls import path
from ecogroapp import views

urlpatterns = [
    
    path('list/',views.ProductListView.as_view(), name='list'),
    path('create/',views.ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>',views.ProductDetailView.as_view(), name='detail'),
    path('edit/<int:pk>',views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>',views.ProductDeleteView.as_view(), name='delete'),
    path('category/<str:categoryname>/', views.show,name='products_by_category'),
    path('category/', views.show,name='allcategory'),
    path('search/', views.search,name='search'),
]