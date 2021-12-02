from parse import read_input_file, write_output_file
import os
import math
#items in task jobs (Deadline, Duration, Profit)
EOD = 1440
def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    print(tasks[0])
    tasks.sort(key = lambda x: x[0])
    dp = [[0 for _ in range(len(tasks))] for _ in range(EOD)]
    for i in range(1, EOD + 1):
        for t in tasks:
            deadline, duration, profit = t[0], t[1], t[2]
            t_latest = min(deadline, EOD) - duration
            if t_latest < 0:
                dp[i][t] = dp[i-1][t]
            else:
                dp[i][t] = max(dp[i-1][t], profit + dp[i-1][t_latest])
                
    return dp[-1][-1]

def profitDecay(p, s):
    return p*math.e^(-0.017*s)

def main():
    if __name__ == '__main__':
        for input_path in os.listdir('inputs/small/'):
            print(input_path)
            output_path = 'outputs/' + input_path[:-3] + '.out'
            tasks = read_input_file('inputs/small/' + input_path)
            output = solve(tasks)
            write_output_file(output_path, output)

main()

# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)
