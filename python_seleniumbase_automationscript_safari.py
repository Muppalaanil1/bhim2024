from seleniumbase import BaseCase

class SafariQuoteAutomation(BaseCase):
    def do_login(self, username, password):
        if not self.is_element_present('[auto-test-id="signin-submit-button"]'):
            self.click("button:contains('Login')")
        self.type('#signin-email', username)
        self.type('input[type="password"]', password)
        self.click("button:contains('Sign In')")
        print(f"sign in for {username} successful")

    ## Click Profile Icon at top-right then Click on logout
    def do_logout(self, user_type):
        if user_type == 'tourist':
            ## Tourist logout
            self.click('button:contains("tourist")')
            self.click('[auto-test-id="logout-menu-item"]')
        elif user_type == 'operator':
            ## Operator logout
            self.click('button[auto-test-id="user-menu-trigger"]')
            self.click('div[auto-test-id="logout-button"]')
        else:
            print(f"Invalid user_type - {user_type}")
            exit(1)
        print(f"{user_type} logout successful")
  

    def test_request_safari_quote(self):
        # Step 1: Open the website
        self.open("https://zen-price-my-tours.lovable.app/") 
        print("opening the website")
        self.save_screenshot("zen-price website")
        self.sleep(2)

        # Step 2: Click Login and perform login
        self.do_login('tourist@demo.app', 'tourist@123!')
        
        # Step 3: Click Request Custom Tour
        self.click('button:contains("Request Custom Tour")')
        print("click request custom tour to make request custom safari quote")
        self.save_screenshot("tourist page")

        # Click the activity type combobox
        self.click('[auto-test-id="activity-type-select"]')

        # safari Details select safari experience
        self.click("//div[@role='option' and contains(., 'Mountain Climbing (Mount Kenya)')]")

        # Number of Travelers 
        self.clear('[auto-test-id="guests-input"]')
        self.type('[auto-test-id="guests-input"]', '2')

        #  Safari Duration 
        self.clear('[auto-test-id="number-of-days-input"]')
        self.type('[auto-test-id="number-of-days-input"]', '1')
    
        # country select
        self.click('[auto-test-id="country-select"]')
        self.click("//div[@role='option' and contains(., 'Tanzania')]")
        self.assert_text('Tanzania', '[auto-test-id="country-select"]')

        # Select preferred start time: Afternoon
        self.click('[auto-test-id="start-time-select"]')
        self.click("//div[@role='option' and contains(., 'Morning')]")
        self.assert_text('Morning', '[auto-test-id="start-time-select"]')
        self.save_screenshot("safari details")

        # Day by Day safari palnning Transportation
        self.click('button[role="combobox"]:contains("Vehicle")')
        self.wait_for_element('div[role="option"]:contains("Open Game Drive Vehicle")')
        self.click('div[role="option"]:contains("Open Game Drive Vehicle")')

        # Accommodation
        self.click('button[role="combobox"]:contains("Lodge")')
        self.wait_for_element('div[role="option"]:contains("Camping")')
        self.click('div[role="option"]:contains("Camping")')

        # Meal Plan
        self.click('button[role="combobox"]:contains("Board")')
        self.wait_for_element('div[role="option"]:contains("Breakfast Only")')
        self.click('div[role="option"]:contains("Breakfast Only")')
        
        # Travelers This Day
        self.wait_for_element('input[type="number"]')
        self.clear('input[type="number"]')
        self.type('input[type="number"]', '2')

        # Special Requests for Day 1
        self.wait_for_element('textarea[placeholder*="special activities"]')
        self.type('textarea[placeholder*="special activities"]', "for a meeting with friends")

        # Additional Information Tell Us More About Your Dream Safari
        self.type('textarea#comments', "Explore more in tanzania")
        self.sleep(3)
        self.save_screenshot("day by day safari")

        # click request custom safari quote
        self.click('button[type="submit"][auto-test-id="tour-request-submit-button"]')

        # click your requests
        self.click('[auto-test-id="view-requests-button"]')
        self.save_screenshot("your requests")
        self.sleep(4)
        
        ## Activity title
        activity_title = self.get_text('[auto-test-id="request-activity-title"]')
        print("Activity Title:", activity_title)

        ## Tour request id
        tr_id = self.get_text("p[auto-test-id='request-origin-id']")
        print("TR ID:", tr_id)

        # Back to home
        self.click('[auto-test-id="back-to-tours-button"]')

        # tourist logout
        self.do_logout('tourist')

        
        # step4: Click Login with operator
        self.do_login("loc_operator@lala.com", "password@123#")


        # Verify successful login
        self.assert_text("Safari Operator Dashboard", "h1")

        # step5: Wait for the Submit Quote button to appear
        self.wait_for_element("button[auto-test-id='submit-quote-button']")

        # Click the Submit Quote button
        self.click("button[auto-test-id='submit-quote-button']")
        print("click on submit quote fill details and submit the quote")
        
        
        # step6: In your quote enter totalprice and validdate
        self.type('#price', '800')
        self.type('#valid_until', '30-07-2025')
        
        # In what's included select accommodation and transport
        self.click('[auto-test-id="quote-includes-selector-option-toll-charges"]')
        self.click('[auto-test-id="quote-includes-selector-option-park-fees"]')
 
        # Add Additionalnotes
        self.type('[auto-test-id="quote-notes-textarea"]', "This for a breakfast")
        self.sleep(3)
        self.save_screenshot("your quote details")

        # step6: click on the button submitquote
        self.click('[auto-test-id="quote-submit-button"]')
        
        # step7: operator logout
        self.do_logout("operator")

        # step8: Back To Home
        self.wait_for_element('[auto-test-id="back-to-home-button"]')
        self.scroll_to('[auto-test-id="back-to-home-button"]') 
        self.click('[auto-test-id="back-to-home-button"]')
        
        # step9: Tourist login
        self.do_login('tourist@demo.app', 'tourist@123!')
        

        # step10: Click the your requests
        self.click('[auto-test-id="view-requests-button"]')
        print("your requests dispaly successfull")
        self.sleep(3)


        # step11: open the eye icon button
        self.click('[auto-test-id="view-request-button"]')
        self.save_screenshot("request details")
        self.sleep(4)
        
        # quote id
        quote_id = self.get_text("p.text-xs.text-gray-600")
        print("Quote ID:", quote_id)
        
        # step12: Accept the Quote
        self.scroll_to('button:contains("Accept Quote")')
        self.click('button:contains("Accept Quote")')
        print("accepts the quote successfully")
        self.sleep(3)
        
        # close icon
        self.click("//div[@role='dialog']//button[.//span[text()='Close']]")
        
        # step13: Back to tours
        self.click('[auto-test-id="back-to-tours-button"]')

        # step14: tourist logout
        self.do_logout('tourist')
        
        # step15: Login with operator
        self.do_login("loc_operator@lala.com", "password@123#")

        ##Accepted Tab
        self.click('[auto-test-id="accepted-tab"]')
        self.sleep(3)
        
        ##operator logout
        self.do_logout("operator")