from graia.protocol.core import GraiaProtocol, exceptions as ProtocolExceptions
from .session import MiraiSession

class MiraiAiohttpProtocol(GraiaProtocol):
    session: MiraiSession

    def __init__(self, session: MiraiSession):
        self.session = session