#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sys import version_info

if version_info.major == 3:
    import urllib.request, urllib.parse
elif version_info.major == 2:
    import urllib
    import urllib2
    
import json, ast

class simplehttp():
    
    def __init__(self):
        pass
    
    # get method
    def get_json( url, params={} ): # params is optional
        
        if version_info.major == 3:
            url_values = urllib.parse.urlencode(params) # convert params's dictionaries into query strings

            # add query to url
            if '?' in url:
                full_url = url + '&' +  url_values
            else:
                full_url = url + '?' +  url_values

            req = urllib.request.Request(full_url) # send URL request

            # use 'with' to automatically create, clean and recover resources
            with urllib.request.urlopen(req) as response: # open the URL, which can be a string or a Request object
                response_page = response.read() # read the response
                data = json.loads(response_page) # convert to json formate

            # assert chacking
            if '?' not in url:
                assert data['args'] == {}
            else:
                assert_data = {}
                split_url = url.split('?', 1 )
                for i in range(1, len(split_url)):
                    split_key_value = split_url[i].split('=', 1)
                    assert_data[ split_key_value[0] ] = split_key_value[1]
                assert_data = simplehttp.merge_two_dicts(assert_data, params)

                assert data['args'] == assert_data
            
        elif version_info.major == 2:
            url_values = urllib.urlencode(params) # convert params's dictionaries into query strings
        
            # add query to url
            if '?' in str(url):
                full_url = str(url) + '&' +  url_values
            else:
                full_url = str(url) + '?' +  url_values

            req = urllib2.Request(full_url) # send URL request

            # use 'with' to automatically create, clean and recover resources
            with urllib2.urlopen(req) as response: # open the URL, which can be a string or a Request object
                response_page = response.read() # read the response
                data = json.loads(response_page) # convert to json formate

            # assert chacking
            if '?' not in str(url):
                assert data['args'] == {}
            else:
                assert_data = {}
                split_url = url.split('?', 1 )
                for i in range(1, len(split_url)):
                    split_key_value = split_url[i].split('=', 1)
                    assert_data[ split_key_value[0] ] = split_key_value[1]
                assert_data = simplehttp.merge_two_dicts(assert_data, params)

                assert data['args'] == assert_data
        
        print("HTTP status code: ", response.getcode()) # print HTTP status code
        print("Query parameter: ", data['args']) # print specific column's value
        print("URL after requesting: ", response.url) # print url
        
    # post method    
    def post_json( url, params={}, pass_data={} ): # params and pass_data are optional
        
        if version_info.major == 3:
            url_values = urllib.parse.urlencode(params) # convert param's dictionaries into query strings

            # add query to url
            if '?' in url:
                full_url = url + '&' +  url_values
            else:
                full_url = url + '?' +  url_values

            process_data = urllib.parse.urlencode(pass_data) # convert pass_data's dictionaries into query strings
            process_data = process_data.encode('ascii') # encode into Ascii

            req = urllib.request.Request(full_url, process_data) # send URL request with data to be sent to the server

            # use 'with' to automatically create, clean and recover resources
            with urllib.request.urlopen(req) as response:
                response_page = response.read() # read the response
                data = json.loads(response_page) # convert to json formate

            # assert chacking
            assert data['args'] == params
            assert data['form'] == ast.literal_eval(json.dumps(pass_data)) # remove u chars from the dictionary
        
        elif version_info.major == 2:
            url_values = urllib.urlencode(params) # convert param's dictionaries into query strings

            # add query to url
            if '?' in str(url):
                full_url = str(url) + '&' +  url_values
            else:
                full_url = str(url) + '?' +  url_values

            process_data = urlliburlencode(pass_data) # convert pass_data's dictionaries into query strings
            process_data = process_data.encode('ascii') # encode into Ascii

            req = urllib2.Request(full_url, process_data) # send URL request with data to be sent to the server

            # use 'with' to automatically create, clean and recover resources
            with urllib2.urlopen(req) as response:
                response_page = response.read() # read the response
                data = json.loads(response_page) # convert to json formate

            # assert chacking
            assert data['args'] == params
            assert data['form'] == ast.literal_eval(json.dumps(pass_data)) # remove u chars from the dictionary
    
        print("HTTP status code: ", response.getcode()) # print HTTP status code
        print("Query parameter: ", data['args']) # print specific column's value
        print("Posted data:", data['form']) # print posted data's value
        print("URL after requesting: ", response.url) # print url
    
    
    # merge to dictionaries(for assert checking)
    def merge_two_dicts(x, y):
        merge_result = x.copy()   
        merge_result.update(y)  
        
        return merge_result


# In[ ]:




