class APIClient:

    def __init__(self, playwright):

        self.request_context = playwright.request.new_context(
            base_url="https://gorest.co.in/",
            extra_http_headers={
                "Authorization":
                "Bearer e7c10ef3f48257c0c331a36b50462fe391d403c1e1302ad75aada59defaa2c36"
            }
        )
