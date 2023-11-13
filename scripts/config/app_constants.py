class BaseUrl:
    base_url = "/v1.0/flipkart"


class Routes:
    user_route = BaseUrl.base_url + '/user'


class UserEndpoints:
    login = '/login'
    signup = '/signup'


class MongoCollections:
    user_collection = 'users'
