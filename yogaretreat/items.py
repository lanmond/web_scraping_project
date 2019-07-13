# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YogaretreatItem(scrapy.Item):

	# define the fields for your item here like:
	# name = scrapy.Field()

	listing_id = scrapy.Field()
	rating = scrapy.Field()
	title = scrapy.Field()
	duration = scrapy.Field()
	address = scrapy.Field()
	country = scrapy.Field()
	introducing = scrapy.Field()
	expert_tip = scrapy.Field()
	listing_introduction = scrapy.Field()
	skill_level = scrapy.Field()
	yoga_style = scrapy.Field()
	instruction_language = scrapy.Field()
	transportation = scrapy.Field()
	#accommodation = scrapy.Field()
	#standard_room = scrapy.Field()
	program = scrapy.Field()
	daily_schedule = scrapy.Field()
	#instructors = scrapy.Field()
	#retreat_location = scrapy.Field()
	#nearby_places = scrapy.Field()
	#food = scrapy.Field()
	#what_is_included = scrapy.Field()
	#airport_code = scrapy.Field()
	airport_name = scrapy.Field()
	airport_distance = scrapy.Field()
	#arrival_by_air = scrapy.Field()
	#cancellation_policy = scrapy.Field()