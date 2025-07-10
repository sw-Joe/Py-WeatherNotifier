# file PATH
PATH_KEY: str = r"./plaintext/key.json"
PATH_TOKEN: str = r"./plaintext/token.json"


# # API 요청에 필요한 값들을 JSON파일에서 import --> 환경변수로 대체
# API_KEY = read_json(PATH_KEY, "kakao_api_key")


# 인가코드 요청 - 로그인
# Http Response Code 리다이렉트
REDIRECT_URI: str = "https://example.com/oauth"


# 토큰 발급을 위한 인가 코드 받기
# *API_KEY만 다른 모듈에서 Import
auth_code_URI: str = f"https://kauth.kakao.com/oauth/authorize?&response_type=code&client_id={API_KEY}&redirect_uri={REDIRECT_URI}"


# 토큰 요청/갱신 - 요청 파라미터에 따라 다른 동작
OAUTH_URI: str = "https://kauth.kakao.com/oauth/token"


# 메세지 전송 요청
SEND_MSG_URI: str = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


# 액세스 토큰 정보 조회 .
INQUIRY_ACCESS_TOKEN_URI: str = "https://kapi.kakao.com/v1/user/access_token_info"


# Access token, Refresh token 두 가지 토큰이 존재
# Refresh token은 Access token과 비교해서 상대적으로 긴 유효기간을 가지고 있음.
