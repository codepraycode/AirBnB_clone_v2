

def generateObjId(obj):
    """Generate Id for object in Storage

    key =  object_class_name +  "." + object_id
    Args:
        obj (any): object that is to be save

    Returns:
        str: generated id
    """

    # return str(obj.__class__.__name__) + "." + str(obj.id)
    return "{}.{}".format(type(obj).__name__, obj.id)
