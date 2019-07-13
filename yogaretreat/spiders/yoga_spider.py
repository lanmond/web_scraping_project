

from scrapy import Spider, Request
from yogaretreat.items import YogaretreatItem
import math
import re

class cm_spider(Spider):
	name = 'yoga_spider'
	allowed_urls = ['https://www.bookyogaretreats.com']
	start_urls = ['https://www.bookyogaretreats.com']
	domain = 'https://www.bookyogaretreats.com'

	
	def parse(self, response):

		number_pages = int(math.ceil(7716/12))

		url = 'https://www.bookyogaretreats.com/?page={}'
		results_url = [url.format(x) for x in range(1, number_pages + 1)] # receive all 644 pages
		#info = response.meta['info']

		for url in results_url:
			#yield Request(url=url, callback=self.parse_result_page, meta={'info': info})
			yield Request(url=url, callback=self.parse_result_page)


	def parse_result_page(self, response):
		#info = response.meta['info']
		# detail_urls = response.xpath('//div[@class="cards"]/div/div/div/a/@href').extract() # 12 urls on one page
		#print('number of urls:', len(detail_urls))

		detail_urls = response.xpath('//div[@class="showcards"]')

		for detail_url in detail_urls:
			#print(detail_url)	
			info = detail_url.css('div::attr(data-listing-id)').extract()[0]
			
			final = detail_url.xpath('.//h2[@class="title"]/a/@href').extract()[0]
			yield Request(url=self.domain + final, callback=self.parse_detail_page, meta={'info': info})


	def parse_detail_page(self, response):
		#print(response.url)
		#info = response.meta['info']

		listing_id = response.meta['info']

		star_rating = response.xpath('//div[@class="section ratings right-column full-width-sm"]//div[@class="star-visuals"]/i/@class').extract()
		rating = list(map(lambda L: L.split('-')[-1], star_rating)) 


		title = response.xpath('//div[@class="listing-title"]/h1/text()').extract_first()
		duration = title.split(' ')[0]
		address =  response.xpath('//div[@class="listing-title__location"]/text()').extract_first()
		country = address.split(',')[-1]
		introducing = response.xpath('//div[@class="section listing-overview left-column full-width-sm"]/h2/text()').extract()
		
		expert_tip = response.xpath('//div[@class="section listing-overview left-column full-width-sm"]/div[@class="listing-box listing-box-colorful"]/p/text()').extract_first()
		expert_tip = 'most popular' if str(expert_tip).split(':')[0] == "\nExpert tip" else ' '

		listing_introduction = response.xpath('//div[@class="section listing-overview left-column full-width-sm"]/div[@class="listing-overview__introduction"]/p/text()').extract()[0]
		skill_level = response.xpath('//div[@class="section listing-overview left-column full-width-sm"]/div[@class="listing-description-container"]/ul[2]//li/text()').extract()
		yoga_style = response.xpath('//div[@class="section listing-overview left-column full-width-sm"]/div[@class="listing-description-container"]/ul[3]//li/a/text()').extract()
		instruction_language = response.xpath('//div[@class="listing-overview__notes"]/div/strong/text()').extract()[0]
		transportation = response.xpath('//div[@class="listing-overview__notes"]/div[@class="listing-overview__airport"]/@title').extract()
		# accommodation = response.xpath('//div[@id="accordion"]/div[2]/div/div[4]/p/text()').extract()
		#standard_room = response.xpath('//div[@id="accordion"]/div[2]/div/div[4]/p[2]/text()').extract()
		program = response.xpath('//div[@id="accordion"]/div[3]/div[@class="listing-description-container js-collapsible"]/p/text()').extract()
		daily_schedule = response.xpath('//div[@id="accordion"]/div[3]/div[@class="listing-description-container js-collapsible"]/ul//li/text()').extract()
		#instructors = response.xpath('//div[@id="accordion"]/div[5]//h3/text()').extract()
		#retreat_location = response.xpath('//div[@id="accordion"]/div[6]/div[1]/p/text()').extract()
		#nearby_places = response.xpath('//div[@id="accordion"]/div[6]/div[1]/ul/li//text()').extract()
		#food = response.xpath('//div[@id="accordion"]/div[7]/div[1]/p/text()').extract()
		#what_is_included = response.xpath('//div[@id="accordion"]/div[10]/div[1]/ul/li//text()').extract()
		# airport_code = response.xpath('//div[@id="accordion"]/div[12]//div[@class="airport-code"]/text()').extract()
		airport_name = response.xpath('//div[@id="accordion"]/div[12]//p[@class="airport-name"]/text()').extract()
		airport_distance = response.xpath('//div[@id="accordion"]/div[12]//p[@class="airport-distance"]/text()').extract()
		# arrival_by_air = response.xpath('//div[@id="accordion"]/div[12]/div[1]/div[2]/p/text()').extract()
		#cancellation_policy = response.xpath('//div[@id="accordion"]/div[13]/div/ul/li//text()').extract()



		Item = YogaretreatItem()

		Item['listing_id'] = listing_id
		Item['rating'] = rating
		Item['title'] = title
		Item['duration'] = duration
		Item['address'] = address
		Item['country'] = country
		Item['introducing'] = introducing
		Item['expert_tip'] = expert_tip
		Item['listing_introduction'] = listing_introduction
		Item['skill_level'] = skill_level
		Item['yoga_style'] = yoga_style
		Item['instruction_language'] = instruction_language
		Item['transportation'] = transportation
		#Item['accommodation'] = accommodation
		#Item['standard_room'] = standard_room
		Item['program'] = program
		Item['daily_schedule'] = daily_schedule
		#Item['instructors'] = instructors
		#Item['retreat_location'] = retreat_location
		#Item['nearby_places'] = nearby_places
		#Item['food'] = food
		#Item['what_is_included'] = what_is_included
		#Item['airport_code'] = airport_code
		Item['airport_name'] = airport_name
		Item['airport_distance'] = airport_distance
		#Item['arrival_by_air'] = arrival_by_air
		#Item['cancellation_policy'] = cancellation_policy
		yield Item
	





