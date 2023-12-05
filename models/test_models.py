
import unittest
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

class TestCustomerRestaurantReview(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("John", "Doe")
        self.customer2 = Customer("Jane", "Smith")
        self.restaurant1 = Restaurant("Restaurant A")
        self.restaurant2 = Restaurant("Restaurant B")

    def test_customer_creation(self):
        self.assertEqual(self.customer1.given_name, "John")
        self.assertEqual(self.customer1.family_name, "Doe")

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant1.name(), "Restaurant A")

    def test_review_creation(self):
        self.customer1.add_review(self.restaurant1, 4)
        self.assertEqual(len(self.customer1.reviews), 1)
        self.assertEqual(self.customer1.reviews[0].rating(), 4)

    def test_restaurant_average_star_rating(self):
        self.customer1.add_review(self.restaurant1, 4)
        self.customer2.add_review(self.restaurant1, 5)

       
        print(self.restaurant1.reviews)


    def test_find_customer_by_name(self):
        found_customer = Customer.find_by_name("John Doe")
        self.assertEqual(found_customer.given_name, self.customer1.given_name)
        self.assertEqual(found_customer.family_name, self.customer1.family_name)


    def test_find_all_customers_by_given_name(self):
        found_customers = Customer.find_all_by_given_name("John")
        self.assertIn(self.customer1, found_customers)
        self.assertNotIn(self.customer2, found_customers)

if __name__ == "__main__":
    unittest.main()
