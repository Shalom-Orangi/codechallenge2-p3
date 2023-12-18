class Restaurant:
    def __init__(self,name):
        self._name=name
        #underscore after the period(.) indicates that the name cannot be changed
        self.reviews =[]

    @property
    def name(self):
        return self._name
    

#Object Relationship Methods
    def add_review (self,review):
        self._reviews.append(review)

    def reviews(self):
        return self.reviews
    
    def customers(self):
        unique_customers=set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)
    
    #Aggregate and Association Methods
    def average_star_rating(self):
        if len(self.reviews)==0:
            total_ratings= sum (review.rating()for review in self.reviews)
            return total_ratings/len(self.reviews)
    

restaurant= Restaurant("Chakula Tamu")
print (restaurant.name())