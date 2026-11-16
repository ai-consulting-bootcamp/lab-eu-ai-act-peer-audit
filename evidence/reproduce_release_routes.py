"""Reproduce two reviewed routing functions without importing the application.

Usage: python evidence/reproduce_release_routes.py PATH_TO_REVIEWED_CHECKOUT
Only the two named function bodies and MAX_RETRIES are executed. No API calls,
application startup, uploads, credentials, or patient records are needed.
"""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1]).resolve()
source = root / "app/agent/nodes.py"
raw = source.read_bytes()
tree = ast.parse(raw.decode("utf-8"))
names = {"route_after_check", "route_after_guard"}
selected = []
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "MAX_RETRIES" for t in node.targets):
        selected.append(node)
    if isinstance(node, ast.FunctionDef) and node.name in names:
        node.returns = None
        for arg in node.args.args:
            arg.annotation = None
        selected.append(node)
assert len(selected) == 3, "Expected constant and two routing functions"
namespace = {}
exec(compile(ast.Module(body=selected, type_ignores=[]), str(source), "exec"), namespace)
cases = [
    ("findings_failure_with_retry", "route_after_check", {"passed": False, "retries": 2}, "write"),
    ("findings_failure_exhausted", "route_after_check", {"passed": False, "retries": 3}, "interpret"),
    ("guard_failure_with_retry", "route_after_guard", {"guard_errors": ["unsupported claim"], "i_retries": 2}, "interpret"),
    ("guard_failure_exhausted", "route_after_guard", {"guard_errors": ["unsupported claim"], "i_retries": 3}, "end"),
    ("guard_success_control", "route_after_guard", {"guard_errors": [], "i_retries": 0}, "end"),
]
results = []
for label, function, state, expected in cases:
    actual = namespace[function](state)
    assert actual == expected, (label, actual, expected)
    results.append({"case": label, "function": function, "input": state, "output": actual})
commit = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
print(json.dumps({
    "review_date": "2026-11-16", "source_commit": commit,
    "source_file": "app/agent/nodes.py", "source_sha256": hashlib.sha256(raw).hexdigest(),
    "method": "Isolated execution of two source-extracted routing functions; not an end-to-end application test",
    "max_retries": namespace["MAX_RETRIES"], "results": results,
    "conclusion": "After retries are exhausted, failed findings continue to interpretation and failed guardrails terminate normally. UI delivery paths require separate source inspection."
}, indent=2))
