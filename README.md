# w2p_location_widget
This will extend the existing gis location picker widget developed by Leonel Camara to support client side address lookup and geolocation.  The original version of this project is listed at the following link. 

https://groups.google.com/forum/#!searchin/web2py/map$20picker%7Csort:relevance/web2py/bCGmGAMWhG0/FPEaxH4_pqAJ

and some of the jquery stuff may have originated at:

http://miloss.github.io/jquery-geolocation-edit/  which appears to have some address lookup functionality which may be used.

The intention is that this will broadly do three additional things:
1 Provide additional form buttons to populate latitude and longitude from an address or populate address from lat/long
2 Provide support for non-geographical databases - it seems that separate latitude and longitude fields in the database will provide an acceptable solution for point based proximity on all databases without spatial indexes by means of the standard bounding box approach at the database level and further filtering of results to get items within a set radius
3 Optionally use html5 geolocation functionality to set initial location on a form


