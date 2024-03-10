# Models

## BaseModel
This defines a class called `BaseModel` that serves as a base class for other classes in the Airbnb clone project. 
* It has an `__init__` method that initializes the instance attributes. 
	* If the `kwargs` parameter is not empty, it sets the instance attributes to the values in the dictionary `kwargs`. 
	* If the `kwargs` parameter is empty, it creates a new instance and sets a unique `id`, a `created_at` timestamp and an `updated_at` timestamp. 
	* It also uses the storage module to add the instance to a dictionary of instances.
* The `__str__` method returns a string representation of the instance.
* The `save` method updates the `updated_at` attribute and calls the `save` method from the `storage` module to save the updated instance.
* The `to_dict` method returns a dictionary of all the attributes of the instance in a `key-value` format, including the `__class__` attribute which represents the name of the class. 
* The `created_at` and `updated_at` attributes are converted to `ISO` format before being returned.

## Amenity
* This defines a class called `Amenity` which is a subclass of `BaseModel`. 
* `Amenity` class has one class attribute called `name`, which is an empty string. 
	* *Class attributes are attributes that are shared among all instances of the `class`.*
* `BaseModel` is a parent class that provides `Amenity` with instance attributes such as `id`, `created_at`, `updated_at`,` __str__` method for string representation of the instance and `to_dict` method that returns a dictionary representation of the instance attributes.
* `Amenity` does not have its own constructor method (`__init__`) so it will inherit `BaseModel`'s constructor method. 
* The `name` attribute is not defined in the `__init__` method, which means it will not be an instance attribute but rather a class attribute that can be accessed by all instances of the `Amenity` class.

## User
* This is a class named `User` that inherits from the `BaseModel` class defined `base_model` module. 
* The `User` class has four **class-level** attributes: `email`, `password`, `first_name`, and `last_name`.

* **Class-level** attributes are shared across all instances of the class and can be accessed using either the class name or an instance of the class. 
		* **For example**, you could access the `email` attribute of the `User` class using either `User.email` or `user_instance.email`, where `user_instance` is an instance of the `User` class.
* The implementation for methods like `__init__()`, `__str__()`, `save()`, and `to_dict()` will be inherited from the `BaseModel` class.

## State
* This defines a class called `State` which is a subclass of `BaseModel`. 
* State class has one class attribute called `name`, which is an empty string. 
	* *Class attributes are attributes that are shared among all instances of the `class`.*
* `BaseModel` is a parent class that provides `State` with instance attributes such as `id`, `created_at`, `updated_at`,` __str__` method for string representation of the instance and `to_dict` method that returns a dictionary representation of the instance attributes.
* `State` does not have its own constructor method (`__init__`) so it will inherit `BaseModel`'s constructor method. 
* The `name` attribute is not defined in the `__init__` method, which means it will not be an instance attribute but rather a class attribute that can be accessed by all instances of the `State` class.

## Place
This module defines a `Place` class that inherits from `BaseModel` and contains several attributes that define the characteristics of a place.

### Dependencies
This module requires `BaseModel` class to be imported from `models.base_model`.
### Attributes
To use this class, simply import it and create an instance of it, providing values for the attributes as desired. The available attributes are:

* `city_id`: The `ID` of the `city` where the place is located.
* `user_id`: The `ID` of the `user` who owns the place.
* `name`: The `name` of the place.
* `description`: A brief description of the place.
* `number_rooms`: The number of rooms in the place.
* `number_bathrooms`: The number of bathrooms in the place.
* `max_guest`: The maximum number of guests the place can accommodate.
* `price_by_night`: The price per night to stay at the place.
* `latitude`: The latitude of the place's location.
* `longitude`: The longitude of the place's location.
* `amenity_ids`: A list of IDs of the amenities available at the place.
### Example
```
from models.place import Place

my_place = Place(city_id="1", user_id="123", name="My Cool Place", description="A place to crash", number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=50.0, latitude=37.7749, longitude=-122.4194, amenity_ids=[1, 2, 3])
```
*In this example, an instance of `Place` is created with the specified attributes. The instance can be manipulated further as needed.*

## City
This module defines the City class, a subclass of the BaseModel class, which represents a city and its attributes.

### Usage
To use the `City` class, import it into your Python script:
```
from models.city import City
```
Then, create an instance of the City class, passing in the required attributes:
```
my_city = City(state_id="1234", name="New York")
```
### Attributes
The `City` class has the following instance attributes:

* `id`: a string representing a unique identifier for the city.
* `created_at`: a `datetime` object representing the date and time when the city instance was created.
* `updated_at`: a `datetime` object representing the date and time when the city instance was last updated.
* `state_id`: a string representing the `id` of the state that the city belongs to.
* `name`: a string representing the `name` of the city.
### Methods
The `City` class inherits methods from its parent class, `BaseModel`. These methods include `__str__()`, `to_dict()`, `save()`, and `delete()`.

## Review
* This module contains the `Review` class, which is a subclass of the `BaseModel` class. 
* It defines the attributes of a review instance, including the `place_id`, `user_id`, and `text`.
### Attributes
The `Review` class has the following attributes:

* `id`: string - a unique identifier for the review instance.
* `created_at`: datetime - the date and time the review instance was created.
* `updated_at`: datetime - the date and time the review instance was last updated.
* `place_id`: string - the ID of the place that the review is for.
* `user_id`: string - the ID of the user who wrote the review.
* `text`: string - the text of the review.

### Methods
The `Review` class inherits several methods from its parent class, `BaseModel`. These methods include:

* `__init__(self, *args, **kwargs)`: Initializes a new Review instance. Accepts optional keyword arguments that correspond to the instance attributes.
* `__str__(self)`: Returns a string representation of the Review instance.
* `save(self)`: Saves the Review instance to a JSON file.
* `to_dict(self)`: Returns a dictionary representation of the Review instance.
### Example
Here is an example of how you might use the Review class:
```
from models.review import Review

review = Review(place_id="123", user_id="456", text="This place is great!")
review.save()

```
This would create a new `Review` instance with the given attributes, and then save it to a JSON file.
