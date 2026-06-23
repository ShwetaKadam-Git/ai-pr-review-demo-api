import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.models.review import FileInput
from app.services.mock_ai_services import run_mock_review


def test_detects_bare_except():
    files = [FileInput(filename="x.py", patch="+    except:\n+        pass")]
    findings = run_mock_review(files, "default")
    assert any(f["rule"] == "no-bare-except" for f in findings)


def test_no_findings_on_clean_diff():
    files = [FileInput(filename="x.py", patch="+    return result")]
    findings = run_mock_review(files, "default")
    assert findings == []