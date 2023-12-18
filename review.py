from customer import Customer
from restaurant import Restaurant

class Review:
    all_reviews=[]

    def __init__(self,customer,restaurant,rating):
        self._customer=customer
        self._restaurant=restaurant
        self._rating=rating
        
        Review.all_reviews.append(self)

    def rating(self):
        if not isinstance(self._rating,int):
            print("Rating must be an integer")
        else :
            return self._rating
        
    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews
    
#Object Relationship Methods
    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant
    
    
customer1=Customer("Shalom","Orangi")
restaurant1=Restaurant("Chakula Tamu")

review1=Review(customer1,restaurant1,3)

#getting reviews and printing them
reviews=Review.all()
for review in reviews:
  print(f"Customer:{review.customer.full_name()},Rating: {review.rating()}")

#getting rating
rating=review1._rating
print(f"Rating for review1:{rating}")