# phase3_wk2_codechallenge
# Customer, Restaurant, and Review Management System


This Python project implements a simple system for managing customers, restaurants, and reviews. The system is organized into three classes: Customer, Restaurant, and Review. These classes allow you to create and manage customer data, restaurant data, and customer reviews of restaurants.

# Table of Contents

Classes
Customer
Restaurant
Review
Usage
Methods
Example Script
License
Contributing
Acknowledgments
Classes
Customer
The Customer class represents a customer and their interactions with the system.

# Attributes
given_name: The given name of the customer.
family_name: The family name of the customer.
reviews: A list of reviews authored by the customer.
Methods
__init__(given_name, family_name): Initializes a new customer with the given name and family name.
given_name(): Returns the given name of the customer.
family_name(): Returns the family name of the customer.
full_name(): Returns the full name of the customer.
all(): Returns a list of all customer instances.
restaurants(): Returns a unique list of all restaurants reviewed by the customer.
add_review(restaurant, rating): Adds a new review for a given restaurant and rating.
num_reviews(): Returns the total number of reviews authored by the customer.
find_by_name(name): Class method - Finds a customer by their full name.
find_all_by_given_name(given_name): Class method - Finds all customers with a given name.
Restaurant
The Restaurant class represents a restaurant and its reviews.

# Attributes
name: The name of the restaurant.
reviews: A list of reviews for the restaurant.
Methods
__init__(name): Initializes a new restaurant with the given name.
name(): Returns the name of the restaurant.
all(): Returns a list of all restaurant instances.
reviews(): Returns a list of all reviews for the restaurant.
customers(): Returns a unique list of all customers who have reviewed the restaurant.
average_star_rating(): Returns the average star rating based on reviews.
Review
The Review class represents a customer's review of a restaurant.

# Attributes
customer: The customer who wrote the review.
restaurant: The restaurant being reviewed.
rating_value: The rating given in the review.
Methods
__init__(customer, restaurant, rating): Initializes a new review with a customer, restaurant, and rating.
rating(): Returns the rating value.
all(): Returns a list of all reviews.
customer(): Returns the customer object for that review.
restaurant(): Returns the restaurant object for that given review.
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/[Your Username]/[Your Project Name].git
cd [Your Project Name]
(Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Explore the classes and methods in the your_module_name module. Feel free to integrate this module into your own projects.

# Methods
The classes provide a variety of methods for managing customer, restaurant, and review data. These methods include initialization, data retrieval, and aggregation.

# Customer Methods
given_name(), family_name(), full_name(): Get information about the customer's name.
all(): Get all customer instances.
restaurants(): Get a unique list of all restaurants a customer has reviewed.
add_review(restaurant, rating): Add a review for a given restaurant with a star rating.
num_reviews(): Get the total number of reviews that a customer has authored.
find_by_name(name): Find a customer by their full name.
find_all_by_given_name(given_name): Find all customers with a given name.
Restaurant Methods
name(): Get the restaurant's name.
all(): Get all restaurant instances.
reviews(): Get a list of all reviews for the restaurant.
customers(): Get a unique list of all customers who have reviewed a particular restaurant.
average_star_rating(): Get the average star rating for a restaurant based on its reviews.
Review Methods
rating(): Get the rating for a restaurant.
all(): Get all reviews.
customer(): Get the customer object for that review.
restaurant(): Get the restaurant object for that given review.
Example Script
A script (main.py) is provided to demonstrate the usage of the classes and methods. Run the script using:

bash
Copy code
python main.py
This script creates customers, restaurants, and reviews, and then prints information about them using the specified methods.

# License
This project is licensed under the MIT License.

# Contributing
Feel free to contribute to the project. Fork the repository, make your changes, and submit a pull request.

# Acknowledgments
Special thanks to [Your Name] for creating this awesome project!
Inspired by [Any external projects or tutorials that inspired your project]
This README provides comprehensive information about the project, including details about the classes, their methods, how to use the project, licensing information, contribution guidelines, and acknowledgments. Customize it further based on your project's specific details and requirements.





