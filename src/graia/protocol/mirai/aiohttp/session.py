from pydantic.main import BaseModel # pylint: disable=no-name-in-module
from pydantic.networks import HttpUrl # pylint: disable=no-name-in-module 
from urllib import parse

class MiraiSession(BaseModel):
    api_root: HttpUrl
    qq: int
    auth_key: str
    websocket: bool = True

    @classmethod
    def from_url(cls, url: str):
        websocket, auth_key, qq, api_root = True, "", None, ""
        urlinfo = parse.urlparse(url)
        if urlinfo:
            query_info = parse.parse_qs(urlinfo.query)
            if all([
                urlinfo.scheme == "mirai",
                urlinfo.path in ["/", "/ws"],

                "authKey" in query_info and query_info["authKey"],
                "qq" in query_info and query_info["qq"]
            ]):
                if urlinfo.path == "/ws":
                    websocket = True
                else:
                    websocket = False

                api_root = f"http://{urlinfo.netloc}"
                auth_key = query_info["authKey"][0]
                qq =  int(query_info["qq"][0])
        else:
            raise ValueError("invaild url: wrong format")
        return cls(api_root=api_root, qq=qq, auth_key=auth_key, websocket=websocket)