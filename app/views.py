from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import aiohttp
import json
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

@csrf_exempt
async def proxy_request(request):
    if request.method == 'POST':
        body_data = request.body.decode('utf-8')
        data = json.loads(body_data)  # Parse JSON from the body
        url = 'https://back.aisha.group/stt_app/stt/post/'
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Your User Agent Here'  # Example: 'Mozilla/5.0'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status != 200:
                    error_body = await response.text()  # Get the error response as text
                    return JsonResponse({'error': 'API returned an error', 'details': error_body}, status=response.status)

                response_data = await response.json()
                return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)
