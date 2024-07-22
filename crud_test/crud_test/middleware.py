from django.utils.deprecation import MiddlewareMixin
from django.db import connection

class DatabaseRoutingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Example: Get the database name from a request header
        db_name = request.headers.get('X-Database-Name')
        if db_name:
            connection.set_schema(db_name)
