not_empty = IS_NOT_EMPTY()

from plugin_location_picker import IS_GEOLOCATION, location_widget
from gluon.dal import DAL, Field, geoPoint, geoLine, geoPolygon

db.define_table('locn',
                Field('location_name', label='Location Name', requires=[not_empty,
                                                                        IS_NOT_IN_DB(db, 'locn.location_name')]),
                Field('address1', label='Address 1', writable=False, readable=False),
                Field('address2', label='Address 2', writable=False, readable=False),
                Field('address3', label='Address 3', writable=False, readable=False),
                Field('address4', label='Address 4', writable=False, readable=False),
                Field('addrcode', label='Postal Code', writable=False, readable=False),
                Field('addrurl', label='Location Website'),
                Field('continent', default='Unspecified', label='Continent'),
                Field('country', default='Unspecified', label='Country'),
                Field('subdivision', default='Unspecified', label='Subdivision'),
                Field('geox', 'double', default=0.0, label='Longitude', writable=False, readable=False),
                Field('geoy', 'double', default=0.0, label='Latitude', writable=False, readable=False),
                Field('coord', label='Lat/Longitude'),
                Field('description', 'text'),
                Field('locn_shared', 'boolean', label='Shared', default=False,
                      comment='Allows other users to link events'),
                  format='%(location_name)s')
                  
db.locn.coord.requires = IS_GEOLOCATION()
db.locn.coord.widget = location_widget()