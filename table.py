class Table:
	def __getattr__(self, attr):
		return self.__dict__.get(attr, None)
	def __setattr__(self, attr, value):
		self.__dict__[attr] = value
	def __getitem__(self, key):
		return self.__dict__.get(key, None)
	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __delitem__(self, key):
		del self.__dict__[key]
	def __contains__(self, value):
		return value in self.__dict__
	def __iter__(self):
		return iter(self.__dict__)
	def __eq__(self, other):
		return type(self) == type(other) and self.__dict__ == other.__dict__
