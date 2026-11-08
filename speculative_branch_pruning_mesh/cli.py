"""CLI for speculative-branch-pruning-mesh."""
import sys
import argparse
from .mesh import SpeculativeBranchPruningMesh


def main():
    parser = argparse.ArgumentParser(description="Speculative Branch Pruning Mesh CLI")
    parser.add_argument("--demo", action="store_true", help="Run branch pruning demo")
    args = parser.parse_args()

    if args.demo:
        mesh = SpeculativeBranchPruningMesh(pruning_threshold=0.6, max_active_branches=2)
        mesh.add_branch("b1", "Refactor using AST visitors", score=0.92)
        mesh.add_branch("b2", "Regenerate entire file from prompt", score=0.35)
        mesh.add_branch("b3", "Search StackOverflow regexes", score=0.48)
        mesh.add_branch("b4", "Patch byte offsets directly", score=0.75)

        pruned = mesh.prune()
        print(f"[+] Pruned Dead-End Branches: {pruned}")
        print(f"[+] Active Promising Branches: {[b.branch_id + ' (' + str(b.score) + ')' for b in mesh.get_active_branches()]}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
