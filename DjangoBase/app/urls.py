from django.urls import path
from django.urls import path
from app.views import ProductList
from app.appviews.search import Search

urlpatterns = [
    path('valerdat/products/', ProductList.as_view(), name='product-list'),
    path('word_finder/<str:input_word>/', Search.word_finder, name='word-finder'),
    path('valerdat/searchcoords/', Search.search_coords, name='search-coords'),
]
