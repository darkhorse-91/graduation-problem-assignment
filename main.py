# Main file for entrypoint
# and calling other source file

from src.prob_calculation import GradProbability


if __name__ == "__main__":

	N = int(input("Please enter the number of days for probability calculation.\nTo stop calculating, please enter -1 \n"))
	while N != -1:
		grad_prob_instance = GradProbability()
		ways_to_attend = grad_prob_instance.prob_attend_class(N)
		ways_to_miss = grad_prob_instance.prob_miss_class(N)
		final_prob = "{}/{}".format(ways_to_miss, ways_to_attend)
		print(final_prob)
		N = int(input("Please enter the number of days for probability calculation.\nTo stop calculating, please enter -1 \n"))
