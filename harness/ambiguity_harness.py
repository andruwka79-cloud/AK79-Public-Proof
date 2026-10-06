from dataclasses import dataclass

class AckLost(RuntimeError):
    pass

@dataclass
class Event:
    task_id: str
    attempt_id: str
    provider: str
    kind: str

class RemoteWorld:
    def __init__(self):
        self.value = None
        self.write_count = 0
        self.events = []

    def write_then_lose_ack(self, task_id, attempt_id, provider, value):
        if self.value is not None:
            raise RuntimeError("duplicate_write_attempt")
        self.value = value
        self.write_count += 1
        self.events.append(Event(task_id, attempt_id, provider, "WRITE_COMMITTED"))
        raise AckLost("effect_committed_ack_lost")

    def read(self, task_id, attempt_id, provider):
        self.events.append(Event(task_id, attempt_id, provider, "REMOTE_READBACK"))
        return self.value

def reconcile_after_unknown(world, task_id, first_attempt, second_attempt, value):
    try:
        world.write_then_lose_ack(task_id, first_attempt, "provider-a", value)
    except AckLost:
        observed = world.read(task_id, second_attempt, "provider-b")
        if observed == value:
            return {
                "terminal_state": "COMPLETE",
                "task_id": task_id,
                "write_count": world.write_count,
                "remote_value": observed,
                "blind_replay": False,
            }
        raise RuntimeError("unresolved_unknown")
