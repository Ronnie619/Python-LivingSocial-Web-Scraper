from scrapy.item import Item, Field

class LivingSocialDeal(Item):
	"""Livingsocial container (dictionary-like object) for scraped data"""
	title = Field()
	description = Field()
	link = Field()
	category = Field()
	location = Field()
	original_price = Field()
	price = Field()
	"""Assigned to Field() because that is how to specify metadata to scrapy"""
	"""The scrapy Item class behaves similiar to Python's dict when getting keys and vals"""
