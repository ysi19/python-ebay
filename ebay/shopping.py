from ConfigParser import ConfigParser
import requests
from utils import relative

# Item Search
def FindProducts(encoding, query, available_items, max_entries):
    
    user_param={'callname' : FindProducts.__name__,
                'responseencoding' : encoding,
                 'QueryKeywords' : query,
                 'AvailableItemsOnly' : available_items,
                 'MaxEntries' : max_entries}
    
    response = get_response(user_param)
    return response.content
    
def FindHalfProducts(encoding="JSON", query=None, max_entries=None, product_type=None, product_value=None, include_selector=None):                  
    if product_type and product_value and include_selector:
        user_param = {'callname' : FindHalfProducts.__name__,
                      'responseencoding' : encoding, 
                      'ProductId.type' : product_type,
                      'ProductId.Value' : product_value,
                      'IncludeSelector' : include_selector}
        
    if query and max_entries:
        user_param = {'callname' : FindHalfProducts.__name__,
                  'responseencoding' : encoding,
                  'QueryKeywords' : query,
                  'MaxEntries' : max_entries}

    response = get_response(user_param)
    return response.content

# Item Data
def GetSingleItem(encoding, item_id, include_selector=None):
    user_param={'callname' : GetSingleItem.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    if include_selector:
        user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content
    
def GetItemStatus(encoding, item_id):
    user_param={'callname' : GetItemStatus.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    response = get_response(user_param)
    return response.content
    
def GetShippingCosts(encoding, item_id, destination_country_code, destination_postal_code, details, quantity_sold):
    user_param={'callname' : GetShippingCosts.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id,
                'DestinationCountryCode' : destination_country_code, 
                'DestinationPostalCode' : destination_postal_code, 
                'IncludeDetails' : details, 
                'QuantitySold' : quantity_sold}
    
    response = get_response(user_param)
    return response.content 
    
def GetMultipleItems(encoding, item_id):
    user_param={'callname' : GetMultipleItems.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}
    
    response = get_response(user_param)
    return response.content

# User Reputation
def GetUserProfile(encoding, user_id, include_selector=None):
    user_param={'callname' : GetUserProfile.__name__,
                'responseencoding' : encoding,
                'UserID' : user_id}
   
    if include_selector:
       user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content
 

# eBay pop!
def FindPopularSearches(encoding, query, category_id=None):
    user_param={'callname' : FindPopularSearches.__name__,
                'responseencoding' : encoding,
                'QueryKeywords' : query}
   
    if category_id:
       user_param['CategoryID'] = category_id
    
    response = get_response(user_param)
    return response.content

    
def FindPopularItems(encoding, query, category_id_exclude=None):
    user_param={'callname' : FindPopularItems.__name__,
                'responseencoding' : encoding,
                'QueryKeywords' : query}
   
    if category_id_exclude:
       user_param['CategoryIDExclude'] = category_id_exclude
    
    response = get_response(user_param)
    return response.content

    
# Search: Bug in eBay documentation of Product Id: http://developer.ebay.com/devzone/shopping/docs/callref/FindReviewsAndGuides.html#Samples
def FindReviewsandGuides(encoding, category_id=None, product_id=None):
    if category_id:
        user_param={'callname' : FindReviewsAndGuides.__name__,
                'responseencoding' : encoding,
                'CategoryID' : category_id}
   
    if product_id:
        user_param={'callname' : FindReviewsandGuides.__name__,
                'responseencoding' : encoding,
                'ProductID' : product_id}
                
    response = get_response(user_param)
    return response.content


# Utilities
def GetCategoryInfo(encoding, category_id, include_selector=None):
    if category_id:
        user_param={'callname' : GetCategoryInfo.__name__,
                'responseencoding' : encoding,
                'CategoryID' : category_id}
   
    if include_selector:
        user_param['IncludeSelector'] = include_selector 
                
    response = get_response(user_param)
    return response.content
 
def GeteBayTime(encoding):
    user_param={'callname' : GeteBayTime.__name__,
                'responseencoding' : encoding}
                
    response = get_response(user_param)
    return response.content 
    

#requests method
def get_response(user_params):
    endpoint = "http://open.api.sandbox.ebay.com/shopping"
    
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    
    app_id = config.get("keys", "app_name")
    site_id = config.get("call", "siteid")
    version = config.get("call", "compatibility_level")

    d=dict(appid = app_id, siteid = site_id, version = version)
    
    d.update(user_params)
    
    return requests.get(endpoint, params=d)
