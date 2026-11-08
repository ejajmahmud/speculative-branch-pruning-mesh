"""Unit tests for speculative-branch-pruning-mesh."""
import unittest
from speculative_branch_pruning_mesh.mesh import SpeculativeBranchPruningMesh


class TestSpeculativeBranchPruningMesh(unittest.TestCase):
    def test_prune_below_threshold(self):
        m = SpeculativeBranchPruningMesh(pruning_threshold=0.5)
        m.add_branch("b1", "h1", 0.8)
        m.add_branch("b2", "h2", 0.3)
        pruned = m.prune()
        self.assertIn("b2", pruned)
        self.assertEqual(len(m.get_active_branches()), 1)

    def test_prune_excess_capacity(self):
        m = SpeculativeBranchPruningMesh(pruning_threshold=0.1, max_active_branches=1)
        m.add_branch("b1", "h1", 0.7)
        m.add_branch("b2", "h2", 0.9)
        pruned = m.prune()
        self.assertIn("b1", pruned)
        active = m.get_active_branches()
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].branch_id, "b2")
