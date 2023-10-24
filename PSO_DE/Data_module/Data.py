class Data:
    def __init__(self, best_result, avg_result, standard_deviation, number_of_iterations) -> None:
      self.best_result = best_result
      self.avg_result = avg_result
      self.standard_deviation = standard_deviation
      self.number_of_iterations = number_of_iterations
      self.success_rate = None