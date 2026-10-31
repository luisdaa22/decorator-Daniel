from .message_decorator import MessageDecorator
class UrgentDecorator(MessageDecorator):
    def render(self): return f"[URGENT] {self.wrapped.render()}"
