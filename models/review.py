

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def __str__(self):
        return f"Review: {self.rating_value} stars by {self.customer.full_name()} for {self.restaurant.name_value}"



