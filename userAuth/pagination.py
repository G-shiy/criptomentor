from rest_framework.pagination import PageNumberPagination

class FilterResults(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_sizes'
    max_page_size = 150
