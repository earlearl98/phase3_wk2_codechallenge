# models/customer.py
from models.review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set(review.restaurant() for review in self.reviews))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]

    def __str__(self):
        return f"Customer: {self.full_name()}"





# class Customer:
#     all_customers = []

#     def __init__(self, given_name, family_name):
#         self.given_name = given_name
#         self.family_name = family_name
#         self.reviews = []
#         Customer.all_customers.append(self)

#     def given_name(self):
#         return self.given_name

#     def family_name(self):
#         return self.family_name

#     def full_name(self):
#         return f"{self.given_name} {self.family_name}"

#     @classmethod
#     def all(cls):
#         return cls.all_customers

#     def restaurants(self):
#         return list(set(review.restaurant() for review in self.reviews))

#     def add_review(self, restaurant, rating):
#         review = Review(self, restaurant, rating)
#         self.reviews.append(review)

