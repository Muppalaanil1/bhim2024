from seleniumbase import BaseCase

class SafariQuoteAutomation(BaseCase):
    def test_request_safari_quote(self):
        # Step 1: Open the website
        self.open("https://zen-price-my-tours.lovable.app/") 

        # Step 2: Click Login and perform login
        self.click("button:contains('Login')")
        self.type('input[type="email"]', "tourist@demo.app")
        self.type('input[type="password"]', "tourist@123!")
        self.click("button:contains('Sign In')")
    

        # Wait for login to finish
        #self.wait_for_element('button:contains("Request Custom Tour")', timeout=10)

        # Step 3: Click Request Custom Tour
        self.click('button:contains("Request Custom Tour")')

        # Step 4: Fill in Tour Request Form 
        #self.select_option_by_text("select['auto-test-id'='activity-type-select']", "Great Migration Safari")
        #self.select_option_by_value("div.space-y-1:nth-of-type(1) select", "Big Five Safari")
        
        #self.type("#guests", "2")
        #self.type("#number_of_days", "1")
        
        #self.click("button[auto-test-id='country-select']")
        #self.click("text='KE Kenya'")

        #self.select_option_by_value("div.space-y-1:nth-of-type(2) select", "🇰🇪 Kenya")

        #self.wait(5)
        #self.select_option_by_value("div.space-y-1:nth-of-type(4) select", "Kenya")
        
        #self.click("button[auto-test-id='origin-select']")
        #self.select_option_by_value("div.space-y-1:nth-of-type(5) select", "Moshi")
 
        #self.click("button[auto-test-id='start-time-select']")
        #self.select_option_by_value('div.space-y-1:nth-of-type(6) select', "Morning")
        #self.wait(5)


        ## Day by Day configuration
        #Transportation
        self.click('button[role="combobox"]:contains("Safari")')
        self.wait_for_element('div[role="option"]:contains("Safari Minibus")')
        self.click('div[role="option"]:contains("Safari Minibus")')

         # Accommodation
        self.click('button[role="combobox"]:contains("Lodge")')
        self.wait_for_element('div[role="option"]:contains("Luxury Lodge")')
        self.click('div[role="option"]:contains("Luxury Lodge")')

          # Meal Plan
        self.click('button[role="combobox"]:contains("Board")')
        self.wait_for_element('div[role="option"]:contains("Breakfast Only")')
        self.click('div[role="option"]:contains("Breakfast Only")')
        
        # TRAVELERS THIS DAY
        self.wait_for_element('input[type="number"]')
        self.clear('input[type="number"]')
        self.type('input[type="number"]', '3')

        # SPECIAL REQUEST FOR DAY 1
        self.wait_for_element('textarea[placeholder*="special activities"]')
        self.type('textarea[placeholder*="special activities"]', "Annual function for Day 1")

        # Step 5: Click Request Custom Safari Quote
        self.click('button:contains("Request Custom Safari Quote")')

        # Step 6: Verify in "Your Requests"
        self.click('[auto-test-id="view-requests-button"]')