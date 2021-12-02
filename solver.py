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
    tasks = [(tasks[i].task_id, tasks[i].deadline, tasks[i].duration, tasks[i].perfect_benefit) for i in range(len(tasks))]
    tasks.sort(key = lambda x: x[0])
    tasks = [0] + tasks
    dp = [[0 for _ in range(EOD)] for _ in range(len(tasks))]
    scheduledTasks = []
    scheduled = set()
    for t in range(1, EOD):
        for i in range(1, len(tasks)):
            task = tasks[i]
            id, deadline, duration, profit = task[0], task[1], task[2], task[3]
            if id in scheduled:
                continue
            t_latest = min(deadline, t) - duration
            if t_latest < 0:
                dp[i][t] = dp[i-1][t]
            else:
                if dp[i-1][t] > profit + dp[i-1][t_latest]:
                    dp[i][t] = dp[i-1][t]
                else:
                    dp[i][t] = profit + dp[i-1][t_latest]
                    scheduledTasks.append(id)
                    scheduled.add(id)
    return scheduledTasks

def profitDecay(p, s):
    return p*math.e^(-0.017*s)

def main():
    if __name__ == '__main__':
        for input_path in os.listdir('inputs/large/'):
            print(input_path)
            output_path = 'outputs/large/' + input_path[:-3] + '.out'
            tasks = read_input_file('inputs/large/' + input_path)
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
