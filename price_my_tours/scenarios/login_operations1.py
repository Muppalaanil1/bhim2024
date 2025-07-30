class LoginActions:
    def do_login(self, username, password):
        if not self.is_element_present('[auto-test-id="signin-submit-button"]'):
            self.click("button:contains('Login')")
        self.type('#signin-email', username)
        self.type('input[type="password"]', password)
        self.click("button:contains('Sign In')")
        print(f"sign in for {username} successful")

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