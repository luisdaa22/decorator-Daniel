from datetime import datetime
from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator
def test_urgent_and_timestamp_decorators_stack():
    message=UrgentDecorator(TimestampDecorator(PlainMessage("Deploy complete"), lambda: datetime(2026, 1, 2, 9, 30)))
    assert message.render()=="[URGENT] [2026-01-02 09:30] Deploy complete"
