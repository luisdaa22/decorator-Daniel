from datetime import datetime
from typing import Callable
from .message import Message
from .message_decorator import MessageDecorator
class TimestampDecorator(MessageDecorator):
    # The clock is injected so tests can pin the time; datetime.now is the production default.
    def __init__(self, wrapped: Message, clock: Callable[[], datetime]=datetime.now):
        super().__init__(wrapped)
        self.clock=clock
    def render(self): return f"[{self.clock():%Y-%m-%d %H:%M}] {self.wrapped.render()}"
