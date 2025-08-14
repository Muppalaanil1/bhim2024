class TouristActions:
   def submit_tour_request(self):    
        self.click('button:contains("Request Custom Tour")')
        print("click request custom tour to make request custom safari quote")
        
        ## Destination country
        self.click('button[data-testid="destination-country-select"]')
        self.click('//div[@role="option" and normalize-space(.)="Kenya"]')
        self.assert_text("Kenya", 'button[data-testid="destination-country-select"] span')
        
        ## Number of travelers
        self.click('button[data-testid="number-of-travelers-select"]')
        self.click('//div[@role="option" and normalize-space(.)="3 travelers"]')
        self.assert_text("3 travelers", 'button[data-testid="number-of-travelers-select"] span')

        ## preferred tour date
        self.type('input[type="date"]', "23-08-2025")

        ## tour duration
        self.click('button[data-testid="tour-duration-select"]')
        self.click('//div[@role="option" and normalize-space(.)="3 days"]')
        self.assert_text("3 days", 'button[data-testid="tour-duration-select"] span')
        print("enter basic information details")
      
        ## Day1
        ## origin city
        self.click('button[data-testid="day-1-destination-autocomplete"]')
        self.click('//div[@role="option" and contains(normalize-space(.), "Samburu")]')
        
        ## Time of day
        self.click('button[data-testid="day-1-time-of-day-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Evening")]')
        self.assert_text("Evening", 'button[data-testid="day-1-time-of-day-select"] span')

        ## Activity
        self.click('button[data-testid="day-1-activity-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Cultural Tours")]')
        self.assert_text("Cultural Tours", 'button[data-testid="day-1-activity-select"] span')

        ## Accommodation
        self.click('button[data-testid="day-1-accommodation-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Camping")]')
        self.assert_text("Camping", 'button[data-testid="day-1-accommodation-select"] span')
        
        ## Transport
        self.click('button[data-testid="day-1-transport-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Boat")]')
        self.assert_text("Boat", 'button[data-testid="day-1-transport-select"] span')
        
        ## Notes
        self.type('textarea[data-testid="day-1-notes-textarea"]', "this for a dinner")
        self.assert_text("this for a dinner", 'textarea[data-testid="day-1-notes-textarea"]')
        print("enter day 1 information details")

        
        ## Day2
        self.click('button:contains("Day 2")')
        
        ## origin city
        self.click('button[data-testid="day-2-destination-autocomplete"]')
        self.click('//div[@role="option" and contains(normalize-space(.), "Amboseli")]')
      
        ## Time of day
        self.click('button[data-testid="day-2-time-of-day-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Afternoon")]')
        self.assert_text("Afternoon", 'button[data-testid="day-2-time-of-day-select"] span')

        ## Activity
        self.click('button[data-testid="day-2-activity-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Walking Safari")]')
        self.assert_text("Walking Safari", 'button[data-testid="day-2-activity-select"] span')

        ## Accommodation
        self.click('button[data-testid="day-2-accommodation-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Luxury Lodge")]')
        self.assert_text("Luxury Lodge", 'button[data-testid="day-2-accommodation-select"] span')
        
        ## Transport
        self.click('button[data-testid="day-2-transport-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Train")]')
        self.assert_text("Train", 'button[data-testid="day-2-transport-select"] span')
        
        ## Notes
        self.type('textarea[data-testid="day-2-notes-textarea"]', "this for a meeting with friends")
        self.assert_text("this for a meeting with friends", 'textarea[data-testid="day-2-notes-textarea"]')
        print("enter day 2 information details")

        ## Day 3
        self.click('button:contains("Day 3")')

        ## origin city
        self.click('button[data-testid="day-3-destination-autocomplete"]')
        self.click('//div[@role="option" and contains(normalize-space(.), "Masai Mara")]')
       
        ## Time of day
        self.click('button[data-testid="day-3-time-of-day-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Evening")]')
        self.assert_text("Evening", 'button[data-testid="day-3-time-of-day-select"] span')

        ## Activity
        self.click('button[data-testid="day-3-activity-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Night Game Drive")]')
        self.assert_text("Night Game Drive", 'button[data-testid="day-3-activity-select"] span')

        ## Accommodation
        self.click('button[data-testid="day-3-accommodation-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Resort")]')
        self.assert_text("Resort", 'button[data-testid="day-3-accommodation-select"] span')
        
        ## Transport
        self.click('button[data-testid="day-3-transport-select"]')
        self.click('//div[@role="option" and contains(normalize-space(.),"Minibus")]')
        self.assert_text("Minibus", 'button[data-testid="day-3-transport-select"] span')
        
        ## Notes
        self.type('textarea[data-testid="day-3-notes-textarea"]', "this for a breakfast")
        self.assert_text("this for a breakfast", 'textarea[data-testid="day-3-notes-textarea"]')
        print("enter day 3 information details")

        # submit tour request button
        self.click('button[data-testid="submit-tour-request-btn"]')
        print("click submit tour request")