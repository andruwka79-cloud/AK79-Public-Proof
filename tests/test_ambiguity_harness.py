import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from ambiguity_harness import RemoteWorld, reconcile_after_unknown

class AmbiguityHarnessTest(unittest.TestCase):
    def test_lost_ack_provider_switch_has_no_blind_replay(self):
        # Visible vector V13: effect committed, ACK lost, provider switch.
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

    def test_preexisting_effect_blocks_second_write(self):
        # A second write against an already-committed effect must be refused, never replayed.
        world = RemoteWorld()
        world.value = "already-there"
        with self.assertRaisesRegex(RuntimeError, "duplicate_write_attempt"):
            reconcile_after_unknown(world, "PUBLIC-DEMO-002", "A1", "A2", "expected-effect")
        self.assertEqual(world.write_count, 0)

    def test_readback_mismatch_is_unresolved_not_complete(self):
        # The readback branch that refuses to report COMPLETE when remote state disagrees.
        class DivergentWorld(RemoteWorld):
            def read(self, task_id, attempt_id, provider):
                super().read(task_id, attempt_id, provider)
                return "something-else"

        with self.assertRaisesRegex(RuntimeError, "unresolved_unknown"):
            reconcile_after_unknown(DivergentWorld(), "PUBLIC-DEMO-003", "A1", "A2", "expected-effect")

if __name__ == "__main__":
    unittest.main()
