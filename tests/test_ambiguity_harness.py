import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from ambiguity_harness import RemoteWorld, reconcile_after_unknown

class AmbiguityHarnessTest(unittest.TestCase):
    def test_lost_ack_provider_switch_has_no_blind_replay(self):
        world = RemoteWorld()
        result = reconcile_after_unknown(
            world,
            task_id="PUBLIC-DEMO-001",
            first_attempt="A1",
            second_attempt="A2",
            value="expected-effect",
        )
        self.assertEqual(result["terminal_state"], "COMPLETE")
        self.assertEqual(result["write_count"], 1)
        self.assertFalse(result["blind_replay"])
        self.assertEqual(result["remote_value"], "expected-effect")
        self.assertEqual(len(world.events), 2)
        self.assertEqual(world.events[0].kind, "WRITE_COMMITTED")
        self.assertEqual(world.events[1].kind, "REMOTE_READBACK")
        self.assertEqual(world.events[0].task_id, world.events[1].task_id)
        self.assertNotEqual(world.events[0].attempt_id, world.events[1].attempt_id)

if __name__ == "__main__":
    unittest.main()
