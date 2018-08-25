# - Coding UTF8 -
#
# Plugin location picker widget and lookups
# based on development by Leonel Camara and updated with some additional options

"""This controller has 2 functiosns:
index: -        simple listing of all locations now with buttons
new_location -  for creating and shortly editing locations
accept_location - route after acceptance
"""

from plugin_location_picker import IS_GEOLOCATION


def index():
    grid = SQLFORM.grid(db.locn, formstyle=SQLFORM.formstyles.bootstrap3_inline)
    return locals()


def new_location():

    stdclass = "btn btn-primary btn-xs btn-group-xs"
    # This allows creation and editing of a locations by their owner
    fields = ['location_name', 'description', 'address1', 'address2', 'address3', 'address4', 'addrcode',
              'continent', 'country', 'subdivision', 'coord']

    buttons = [TAG.button('Submit', _type="submit"),
               TAG.INPUT(_TYPE='BUTTON', _id="geocode", _class=stdclass, _onclick="", _VALUE="Get Co-ordinates"),
               TAG.INPUT(_TYPE='BUTTON', _id="rev_geocode", _class=stdclass, _onclick="", _VALUE="Get Address")]

    locationid = request.args(0, default=None)
    if locationid is not None:
        record = db.locn(locationid)
        form = SQLFORM(db.locn, record, fields=fields)
    else:
        form = SQLFORM(db.locn, fields=fields, buttons=buttons)

    if form.validate():
        if locationid:
            if form.deleted:
                db(db.location.id == locationid).delete()
                response.flash = 'Location deleted'
                redirect(URL('location', 'index'))
            else:
                record.update_record(**dict(form.vars))
                response.flash = 'Location updated'
                redirect(URL('location', 'index'))
        else:
            # write values into separate fields for indexed bb queries on non spatial databases
            form.vars.geoy, form.vars.geox = IS_GEOLOCATION.parse_geopoint(form.vars.coord)
            form.vars.id = db.locn.insert(**dict(form.vars))
            session.flash = 'Location Created'
            redirect(URL('accept_location', args=[form.vars.id]))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def accept_location():
    response.flash = "Location Created"
    return locals()
