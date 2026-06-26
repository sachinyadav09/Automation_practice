import os
import pytest


@pytest.fixture
def page(browser, request):

    os.makedirs("reports/videos", exist_ok=True)
    os.makedirs("reports/traces", exist_ok=True)
    os.makedirs("reports/screen_shots", exist_ok=True)

    context = browser.new_context(
        record_video_dir="reports/videos/"
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    context.tracing.stop(
        path=f"reports/traces/{request.node.name}.zip"
    )

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            page.screenshot(
                path=f"reports/screen_shots/{item.name}.png",
                full_page=True
            )