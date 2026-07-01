from playwright.sync_api import Page


def test_api_network_testing(page:Page):

    
        def handle_api_route(route):
            # We intercept the real API call and return our own custom JSON response
            fake_data = {"status": "success", "username": "Super_Coder_99", "balance": "$9,999,999"}
            route.fulfill(
                status=200,
                content_type="application/json",
                json=fake_data
            )
    
        # Whenever the browser hits this specific API endpoint, intercept it
        page.route("**/public/v2/users", handle_api_route)
    
        # Go to the website that calls this API
        page.goto("https://gorest.co.in/public/v2/users")
        
        # The page will now display "Super_Coder_99" and the fake balance!
        page.wait_for_timeout(5000)