
def get_obj_attr(obj,attributename):
	if hasattr(obj,attributename):
		return getattr(obj,attributename)
	else:
		return None