"""
Simulation of Project Outsourcing Planning for an organization.
The program uses basic Monte Carlo simulation techniques.

Part of IS 590PR Final Project
School of Information Sciences,
University of Illinois, Urbana - Champaign

Scenario 2: Fixed projects - If a company wants to estimate the
human resources it will need for a year, this scenario is useful.
We have used Monte Carlo simulation to understand the requirement
of human resources in order to achieve a company's goal of
completing 50 (variable) projects in a year.

The program returns average, minimum and maximum number of
employees required, and plots a scatter plot of the distribution.

"""

import random
import pandas as pd
import matplotlib.pyplot as plt


class Project:
    """
     A project is an undertaking by the organization, characterised by
    certain variables defined by the functions in the class: project duration,
    team size, sensitivity and priority.

    During each simulation/year, a Project Object is created multiple times,
    with each object having various characteristics defined by randomizing
    it's properties.
    """
    def __init__(self):
        return

    def create(self):
        project_duration = self.project_duration()
        team_size = self.team()
        proj_sensitivity = self.sensitivity()
        priority = self.priority()
        return list([project_duration, team_size, proj_sensitivity, priority])

    def project_duration(self):
        # Random distribution within 12-16 weeks
        return random.randint(12, 16)

    def team(self):
        # Random distribution within 3-7 members
        return random.randint(3, 7)

    def sensitivity(self):
        # Random distribution within 2-12 weeks
        return random.randint(2, 12)

    def priority(self):
        # Random distribution within 1-5
        return random.randint(1, 5)


class Simulation:
    """
    Simulating every year
    """
    def __init__(self):
        return

    def simulate_year(self, completed_projects, last_year_incomplete):
        total_weeks = 50  # 50 Working weeks in a year
        projects_in_working = last_year_incomplete  # Handling incomplete projects from previous year
        goal = to_be_completed_projects
        employee_per_week = pd.DataFrame()  # A DataFrame to store number of employees required each week
        print("\n\n-------------------------------------------------------------------------------------------------\
--------------------------------------------------------------------\n")
        for week in range(total_weeks):
            required_employees = 0
            if len(projects_in_working) > 0:
                for every in projects_in_working:
                        every[0] = every[0] - 1
                        if every[0] == 0:
                            projects_in_working.remove(every)

            if random.randint(0, 1) and goal != 0:  # Randomizing the possibility of a project turning up in the week
                new_project = Project()
                new_project = new_project.create()
                projects_in_working.append(new_project)
                projects_in_working = self.sort_queue(projects_in_working)
                goal -= 1

            for each_project in projects_in_working:
                required_employees += each_project[1]
            print("Required employees for week {0} is {1}".format(week + 1, required_employees))
            employee_per_week = employee_per_week.append({'Requirement': required_employees}, ignore_index=True)
        return [employee_per_week.loc[:, "Requirement"].mean(), employee_per_week.loc[:, "Requirement"].min(), \
                employee_per_week.loc[:, "Requirement"].max(), projects_in_working]

    @staticmethod
    def sort_queue(qlist):
        """
        The function is used to sort projects waiting in queue according to their priority
        :param qlist: Takes the projects in queue list
        :return: Returns a list sorted on the basis of the projects' priorities
        """
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
    to_be_completed_projects = 40
    incomplete = []
    for i in range(number_of_simulations):
        s = Simulation()
        yearwise_stats = s.simulate_year(to_be_completed_projects, incomplete)
        summary_df = summary_df.append({'Average_#_of_Employees': yearwise_stats[0],'Minimum_#_of_Employees': yearwise_stats[1], \
                                        'Maximum_#_of_Employees': yearwise_stats[2]}, ignore_index=True)
        incomplete = yearwise_stats[3]
    print("\n\n--------------------------------------------------------------------------------------------------------\
------------------------------------------------------------\n")
    averages = summary_df.mean().round(0)
    print("\nOn an average:\n")
    print(averages)

    # Scatter plot of the performance statistics
    colors = ("green", "red", "yellow")
    x = (summary_df['Average_#_of_Employees'], summary_df['Minimum_#_of_Employees'], summary_df['Maximum_#_of_Employees'])

    for x, color in zip(x, colors):
        plt.scatter(x, y=summary_df.index.values, c = color, alpha=0.5)
    plt.title('Number of employees required to complete 40 projects in a year')
    plt.xlabel('Number of employees required per week')
    plt.ylabel('Index values')
    plt.show()


