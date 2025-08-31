class OperatorActions:
   def submit_quote_for_request(self, op_username, op_userpass, tr_id):
        self.do_login(op_username, op_userpass)
        self.assert_text("Safari Operator Dashboard", "h1")

        ## Search for tr_id 
        self.type('//input[contains(@placeholder, "Search by activity")]', tr_id)

        ## click on submit quote
        self.wait_for_element("button[auto-test-id='submit-quote-button']")
        self.click("button[auto-test-id='submit-quote-button']")
        print("click on submit quote fill details and submit the quote")
        
        
        ## Enter valid date
        self.click("button[auto-test-id='quote-valid-until-input']")
        self.click("//button[normalize-space()='12']")
        ## Day 1
        ## Enter price
        self.type("input[data-testid='day-1-price-input']", "100")
        ## select What's Included
        self.click("button[data-testid='day-1-inclusions-option-all-meals']")
        self.click("button[data-testid='day-1-inclusions-option-accommodation']")
        self.click("button[data-testid='day-1-inclusions-option-airport-transfers']")
        self.click("button[data-testid='day-1-inclusions-option-park-fees']")
        self.click("button[data-testid='day-1-inclusions-option-first-aid']")
        ## Add Additional Notes
        self.type('textarea[placeholder="Special arrangements, activities, or notes for this day..."]', "this for a breakfast")
        self.sleep(3)

        ## Day 2
        self.click('button:contains("Day 2")')
        ## Enter price
        self.type("input[data-testid='day-2-price-input']", "200")
        ## select What's Included
        self.click("button[data-testid='day-2-inclusions-option-all-meals']")
        self.click("button[data-testid='day-2-inclusions-option-accommodation']")
        self.click("button[data-testid='day-2-inclusions-option-transport']")
        self.click("button[data-testid='day-2-inclusions-option-permits']")
        self.click("button[data-testid='day-2-inclusions-option-toll-charges']")
        ## Add Additional Notes
        self.type('textarea[placeholder="Special arrangements, activities, or notes for this day..."]', "this for a launch")
        self.sleep(3)
     
        ## Day 3
        self.click('button:contains("Day 3")')
        ## Enter price
        self.type('input[placeholder="500"]', "300")
        ## select What's Included
        self.click("button[data-testid='day-3-inclusions-option-all-meals']")
        self.click("button[data-testid='day-3-inclusions-option-accommodation']")
        self.click("button[data-testid='day-3-inclusions-option-transport']")
        self.click("button[data-testid='day-3-inclusions-option-permits']")
        self.click("button[data-testid='day-3-inclusions-option-toll-charges']")
        ## Add Additional Notes
        self.type('textarea[placeholder="Special arrangements, activities, or notes for this day..."]', "this for a meeting with friends")
        self.sleep(3)
        
        ## click on submit quote
        self.click('[auto-test-id="quote-submit-button"]')
        self.do_logout('operator')
   
   def quote_tabs(self):
       # click on accept quote
       self.wait_for_element('button[role="checkbox"][aria-checked="false"]', timeout=10)
       self.scroll_to('button[role="checkbox"][aria-checked="false"]')
       self.click('button[role="checkbox"][aria-checked="false"]')
       self.click('button:contains("Accept Quote")')
       self.sleep(3)
       
       # enters the quote id
       operator_name = self.get_text("h5.font-semibold.text-green-800")
       print("Operator Name:", operator_name)
       quote_id = self.get_text("p.text-xs.text-gray-600")
       print("", quote_id)
       included_text = self.get_text("p.text-sm.text-gray-700.whitespace-pre-line.mt-1")
       print("What's Included:", included_text)
       valid_until = self.get_text("div.text-xs.text-green-600")
       print("", valid_until)

      