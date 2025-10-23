

import os
import requests
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

@api_view(['GET'])
def google_login(request):
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={os.getenv('GOOGLE_CLIENT_ID')}&"
        f"redirect_uri={os.getenv('GOOGLE_REDIRECT_URI')}&"
        f"scope=openid%20email%20profile&"
        f"response_type=code&"
        f"access_type=offline&prompt=consent"
    )
    return HttpResponseRedirect(auth_url)

@api_view(['GET'])
def google_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Authorization code missing'}, status=400)

    try:
        # Exchange code for tokens
        token_response = requests.post('https://oauth2.googleapis.com/token', data={
            'code': code,
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri': os.getenv('GOOGLE_REDIRECT_URI'),
            'grant_type': 'authorization_code'
        }).json()

        if 'error' in token_response:
            return JsonResponse({'error': 'Google token exchange failed'}, status=400)

        access_token = token_response['access_token']
        id_token = token_response['id_token']

        # Get user info from Google API
        user_info = requests.get(
            'https://www.googleapis.com/oauth2/v2/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        ).json()

        if 'error' in user_info:
            return JsonResponse({'error': 'Failed to fetch user info'}, status=400)

        # Generate app's JWT
        app_token = jwt.encode({
            'user_id': user_info['id'],
            'email': user_info['email'],
        }, os.getenv('JWT_SECRET'), algorithm='HS256')

        return JsonResponse({
            'success': True,
            'token': app_token,
            'user': {
                'id': user_info['id'],
                'email': user_info['email'],
                'name': user_info.get('name'),
                'picture': user_info.get('picture')  # <-- এখানে profile image যোগ হলো
            }
        })
    except Exception as e:
        return JsonResponse({'error': f'Google login failed: {str(e)}'}, status=500)

