import fitbit
from gather import OAuth2Server

def fit_api():
    server = OAuth2Server('23B287', 'c63032a9dee4941ca40170e248b3dccc',redirect_uri='http://localhost:5000/')
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit('23B287', 'c63032a9dee4941ca40170e248b3dccc', 
                                 oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
    #Similar Multi thing can be access from https://python-fitbit.readthedocs.io/en/latest/#quickstart
    food_units = auth2_client.food_units()
    print(food_units)
    
    
if __name__ == '__main__':
    fit_api()