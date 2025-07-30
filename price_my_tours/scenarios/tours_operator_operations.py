class OperatorActions:
   def submit_quote_for_request(self, op_username, op_userpass, tr_id, valid_date):
        self.do_login(op_username, op_userpass)
        self.assert_text("Safari Operator Dashboard", "h1")

        ## Search for tr_id 
        self.type('//input[contains(@placeholder, "Search by activity")]', tr_id)

        ## click on submit quote
        self.wait_for_element("button[auto-test-id='submit-quote-button']")
        self.click("button[auto-test-id='submit-quote-button']")
        print("click on submit quote fill details and submit the quote")

        ## Enter valid date
        self.type('#valid_until', valid_date)

        ## Enter price
        self.type('input[placeholder="500"]', "100")


        ## select What's Included
        self.click('[auto-test-id="undefined-option-transport"]')
        self.click('[auto-test-id="undefined-option-all-meals"]')

        ## Add Additional Notes
        self.type('textarea[placeholder="Special arrangements, activities, or notes for this day..."]', "this for a breakfast")
        self.sleep(3)

        ## click on submit quote
        self.click('[auto-test-id="quote-submit-button"]')
        self.do_logout('operator')
   
   def quote_tabs(self):
       # click on accept quote
       self.scroll_to('button:contains("Accept Quote")')
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

      