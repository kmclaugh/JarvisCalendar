import urllib.request


school_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/2Xl8TQJNL2mzXztBUxGMlQ9HZuuo3Rq71jwHIHHiFTR-_05oxQ_gJGeoqoc5I2DeaFM3Z9lLyzDEKdPYxmTptutVpaADSSCxXtDxCUMkLe4",'school']
personal_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/BtBadAsXJT_jVD4d9g_O17zr1vgWy3qL_cMDTnerwXhbNTBsduel4dRyunihLvvy16OvivPh08E5bOB97SL9Ewq4TEbEhJnlMwyfkW4AylU",'personal']
work_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/7qYvm9BTDfafpsEqLtGgw0mV5OAif8lnNNYTSgu8DOdqiRu4S_dnmNnPQSyBQmRU",'work']
travel_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/yap8v_4luGdNlTX8qDR_iUcStJ1X4cCSBgfqr9m5xNzjRQ8QvOkqoMnDPi1R3Cj61CEuB3eJ8gFHDmZJDYWyorZHstwa9onzeaVnsV6uBG0",'travel']
business_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/FDlClb_iwhqiFjWYK2K_DEB-VHZ_cQ80CiuaDIXXtGI8mUCmF5l41x5AWBB-05XeMefFKnqp4tQedfk5rJ64i4bhk9XA_Ybvyz5dVn0nr3k",'business']
meeting_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/W5yXm3gW-QuwVf2Ud2vaMIZgmshwg0C1ATUuHtgZPo9Cjh6-OGyn5q4GSfUdmVcMnHE_l_Pxq0kaOVxx5lxlz8aYGgm74lbBViFzL2kcaaE",'meeting']
important_url = ["http://p08-calendarws.icloud.com/ca/subscribe/1/i7N7eimk0IDP0uuXt7h1bjn1ZGqGIVCrJIQEgXDDuRScdNQ554rUnbOAl4qIMiqwZGllwIAdKsGKq4H6tR3LRZm4J3kiMOvrakS94wG8cCg",'imporant']

url_list = [school_url,personal_url,work_url,travel_url,business_url,meeting_url,important_url]

def download(file_name, file_mode, base_url):
    """ download files from Web sites"""
    # generate url(s) of desired file(s) to download
    url = base_url
    # open the url
    f = urllib.request.urlopen(url)
    print("Downloading ---> ", url)
    with open(file_name, "w" + file_mode) as outfile:
        outfile.write(f.read())

## Download the URLs in the list
file_names = []
for url in url_list:
    file_name = "/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/{}.ics".format(url[1])
    download(file_name,"b",url[0])
    file_names.append(file_name)

print(file_names)
