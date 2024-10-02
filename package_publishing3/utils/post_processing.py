from .. import module1

def what(modelobj):
    if modelobj.add:
        return "add"
    elif modelobj.sub:
        return "sub"
    else:
        return "neither"
