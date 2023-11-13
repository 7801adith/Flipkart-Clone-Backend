class BaseUrl:
    base_url = "/v1.0/flipkart"


class Routes:
    user_route = BaseUrl.base_url + '/user'


class UserEndpoints:
    login = '/login'
    signup = '/signup'


class MongoCollections:
    user_collection = 'users'


class Regex:
    phone_regex = r'^\d[-\d\s]*\d$'
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
