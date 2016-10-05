import urllib.parse as ulp
import datetime


def modify_url_date(url, new_date, date_parameter="CloseDate"):
    """modify the SSRS URL to replace the data parameter with the new date"""
    # parse URL for query string parts
    o = ulp.urlparse(url)
    query_parts = ulp.parse_qsl(o.query, True)

    # search for date parameter in query string
    for i in range(0,len(query_parts)):
        if query_parts[i][0]==date_parameter:
            query_parts.remove(query_parts[i])

    # reconstruct query string with date removed
    date_string = str(new_date)
    query_string=ulp.urlencode(query_parts, True)

    # The report name will be a query string parameter with empty string value.  remove equal sign.
    query_string = query_string.replace("=&rs","&rs",1) 
    full_path = o.path+"/?"+query_string+"&"+date_parameter+"="+date_string
    
    # get a new URL from parts, adding query string as part of path
    o_new = ulp.ParseResult(o.scheme, o.netloc, full_path 
                            , o.params, '', o.fragment)
    return o_new.geturl()


    


