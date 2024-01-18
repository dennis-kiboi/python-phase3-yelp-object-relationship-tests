import unittest


class Customer:
    pass


class Restaurant:
    pass


class Review:
    pass


class TestCustomer(unittest.TestCase):

    def setUp(self):
        """Setup method to run before each test case"""

        # Customers
        self.john_doe = Customer("John", "Doe")
        self.jane_smith = Customer("Jane", "Smith")

        # Restaurants
        self.java = Restaurant("Java")
        self.about_thyme = Restaurant("About Thyme")

        # Reviews
        self.john_review = Review(self.john_doe, self.java, 5)
        self.jane_review = Review(self.jane_smith, self.about_thyme, 8)

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """

        Customer._all = []
        Restaurant._all = []
        Review._all = []

    def test_init(self):
        """Test if the Customer objects were initialized properly"""

        self.assertEqual(self.john_doe.given_name, 'John')
        self.assertEqual(self.john_doe.family_name, 'Doe')

        self.assertEqual(self.jane_smith.given_name, 'Jane')
        self.assertEqual(self.jane_smith.family_name, 'Smith')

    def test_given_name_change(self):
        """Test if the given name can be changed after initialization"""
        self.john_doe.given_name = "Joe"
        self.jane_smith.given_name = "Sue"

        self.assertEqual(self.john_doe.given_name, "Joe")
        self.assertEqual(self.jane_smith.given_name, "Sue")

    def test_full_name(self):
        """Test if the fullname property returns the name concatenated Western Style"""

        self.assertEqual(self.john_doe.full_name, "John Doe")
        self.assertEqual(self.jane_smith.full_name, "Jane Smith")

    def test_all(self):
        """Test if all instances of the Customer class were added to the all list"""

        self.assertEqual(len(Customer.all()), 2)

    def test_restaurants(self):
        """Test if the restaurants property returns a unique list of all restaurants a customer has reviewed"""

        self.jane_review_2 = Review(self.jane_smith, self.java, 7)

        self.jane_review_2 = Review(self.jane_smith, self.about_thyme, 10)

        self.assertTrue(len(self.jane_smith.restaurants) ==
                        len(set(self.jane_smith.restaurants)))

    def test_add_review(self):
        """Test if add_review method creates a new review and associates it with that customer and restaurant"""

        kilimanjaro = Restaurant("Kilimanjaro")

        self.john_doe.add_review(kilimanjaro, 2)

        self.assertTrue(kilimanjaro in self.john_doe.restaurants)

    def test_num_reviews(self):
        """Test if num_reviews() method returns the total number of reviews that a customer has authored"""

        self.assertEqual(self.john_doe.num_reviews(), 1)
        self.assertEqual(self.jane_smith.num_reviews(), 1)

    def test_find_by_name(self):
        """Test if find_by_name() method returns the first customer whose full name matches"""

        self.assertEqual(Customer.find_by_name(
            "John Doe").full_name, "John Doe")

    def test_find_all_by_given_name(self):
        """Test if find_all_by_given_name() method returns a list containing all customer with that given name"""

        new_customer = Customer("John", "Smith")
        self.assertEqual(len(Customer.find_all_by_given_name("John")), 2)


class TestRestaurant(unittest.TestCase):

    def setUp(self):
        """Setup method to run before each test case"""

        # Customers
        self.john_doe = Customer("John", "Doe")
        self.jane_smith = Customer("Jane", "Smith")

        # Restaurants
        self.java = Restaurant("Java")
        self.about_thyme = Restaurant("About Thyme")

        # Reviews
        self.john_review = Review(self.john_doe, self.java, 5)
        self.jane_review = Review(self.jane_smith, self.about_thyme, 8)

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """

        Customer._all = []
        Restaurant._all = []
        Review._all = []

    def test_init(self):
        """Test if the Restaurant objects were initialized properly"""

        self.assertEqual(self.java.name, 'Java')
        self.assertEqual(self.about_thyme.name, 'About Thyme')

    def test_name_change(self):
        """Test if the name can be changed after initialization"""
        with self.assertRaises(AttributeError):
            self.java.name = "New Java"
            self.about_thyme = "Thyme"

    def test_reviews(self):
        """Test if the reviews property returns a list of all reviews for a restaurant"""
        self.assertEqual(len(self.java.reviews), 1)

    def test_customers(self):
        """Test if the customer property returns a unique list of all customers who have reviewed a particular restaurant"""

        self.john_review_2 = Review(self.john_doe, self.java, 8)

        self.assertTrue(len(self.java.customers) ==
                        len(set(self.java.customers)))

    def test_average_star_rating(self):
        self.jane_smith.add_review(self.java, 10)
        self.assertEqual(self.java.average_star_rating(), 7.5)


class TestReview(unittest.TestCase):
    def setUp(self):
        """Setup method to run before each test case"""

        # Customers
        self.john_doe = Customer("John", "Doe")
        self.jane_smith = Customer("Jane", "Smith")

        # Restaurants
        self.java = Restaurant("Java")
        self.about_thyme = Restaurant("About Thyme")

        # Reviews
        self.john_review = Review(self.john_doe, self.java, 5)
        self.jane_review = Review(self.jane_smith, self.about_thyme, 8)

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """

        Customer._all = []
        Restaurant._all = []
        Review._all = []

    def test_init(self):
        """Test if the Review objects were initialized properly"""

        self.assertEqual(self.john_review.restaurant.name, "Java")
        self.assertEqual(self.jane_review.restaurant.name, 'About Thyme')

        self.assertEqual(self.john_review.rating, 5)
        self.assertEqual(self.jane_review.rating, 8)

    def test_all(self):
        """Test if all instances of the Review class were added to the all list"""

        self.assertEqual(len(Review.all()), 2)

    def test_customer(self):
        """Test if customer property returns the customer object for that review"""

        self.assertEqual(self.john_review.customer.full_name, "John Doe")
        self.assertEqual(self.jane_review.customer.full_name, "Jane Smith")

    def test_customer_change(self):
        """Test if the customer can be changed after initialization"""

        self.any_other = Customer("Any", "Other")

        with self.assertRaises(AttributeError):
            self.jane_review.customer = self.any_other


if __name__ == "__main__":
    unittest.main()
