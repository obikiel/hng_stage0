from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

class PublicInfoView(APIView):
    def get(self, request):
        data = {
            "email": "ezekielobiomachi1@gmail.com",
            "current_datetime": datetime.now().isoformat() + "Z",
            "github_url": "https://github.com/obikiel/hng_stage0",
        }
        return Response(data)

