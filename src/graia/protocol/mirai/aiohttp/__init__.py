from graia.protocol.core import GraiaProtocol, exceptions as ProtocolExceptions
from .session import MiraiSession
from aiohttp import ClientSession

class MiraiAiohttpProtocol(GraiaProtocol):
    session: MiraiSession
    http_session: ClientSession

    def __init__(self, session: MiraiSession):
        self.session = session
        self.http_session = ClientSession()