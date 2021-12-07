from parse import read_input_file, write_output_file
import os
import math

EOD = 1440
def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    tasks = [(tasks[i].task_id, tasks[i].deadline, tasks[i].duration, tasks[i].perfect_benefit) for i in range(len(tasks))]
    tasks.sort(key = lambda x: x[3] / x[2], reverse = True)
    scheduled = []
    curTime = 0
    profit = 0
    for id, deadline, duration, profit in tasks:
        if curTime + duration > EOD:
            continue
        scheduled.append(id)
        curTime += duration
        if curTime > deadline:
            profit += profitDecay(profit, curTime - deadline)
        else:
            profit += profit
    print("Profit is : " + str(profit))
    return scheduled
    

def profitDecay(p, s):
    return p*math.e**(-0.017*s)

def main():
    if __name__ == '__main__':
        for size in os.listdir('inputs/'):
            if size not in ['small', 'medium', 'large']:
                continue
            for input_file in os.listdir('inputs/{}/'.format(size)):
                if size not in input_file:
                    continue
                input_path = 'inputs/{}/{}'.format(size, input_file)
                output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
                print(input_path, output_path)
                tasks = read_input_file(input_path)
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



# dp_profit = [[0 for _ in range(EOD)] for _ in range(len(tasks))]
#     scheduledTasks = []
#     scheduled = set()
#     for t in range(EOD):
#         for i in range(len(tasks)):
#             task = tasks[i]
#             id, deadline, duration, profit = task[0], task[1], task[2], task[3]
#             if id in scheduled:
#                 continue
#             t_latest = min(deadline, t) - duration
#             if t_latest < 0:
#                 dp_profit[i][t] = dp_profit[i-1][t]
#             else:
#                 if dp_profit[i-1][t] > profit + dp_profit[i-1][t_latest]:
#                     dp_profit[i][t] = dp_profit[i-1][t]
#                 else:
#                     dp_profit[i][t] = profit + dp_profit[i-1][t_latest]
#                     scheduledTasks.append(id)
#                     scheduled.add(id)
#     return scheduledTasks