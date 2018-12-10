import random
import pandas as pd
import matplotlib.pyplot as plt


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
        proj_sens = random.randint(2, 12)
        return proj_sens

    def priority(self):
        proj_priority = random.randint(1, 5)
        return proj_priority

class Simulation:

    def __init__(self):
        return

    def simulate_year(self, completed_projects):
        total_weeks = 50
        projects_in_working = []
        goal = completed_projects
        employee_per_week = pd.DataFrame()
        print("\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for week in range(total_weeks):
            required_employees = 0
            if len(projects_in_working) > 0:
                for every in projects_in_working:
                        every[0] = every[0] - 1
                        if every[0] == 0:
                            projects_in_working.remove(every)

            if random.randint(0, 1) and goal != 0:
                new_project = Project()
                new_project = new_project.create()
                projects_in_working.append(new_project)
                projects_in_working = self.sort_queue(projects_in_working)
                goal -= 1

            for each in projects_in_working:
                required_employees += each[1]
            print("Required employees for week {0} is {1}".format(week + 1 , required_employees))
            employee_per_week = employee_per_week.append({'Requirement': required_employees}, ignore_index=True)
        return [employee_per_week.loc[:, "Requirement"].mean(), employee_per_week.loc[:, "Requirement"].min()\
            ,employee_per_week.loc[:, "Requirement"].max()]


    def sort_queue(self, qlist):
        for i in range(1, len(qlist)):
            j = i - 1
            nxt_element = qlist[i]
            while (qlist[j][3] > nxt_element[3]) and (j >= 0):
                qlist[j + 1] = qlist[j]
                j = j - 1
            qlist[j + 1] = nxt_element
        return qlist


if __name__ == '__main__':
    summary_df = pd.DataFrame()
    number_of_simulations = 100
    completed_projects = 20
    for i in range(number_of_simulations):
        s = Simulation()
        yearwise_stats = s.simulate_year(completed_projects)
        summary_df = summary_df.append({'Average_Team': yearwise_stats[0],'Minimum_Team': yearwise_stats[1],
                                        'Max_Team': yearwise_stats[2]}, ignore_index=True)
    print("\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Year-wise statistics look like:")
    averages = summary_df.mean(axis = 0)
    print("\nOn an average:\n")
    print(averages)

    colors = ("green", "red", "yellow")
    x = (summary_df['Average_Team'], summary_df['Minimum_Team'], summary_df['Max_Team'])

    for x, color in zip(x, colors):
        plt.scatter(x, y=summary_df.index.values, c = color, alpha=0.5)
    plt.title('Number of employees required to complete 20 projects in a year')
    plt.xlabel('Number of employees required per week')
    plt.ylabel('Index values')
    plt.show()


