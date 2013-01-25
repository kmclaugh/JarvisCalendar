from icalendar import Calendar, Event
import vobject
import datetime

def get_class_members(klass):
    ret = dir(klass)
    if hasattr(klass,'__bases__'):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret

def uniq( seq ):
    """ the 'set()' way ( use dict when there's no set ) """
    return list(set(seq))

def get_object_attrs( obj ):
    # code borrowed from the rlcompleter module ( see the code for Completer::attr_matches() )
    ret = dir( obj )
    ## if "__builtins__" in ret:
    ##    ret.remove("__builtins__")
    
    if hasattr( obj, '__class__'):
        ret.append('__class__')
        ret.extend( get_class_members(obj.__class__) )
        
        ret = uniq( ret )
    
    return(ret)

file_location = "/Users/kevin/Desktop/School_Test.ics"

cal = open(file_location,'rb').read()
cal = vobject.readOne(cal)
for ev in cal.vevent_list:
    ev.prettyPrint()



#for component in cal.walk():
#    if component.name == "VEVENT":
#        date = component.get('dtstart:date-time')
#        print(date)
