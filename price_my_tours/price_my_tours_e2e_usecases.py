from login_operations import LoginActions
from tourist_operations import TouristActions
from tours_operator_operations import OperatorActions
from seleniumbase import BaseCase
class price_my_tours(BaseCase, LoginActions, TouristActions, OperatorActions):

## This is testcase that verified end-to-end flow of tourism application
 def test_e2e_tour_request_flow(self):
       # Open the website
       self.open("https://zen-price-my-tours.lovable.app/") 
       print("opening the website")
       self.save_screenshot("zen-price website")
       self.sleep(2)
       '''
        # Click Login and perform login
        self.do_login('tourist@demo.app', 'tourist@123!')

        # tourist --> calling the tour request function
        self.submit_tour_request()
        
        # click on your requests
        self.click('[auto-test-id="view-requests-button"]')
        self.save_screenshot("your requests")
        self.sleep(4)

        # activity title 
        activity_title = self.get_text('[auto-test-id="request-activity-title"]')
        print("Activity Title:", activity_title)

        # enter the tour request
        tr_id = self.get_text("p[auto-test-id='request-origin-id']")
        print("TR ID:", tr_id)
        self.click('[auto-test-id="back-to-tours-button"]')

        # calling the logout for tourist
        self.do_logout('tourist')
       '''
       tr_id = 'eb0f'

       # calling the submit quote function
       self.submit_quote_for_request("sup_operator@demo.app", "password@123#", tr_id, 500, '30-07-2025')

       # calling the submit quote function
       self.submit_quote_for_request('ama_operator@demo.app', 'password@123#', tr_id, 650, '31-07-2025')

       # calling the submit quote function
       self.submit_quote_for_request("pat_operator@demo.com", "password@123#", tr_id, 999, '02-08-2025')

       # calling the submit quote function
       self.submit_quote_for_request("loc_operator@lala.com", "password@123#", tr_id, 700, '04-08-2025')
       
       # calling the submit quote function
       self.submit_quote_for_request("saf_operator@experts.com", "password@123#", tr_id, 1000, '31-07-2025')

       # Tourist login
       self.do_login('tourist@demo.app', 'tourist@123!')

       # click on your request
       self.click('[auto-test-id="view-requests-button"]')
       print("your requests dispaly successful")
       self.sleep(3)

       # click on eye icon button
       self.click('[auto-test-id="view-request-button"]')
       self.sleep(4)
        
       
       # calling operator tabs
       self.quote_tabs()

       # click on back tours button
       self.click("//div[@role='dialog']//button[.//span[text()='Close']]")
       self.click('[auto-test-id="back-to-tours-button"]')

       # calling the logout for tourist
       self.do_logout('tourist')

       # calling the login for operator
       #self.do_login("sup_operator@demo.app", "password@123#")
        
       # click on accepted tab
       #self.click('[auto-test-id="accepted-tab"]')
       #self.sleep(3)
    
       # calling the logout for operator
       #self.do_logout("operator")
       #self.sleep(3)
        
    
