"""Core Speculative Branch Pruning Mesh implementation."""
from typing import List, Dict, Optional, Any


class ReasoningBranch:
    def __init__(self, branch_id: str, hypothesis: str, score: float = 0.5):
        self.branch_id = branch_id
        self.hypothesis = hypothesis
        self.score = score
        self.pruned = False


class SpeculativeBranchPruningMesh:
    def __init__(self, pruning_threshold: float = 0.6, max_active_branches: int = 3):
        self.pruning_threshold = pruning_threshold
        self.max_active_branches = max_active_branches
        self.branches: Dict[str, ReasoningBranch] = {}

    def add_branch(self, branch_id: str, hypothesis: str, score: float = 0.5) -> ReasoningBranch:
        b = ReasoningBranch(branch_id, hypothesis, score)
        self.branches[branch_id] = b
        return b

    def update_score(self, branch_id: str, new_score: float):
        if branch_id in self.branches:
            self.branches[branch_id].score = new_score

    def prune(self) -> List[str]:
        pruned_ids = []
        # Prune branches below absolute threshold
        for b in self.branches.values():
            if not b.pruned and b.score < self.pruning_threshold:
                b.pruned = True
                pruned_ids.append(b.branch_id)

        # Enforce max active branches (keep highest scoring)
        active = [b for b in self.branches.values() if not b.pruned]
        if len(active) > self.max_active_branches:
            active.sort(key=lambda x: x.score, reverse=True)
            for b in active[self.max_active_branches:]:
                b.pruned = True
                pruned_ids.append(b.branch_id)

        return pruned_ids

    def get_active_branches(self) -> List[ReasoningBranch]:
        return [b for b in self.branches.values() if not b.pruned]
