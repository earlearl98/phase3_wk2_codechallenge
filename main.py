# main.py
# main.py
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

# Your code and test cases can be added here

# Example usage:
# customer1 = Customer("John", "Doe")
# restaurant1 = Restaurant("Restaurant A")
# customer1.add_review(restaurant1, 4)
# print(customer1.num_reviews())
# print(restaurant1.average_star_rating())


# # Import the classes from your implementation
# from models.customer import Customer
# from models.restaurant import Restaurant
# # from models.review import Review
# # Create customers
# customer1 = Customer("John", "Doe")
# customer2 = Customer("Jane", "Smith")

# # Create restaurants
# restaurant1 = Restaurant("Fantastic Burgers")
# restaurant2 = Restaurant("Pizza Paradise")

# # Customers add reviews
# customer1.add_review(restaurant1, 4)
# customer1.add_review(restaurant2, 5)
# customer2.add_review(restaurant1, 3)

# # Access information
# print("Customers:")
# for customer in Customer.all():
#     print(f"{customer.full_name()} has reviewed: {', '.join(restaurant.name for restaurant in customer.restaurants())}")

# print("\nRestaurants:")
# for restaurant in Restaurant.all():
#     print(f"{restaurant.name} has been reviewed by: {', '.join(customer.full_name() for customer in restaurant.customers())}")
#     print(f"Average rating: {restaurant.average_star_rating()}")

# print("\nReviews:")
# for review in Review.all():
#     print(f"{review.customer().full_name()} gave {review.restaurant().name} a rating of {review.rating()} stars")

# # Additional examples of aggregate and association methods
# print("\nAggregate and Association Methods:")
# print(f"{customer1.full_name()} has authored {customer1.num_reviews()} reviews")

# found_customer = Customer.find_by_name("John Doe")
# if found_customer:
#     print(f"Found customer by name: {found_customer.full_name()}")
# else:
#     print("Customer not found")

# customers_with_given_name = Customer.find_all_by_given_name("Jane")
# print(f"All customers with given name 'Jane': {[customer.full_name() for customer in customers_with_given_name]}")
