from django.shortcuts import render

# Create your views here.
import redis
from rest_framework.views import APIView
from rest_framework.response import Response

redis_host = "localhost"
redis_port = 6379
# Connect to our Redis instance
r = redis.Redis(host=redis_host, port=redis_port)


class FetchData(APIView):
    def get(self, request):
        search_type = self.request.query_params.get("type", "")
        value = self.request.query_params.get("value", "")
        value = value.upper()
        if search_type == "contains" and value != "":
            all_keys = r.keys("*" + value + "*")
        elif value != "":
            all_keys = r.keys(value + "*")
        else:
            all_keys = r.keys("A*")
        result = []
        for key in all_keys:
            result.append(
                {
                    result_key.decode("utf-8"): value.decode("utf-8")
                    for result_key, value in r.hgetall(key.decode("utf-8")).items()
                }
            )
        return Response(result)
