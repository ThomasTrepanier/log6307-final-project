import pytest
from _pytest.mark.evaluate import MarkEvaluator

def pytest_addoption(parser):
    parser.addoption(
        "--no-skips", action="store_true", default=False, help="disable custom_skip marks"
    )

@hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    if item.config.getoption('--no-skips'):
        return

    # Check if skip or skipif are specified as pytest marks
    item._skipped_by_mark = False
    eval_skipif = MarkEvaluator(item, "custom_skipif")
    if eval_skipif.istrue():
        item._skipped_by_mark = True
        pytest.skip(eval_skipif.getexplanation())

    for skip_info in item.iter_markers(name="custom_skip"):
        item._skipped_by_mark = True
        if "reason" in skip_info.kwargs:
            pytest.skip(skip_info.kwargs["reason"])
        elif skip_info.args:
            pytest.skip(skip_info.args[0])
        else:
            pytest.skip("unconditional skip")

    item._evalxfail = MarkEvaluator(item, "xfail")
    check_xfail_no_run(item)
