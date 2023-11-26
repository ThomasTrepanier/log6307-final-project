@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    mark = item.get_closest_marker(name='myskip')
    if mark:
        condition = next(iter(mark.args), True)
        reason = mark.kwargs.get('reason', 'custom skipping mechanism')
        item.add_marker(pytest.mark.skipif(not os.getenv('PYTEST_RUN_FORCE_SKIPS', False) and condition, reason=reason), append=False)
