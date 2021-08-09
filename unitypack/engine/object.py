def field(f, cast=None, **kwargs):
	def _inner(self):
		if "default" in kwargs:
			ret = self._obj.get(f, kwargs["default"])
		else:
			ret = self._obj[f]
		if cast:
			try:
				ret = cast(ret)
			except ValueError:
				print("The value "+str(ret)+" is not present in the enum/cast "+str(cast)+". This usually means you're dealing with an unknown file compression type.")
				raise ValueError
		return ret
	return property(_inner)


class Object:
	def __init__(self, data=None):
		if data is None:
			data = {}
		self._obj = data

	def __repr__(self):
		return "<%s %s>" % (self.__class__.__name__, self.name)

	def __str__(self):
		return self.name

	name = field("m_Name", default="")


class GameObject(Object):
	active = field("m_IsActive")
	component = field("m_Component")
	layer = field("m_Layer")
	tag = field("m_Tag")
