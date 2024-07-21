#!/usr/bin/python3
"""user posts"""
from models.base_model import BaseModel


class Post(BaseModel):
	"""post representation"""
	user_id = ""
	media = ""
	text = ""
	likes = ""
	comments = []

	def __init__(self, *args, **kwargs):
		"""initializes post instance"""
		if kwargs is not None:
			if "id" in kwargs.keys():
				for key, value in kwargs.items():
					setattr(self, key, value)
			else:
				super().__init__(self, *args, **kwargs)
				for key, value in kwargs.items():
					setattr(self, key, value)
		else:
			super().__init__(self, *args, **kwargs)