class ValueNotFound(Exception):
    """
    값이 존재하지 않거나 또는 찾을 수 없음.
    """
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return f"찾으려는 값 '{self.value}'(을)를 찾을 수 없습니다"


class InvalidTokenRequest(Exception):
    """
    에러: 잘못된 요청입니다. 토큰이 발급되지 않습니다
    """
    def __str__(self):
        return "Invalid token request. token has not been issued."


class RefreshTokenExpired(Exception):
    """
    에러: 리프레시 토큰이 만료되었습니다
    """
    def __str__(self):
        return "Refresh Token expired. Required to issue new Token."


class RefreshTokenStillValid(Exception):
    """
    에러: 리프레시 토큰이 아직 유효하므로 현재 토큰값을 유지합니다
    """
    def __str__(self):
        return """Refresh Token is still valid. 
              System will maintain previous Refresh Token."""
