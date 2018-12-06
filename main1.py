import random
import pandas as pd

class Project:
    def __init__(self):
        return

    def create(self):
        project_duration = self.project_duration()
        team_size = self.team()
        proj_sensitivity = self.sensitivity()
        priority = self.priority()
        return list([project_duration, team_size, proj_sensitivity, priority])

    def project_duration(self):
        duration = random.randint(12, 16)
        return duration

    def team(self):
        team_size = random.randint(3, 7)
        return team_size

    def sensitivity(self):
        proj_sens = random.randint(2, 13)
        return proj_sens

    def priority(self):
        proj_priority = random.randint(1, 5)
        return proj_priority

class Simulation:

    def __init__(self):
        return

    def simulate_year(self):
        completed_projects = 0
        incomplete_projects = 0
        total_weeks = 50
        available_employees = 50
        projects_in_working = []
        projects_in_queue = []

        for week in range(total_weeks):
            if len(projects_in_working) > 0:
                for every in projects_in_working:
                        every[0] = every[0] - 1
                        if every[0] == 0:
                            projects_in_working.remove(every)
                            completed_projects += 1

            if random.randint(0, 1):
                new_project = Project()
                new_project = new_project.create()
                self.print_details(new_project)
                projects_in_queue.append(new_project)
                projects_in_queue = self.sort_queue(projects_in_queue)

            if len(projects_in_queue) > 0:
                for i in projects_in_queue:
                    if available_employees > i[1]:
                        projects_in_queue.remove(i)
                        available_employees -= i[1]
                        projects_in_working.append(i)
                for i in projects_in_queue:
                    if i[2] == 0:
                        projects_in_queue.remove(i)
                        incomplete_projects += 1
                    else:
                        i[2] -= 1

        incomplete_projects = incomplete_projects + len(projects_in_queue)
        projects_in_progress = len(projects_in_working)

        return [completed_projects, incomplete_projects, projects_in_progress]

    def sort_queue(self, qlist):
        for i in range(1, len(qlist)):
            j = i - 1
            nxt_element = qlist[i]
            while (qlist[j][3] > nxt_element[3]) and (j >= 0):
                qlist[j + 1] = qlist[j]
                j = j - 1
            qlist[j + 1] = nxt_element
        return qlist

    def print_details(self, project):
        print("Simulating project of duration {0} weeks, consisting of {1} team members \
              , which cannot be extended beyond {2} weeks, as it has a priority of {3}".format(project[0], project[1],\
                                                                                          project[2], project[3]))


if __name__ == '__main__':
    summary_df = pd.DataFrame(columns=['Completed', 'Incomplete', 'In Progress'])
    number_of_simulations = 10
    for i in range(number_of_simulations):
        s = Simulation()
        yearwise_stats = s.simulate_year()
        summary_df = summary_df.append({'Completed': yearwise_stats[0],'Incomplete': yearwise_stats[1], \
                        'In Progress': yearwise_stats[2]}, ignore_index=True)

        averages = summary_df.mean(axis = 0)

    print(summary_df)
    print(averages)