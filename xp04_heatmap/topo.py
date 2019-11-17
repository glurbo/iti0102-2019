"""
Topography module.
Helps to read topography related data.

"""
import urllib.request
import json


def read_web(url):
    """
    Read url from the web and return contents.

    Use urllib.request to read the contents of the web page.

    :param url: URL to be read
    :return: contents of the web page (string)
    """
    f = urllib.request.urlopen(url)
    contents = f.read()
    return contents


def read_json_from_web(min_lat, max_lat, lat_step, min_lng, max_lng, lng_step):
    """
    Read topography data from web and return json string.

    See the web page:
    http://coastwatch.pfeg.noaa.gov/erddap/griddap/usgsCeSrtm30v6.html

    You should use the parameters to construct url, then use
    read_web function (which you should also implement) to get the contents of the web page.

    Note that the given web page should not be used to get the contents.
    Instead, you can play with this web site to get different data and
    see how downloading data works.
    If you insert some numbers into the latitude and longitude fields,
    make sure "topo" option is checked, then choose file type: json
    and click "Just generate the URL".
    The generated URL is what you should use in here.
    See how different values on the form change the URL,
    then use parameters of this function to generate the required URL.

    Note that there are a lot of data there. If you choose large dimensions,
    the amount of data can be several giga bytes. It's wise to start with small areas.
    For example, Tallinn coordinates are:
    59.438274, 24.754352


    :param min_lat: minimum latitude
    :param max_lat: maximum latitude
    :param lat_step: step for latitude (see stride in the web page)
    :param min_lng: minimum longitude
    :param max_lng: maximum longitude
    :param lng_step: step for longitude (see stride)
    :return: json string with the results
    """
    json_string = read_web(f"https://coastwatch.pfeg.noaa.gov/erddap/griddap/usgsCeSrtm30v6.json?topo"
                           f"[({min_lat}):{lat_step}:({max_lat})][({min_lng}):{lng_step}:({max_lng})]")
    return json_string


def read_json_from_file(filename):
    """
    Read file to get topography data.

    The function should just return the contents of the file.
    :param filename: filename to be opened
    :return: json string (the contents). None if the file cannot be read.
    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def get_topo_data_from_string(data_string):
    """
    Return list of topography data (latitude, longitude, altitude in meters) from input string.

    The input string can be from either web or file.
    :param data_string: input string (json format)
    :return: list of lists
    """
    data = json.loads(data_string)
    return data["table"]["rows"]

    # return [[61.0, 24.0, 136],
    #  [61.0, 24.083333333333343, 153],
    #  [61.0, 24.166666666666657, 125]]


if __name__ == '__main__':
    """print(read_web(" http://coastwatch.pfeg.noaa.gov/erddap/griddap/usgsCeSrtm30v6.html"))"""
    # print(read_json_from_web(59.481375, 59.3784, 1, 24.618599, 24.946075, 1))
    # print(read_json_from_file("Tallinn.json"))
    print(get_topo_data_from_string(read_json_from_web(59.481375, 59.3784, 1, 24.618599, 24.946075, 1)))
