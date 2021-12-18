from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

 

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_limit_number(self):
        limit_number = self.request.query_params.get(self.page_size_query_param, 1)
        return limit_number 

    def get_paginated_response(self, data):
        return Response({
            'total_page': self.page.paginator.num_pages,
            'page': self.page.number,
            'limit': self.get_limit_number(),
            'count': self.page.paginator.count,
            'data': data,
            'link' : {
                'prev': self.get_previous_link(),
                'next': self.get_next_link(),
            }
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'total_page': {
                    'type': 'integer',
                    'example': 123,
                },
                'page': {
                    'type': 'integer',
                    'example': 123,
                },
                'limit': {
                    'type': 'integer',
                    'example': 123,
                },
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'next': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=4'.format(
                        page_query_param=self.page_query_param)
                },
                'prev': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=2'.format(
                        page_query_param=self.page_query_param)
                },
                'data': schema,
            },
        }