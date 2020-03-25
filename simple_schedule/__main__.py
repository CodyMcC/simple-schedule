from time import time, sleep


class Schedule:
	"""
	Example:
		
		timer = Schedule()
		while True:
			if timer.run_action('10_s')
				print('Ran the 10 second task')
				
	"""
	
	def __init__(self):
		self.start_time = time()
		self.elapsed_time = 0
		self.timers = {}

	def run_action(self, interval: str):
		"""
		format: dd_t
			360_s
			12_m
			1_h
			2_d

		"""
		self._add_timer(interval)
		
		self.elapsed_time = time() - self.start_time
		
		if self.timers[interval]['count'] < self.elapsed_time:
			self.timers[interval]['count'] += self.timers[interval]['interval']
			return True
		else:
			return False

	def _add_timer(self, interval):
		
		if interval.lower() not in self.timers:
			self.timers[interval.lower()] = {'count': self._parse_interval(interval),
											'interval': self._parse_interval(interval)}

	@staticmethod
	def _parse_interval(interval: str):
		"""
		format: dd_t
			360_s
			12_m
			1_h
			2_d
		"""
		
		options = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
		
		parse = interval.split('_')
		
		if len(parse) != 2:
			raise ValueError('Must format as value_multiplier. Example: 12_s')
		
		try:
			freq = int(parse[0])
		except ValueError:
			raise ValueError('Example: 12_m')
			
		if parse[1].lower() in options:	
			mul = options[parse[1].lower()]
		else:
			raise ValueError('Multiplier can be: s, m, h, or d')
			
		return freq * mul

		


