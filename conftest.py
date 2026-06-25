import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

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
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("browser_page")

        if page:

            page.screenshot(
                path=f"reports/screen_shots/{item.name}.png",
                full_page=True
            )