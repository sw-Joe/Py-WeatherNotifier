import os

from dotenv import load_dotenv



# file PATH
PATH_KEY: str = r"./plaintext/key.json"
PATH_TOKEN: str = r"./plaintext/token.json"



load_dotenv(verbose=True)
KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')

REDIRECT_URI: str = "http://localhost:8000/oauth/callback"    # 테스트용
# REDIRECT_URI: str = "https://example.com/oauth"
"""
Http Response Code 리다이렉트
"""

auth_code_URI: str = f"https://kauth.kakao.com/oauth/authorize?&response_type=code&client_id={KAKAO_API_KEY}&redirect_uri={REDIRECT_URI}"
"""
토큰 발급을 위한 access code 요청
API 요청에 필요한 값들을 JSON파일에서 import --> 환경변수로 대체
"""


OAUTH_URI: str = "https://kauth.kakao.com/oauth/token"
"""
토큰 요청/갱신
요청 파라미터에 따라 다른 동작
"""


SEND_MSG_URI: str = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
"""
카카오톡 메세지 전송
"""


# Access token, Refresh token 두 가지 토큰이 존재
# Refresh token은 Access token과 비교해서 상대적으로 긴 유효기간을 가지고 있음.
INQUIRY_ACCESS_TOKEN_URI: str = "https://kapi.kakao.com/v1/user/access_token_info"
"""
access token 정보 조회
"""