from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size=5
    # page_query_param='imdbpage'
    page_size_query_param='size'
    max_page_size=50
    # last_page_strings="end"



#Just for trying
class WatchListPaginationlLo(LimitOffsetPagination): 
    default_limit=5
    limit_query_param="end"
    offset_query_param="start"
    max_limit=50


class WatchListPaginationCursor(CursorPagination):
    page_size=1
    # cursor_query_param="page"
