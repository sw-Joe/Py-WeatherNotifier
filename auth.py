import logging as log
import os
# import webbrowser

import requests

from err import InvalidTokenRequest, RefreshTokenStillValid
from io_func import Write, read_json
from value import (KAKAO_API_KEY,INQUIRY_ACCESS_TOKEN_URI, OAUTH_URI,
    PATH_TOKEN, REDIRECT_URI, auth_code_URI)



log.basicConfig(
    level=log.INFO,
    format='%(asctime)s|%(levelname)s| %(message)s'
)


def request_auth_code() -> None:
    """
    인가 코드(authorization_code) 발급, 저장 함수
    @params, @return:
        None
    """
    log.debug("Authoriation을 위한 브라우저")
    log.info("로그인 후, URL을 터미널에 복사&붙여넣기 하여 주세요")
    log.info(f"다음을 요청합니다: {auth_code_URI[:30]} ...")
    log.debug(auth_code_URI)    # 디버그용
    os.system(f'cmd.exe /C start {auth_code_URI}')
    # webbrowser.open(auth_code_URI, new=1, autoraise=True)

    # 올바른 값이 input으로 입력되길 무한히 기다림
    while True:
        access_token_input = input("URL: ")
        input_content = access_token_input.replace(f"URL: {REDIRECT_URI}", "")
        # input_content = input_content[31:]
        # input_content = input_content[36:]

        if input_content == "" or None:
            log.warning("빈 입력값입니다. 다시 시도해주세요")
        elif input_content != "" or None:
            log.info(f"입력값: input_content[:10] ... {input_content[-10:]}")
            break

    Path: Write = Write(PATH_TOKEN)
    Path.write_jsons("authorization_code", access_token_input)
    read_json(PATH_TOKEN, "authorization_code")


def issue_token(authorization_code: str) -> None:
    """
    - 토큰 최초 발급 시
    - refresh token 만료 시 (토큰 발급 시에는 항상 access, refresh token이 함께 발급)
    @params
        authorization_code  : str - 인가코드값 
    @return:
        None
    """

    access_token: str = "N/A"  # not applicable, 해당 없음, 유효하지 않음, 공백
    refresh_token: str = "N/A"

    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_API_KEY,
        "redirect_URI": REDIRECT_URI,
        "code": authorization_code,
    }

    content = requests.post(OAUTH_URI, data=data).json()

    try:  # 시도할 작업
        access_token = content["access_token"]
        refresh_token = content["refresh_token"]
    except KeyError:  # 에러 발생시
        # 발급 과정에서 에러 발생
        raise InvalidTokenRequest
        # refresh token값이 갱신되지 않았다면 유효기간이 1개월 미만으로 남은 경우일 가능성도
    else:  # 에러 발생하지 않을 시
        Path: Write = Write(PATH_TOKEN)
        Path.write_jsons("refresh_token", refresh_token)
        Path.write_jsons("access_token", access_token)
    finally:  # 에러 발생 여부와 관계없이 실행
        content_keys: list = content.keys()

        for key in content_keys:
            print("{0:<24} | {1}".format(key, content[key]))
        # token_type, access_token, expires_in, refresh_token, refresh_token_expires_in을 반환


def access_token_info(access_token: str) -> None:
    """
    엑세스 토큰의 유효기간 등 토큰 관련 정보를 조회
    @params:
        access_token    : str - 액세스 토큰값
    @return:
        None
    """

    headers: dict = {
        'Authorization': "Bearer " + access_token
    }

    token_info = requests.get(INQUIRY_ACCESS_TOKEN_URI, headers=headers).json()
    token_info_keys: list = token_info.keys()
    for key in token_info_keys:
        print("{0:<24} | {1}".format(key, token_info[key]))


def renew_both_token(refresh_token: str) -> None:
    """
    기존의 refresh 토큰을 이용하여 Access token, refresh token 모두 재발행
    @params:
        refresh_token   : str - 리프레시 토큰값
    @return:
        None
    """

    data: dict = {
        "grant_type": "refresh_token",
        "client_id": KAKAO_API_KEY,
        "refresh_token": refresh_token,
    }
    content = requests.post(OAUTH_URI, data=data).json()


    try:
        refresh_token = content["refresh_token"]
    except KeyError:
        # 토큰 발급 도중 에러 발생
        # issue_token()으로 재발급 요청 필요
        raise RefreshTokenStillValid
    else:
        Path: Write = Write(PATH_TOKEN)
        Path.write_jsons("refresh_token", refresh_token)
