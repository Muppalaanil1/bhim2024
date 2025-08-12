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

      # Click Login and perform login
      self.do_login('tourist@demo.app', 'tourist@123!')

      # tourist --> calling the tour request function
      self.submit_tour_request()
        
      # click on your requests
      self.click('[auto-test-id="view-requests-button"]')
      #self.save_screenshot("your requests")
      self.sleep(4)
     
      # click all tab
      self.click("button[auto-test-id='all-requests-tab']")

      # activity title 
      activity_title = self.get_text('[auto-test-id="request-activity-title"]')
      print("Activity Title:", activity_title)

      # Get latest the tour request
      tr_id = self.get_text("p[auto-test-id='request-origin-id']")
      tr_id = tr_id.split('-')[1]
      print("TR ID:", tr_id)
      self.click('[auto-test-id="back-to-tours-button"]')

      # calling the logout for tourist
      self.do_logout('tourist')
      
      # calling the submit quote function
      self.submit_quote_for_request("saf_operator@experts.com", "password@123#", tr_id, '20-08-2025')

      # Tourist login
      self.do_login('tourist@demo.app', 'tourist@123!')

      # click on your request
      self.click('[auto-test-id="view-requests-button"]')
      print("your requests dispaly successful")
      self.sleep(3)

      # click all tab
      self.click("button[auto-test-id='all-requests-tab']")

      # click on eye icon button
      self.click('[auto-test-id="view-request-button"]')
      self.sleep(4)
        
      # click on accept quote
      self.quote_tabs()
      
      # click on back tours button
      self.click("//div[@role='dialog']//button[.//span[text()='Close']]")
      self.click('[auto-test-id="back-to-tours-button"]')

      # calling the logout for tourist
      self.do_logout('tourist')
        
