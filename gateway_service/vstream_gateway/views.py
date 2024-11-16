import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Base URL for the user service (adjust as needed)
USER_SERVICE_BASE_URL = "http://127.0.0.1:8000/vstream_user_service"

@csrf_exempt
def gateway_login(request):
    if request.method == 'POST':
        try:
            # Forward request to the user service login endpoint
            response = requests.post(
                f"{USER_SERVICE_BASE_URL}/login/",
                data=request.body,
                headers={"Content-Type": "application/json"},
            )
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def gateway_register(request):
    if request.method == 'POST':
        try:
            # Forward request to the user service register endpoint
            response = requests.post(
                f"{USER_SERVICE_BASE_URL}/register/",
                data=request.body,
                headers={"Content-Type": "application/json"},
            )
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def gateway_authorize_user(request):
    if request.method == 'POST':
        try:
            # Forward request to the user service authorize_user endpoint
            response = requests.post(
                f"{USER_SERVICE_BASE_URL}/authorize_user/",
                data=request.body,
                headers=request.headers,  # Forward headers (including Authorization)
            )
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
