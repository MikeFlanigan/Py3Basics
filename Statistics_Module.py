import statistics

example_list = [3, 4, 5, 5,63, 2, 1, 3,4]

x = statistics.mean(example_list)
print(x)

x = statistics.stdev(example_list)
print('stddev',x)
