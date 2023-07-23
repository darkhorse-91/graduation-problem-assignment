

class GradProbability:

	def __init__(self):
		
		# constructor initialising a dictionary for storing mapping of days : prob
		# { N : probability_to_attend_class} 
		# { N: probability_to_miss_graduation}
		# Can be used for caching/memoization
		
		self.attend_ways_map = {}
		self.miss_ways_map = {}				


	def prob_attend_class(self, n: int) -> int:

		# Method calculates the ways to attend classes over N days
		# Parameter - (N -> int)
		# Return - (Total ways in which can attend classes -> int)

		if n < 4:
			return 2**n

		elif n == 4:
			return 2**n - 1

		else:
			if n not in self.attend_ways_map:
				self.attend_ways_map[n] = self.prob_attend_class(n-4) + self.prob_attend_class(n-3) + self.prob_attend_class(n-2) + self.prob_attend_class(n-1)

			return self.attend_ways_map[n]


	def prob_miss_class(self, n: int) -> int:

		# Method calculates the ways in which the graduation ceremony is missed
		# Parameter - (N -> int)
		# Return - (Ways to miss graduation ceremony -> int)

		if n < 4:
			return 2**(n-1)

		elif n == 4:
			return 2**(n-1)-1

		else:
			if n not in self.miss_ways_map:
				self.miss_ways_map[n] = self.prob_miss_class(n-4) + self.prob_miss_class(n-3) + self.prob_miss_class(n-2) + self.prob_miss_class(n-1)

			return self.miss_ways_map[n]

