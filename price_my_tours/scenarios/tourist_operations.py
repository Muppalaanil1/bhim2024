class TouristActions:
   def submit_tour_request(self):    
        self.click('button:contains("Request Custom Tour")')
        print("click request custom tour to make request custom safari quote")
        #self.save_screenshot("tourist page")

        ## select Safari Experience
        self.click('[auto-test-id="activity-type-select"]')
        self.click("//div[@role='option' and contains(., 'Mountain Climbing (Kilimanjaro)')]")

        ## select Number of Travelers
        self.clear('[auto-test-id="guests-input"]')
        self.type('[auto-test-id="guests-input"]', '4')

        ## select Safari Duration
        self.clear('[auto-test-id="number-of-days-input"]')
        self.type('[auto-test-id="number-of-days-input"]', '2')

        ## select Destination Country
        self.click('[auto-test-id="country-select"]')
        self.click("//div[@role='option' and contains(., 'Kenya')]")
        self.assert_text('Kenya', '[auto-test-id="country-select"]')

        ## select Preferred Start Time
        self.click('[auto-test-id="start-time-select"]')
        self.click("//div[@role='option' and contains(., 'Afternoon')]")
        self.assert_text('Afternoon', '[auto-test-id="start-time-select"]')
        #self.save_screenshot("safari details")

        # preferred safari date
        self.wait_for_element('[auto-test-id="preferred-date-input"]', timeout=10)
        self.type('[auto-test-id="preferred-date-input"]', '09-08-2025')
        preferred_date = self.get_value('[auto-test-id="preferred-date-input"]')
        print("preferred_safari_date:", preferred_date)

        ## select Transportation
        self.click('button[role="combobox"]:contains("Vehicle")')
        self.wait_for_element('div[role="option"]:contains("Safari Minibus")')
        self.click('div[role="option"]:contains("Safari Minibus")')

        ## select Accommodation
        self.click('button[role="combobox"]:contains("Lodge")')
        self.wait_for_element('div[role="option"]:contains("Mid-range Lodge")')
        self.click('div[role="option"]:contains("Mid-range Lodge")')

        ## select Meal Plan
        self.click('button[role="combobox"]:contains("Board")')
        self.wait_for_element('div[role="option"]:contains("No Meals")')
        self.click('div[role="option"]:contains("No Meals")')

        ## select Travelers This Day
        self.wait_for_element('input[type="number"]')
        self.clear('input[type="number"]')
        self.type('input[type="number"]', '2')

        ## select Special Requests for Day 1
        self.wait_for_element('textarea[placeholder*="special activities"]')
        self.type('textarea[placeholder*="special activities"]', "for a meeting with friends")
        self.type('textarea#comments', "Explore more in kenya")
        self.sleep(3)
        #self.save_screenshot("day by day safari")

        ## click on your request
        self.click('button[type="submit"][auto-test-id="tour-request-submit-button"]')
