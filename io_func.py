import json


def read_json(path: str, keyword: str) -> str:
    """
    JSON 파일 읽기
    @params:
        path    : str - json 파일의 경로
        keyword : str - json 파일에서 검색할 value의 key값에 해당하는 문자열
    @return
        :str - params keyword(json key)값에 맞는 값
    """

    with open(path, "r") as file:
        json_parse = json.load(file)
        return json_parse[keyword]


def write_json(path: str, keyword: str, value: str) -> None:
    """
    JSON 파일 쓰기
    @params:
        path    : str - json 파일 경로
        keyword : str - 파일에서 찾을 value의 key값에 해당하는 문자열
        value   : str - 수정할 내용의 문자열
    @return:
        None
    """

    with open(path, "r") as file:
        json_parse = json.load(file)
        # 데이터 수정
        json_parse[keyword] = value

    # 기존 파일 덮어쓰기
    with open(path, "w", encoding="utf-8") as file:
        json.dump(json_parse, file, indent="\t")


class Write:
    def __init__(self, path):
        self.path = path

    def write_jsons(self, keyword: str, value: str) -> None:
        """
        JSON 파일 쓰기
        @params:
            keyword : str - 파일에서 찾을 value의 key값에 해당하는 문자열
            value   : str - 수정할 내용의 문자열
        @return:
            None
        """

        with open(self.path, "r") as file:
            json_parse = json.load(file)
            # 데이터 수정
            json_parse[keyword] = value

        # 기존 파일 덮어쓰기
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(json_parse, file, indent="\t")
