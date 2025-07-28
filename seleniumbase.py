from seleniumbase import BaseCase

class SafariLoginTests(BaseCase):

    def login_and_verify(self, username, password, role):
        """Reusable function to log in and verify"""
        # Replace with your actual working login URL
        self.open("https://abcd-price-my-safari.lovable.app/")

        
        self.click("button:contains('Login')")
        # Fill in the login form
        self.type("#signin-email", username, timeout=10)
        self.type("#signin-password", password, timeout=10)

        self.click("button:contains('Sign In')")

        # Verify the dashboard or welcome message
        self.assert_text(f"Welcome {role}", "h1")

        # Optional: Log out and verify returned to login page
        self.click("#logout-link")
        if role == 'Admin':
            self.assert_text("Admin Dashboard", "h1")
        elif role == 'Tourist':
            self.assert_true("button.contains('Your Requests')")
        elif role == "Operator":
            self.assert_text("Safari Operator Dashboard", "h1")
        else:
            print(f"Unsupport Role - {role}")
            raise ValueError(f"UnSupported Role")

        
    def test_admin_login(self):
        """Test login for Admin"""
        self.login_and_verify(
            username="admin@123.com",
            password="admin@123#",
            role="Admin"
        )

    def test_operator_login(self):
        """Test login for Operator"""
        self.login_and_verify(
            username="hos_operator@gmail.com",
            password="operator@123#",
            role="Operator"
        )

    def test_tourist_login(self):
        """Test login for Tourist"""
        self.login_and_verify(
            username="tourist@123.app",
            password="tourist@1234#",
            role="Tourist"
        )
