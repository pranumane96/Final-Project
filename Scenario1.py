"""
Simulation of Project Outsourcing Planning for an organization.
The program uses basic Monte Carlo simulation techniques.

Part of IS 590PR Final Project
School of Information Sciences,
University of Illinois, Urbana - Champaign

Scenario 1: Fixed employees - This scenario uses Monte Carlo simulation
to estimate the number of projects and organization can complete
within a year, based on certain existing variables/resources.

The program returns an average estimated value of completed, incomplete
and in-progress projects after a year, along with a visual distribution.
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
    Each simulation, is a year defined by 50 working weeks.
    Number of employees considered are 30.
    Both weeks and number of employees can be changed as per requirement.

    The simulation is run over 500 times and the results are averaged.
    """

    def __init__(self):
        return

    def simulate_year(self):
        # Initialisation of variables
        completed_projects = 0
        incomplete_projects = 0
        total_weeks = 50
        available_employees = 30

        # Queues to store projects in progress and projects in waiting
        projects_in_working = []
        projects_in_queue = []

        for week in range(total_weeks):
            if len(projects_in_working) > 0:  # If some projects are in the progress queue
                for every_project in projects_in_working:
                        every_project[0] = every_project[0] - 1  # Subtract a week from the project duration
                        if every_project[0] == 0:  # If project duration is 0
                            projects_in_working.remove(every_project)
                            completed_projects += 1
                            available_employees += every_project[1]  # Add the free employees to available employees

            if random.randint(0, 1):  # Randomizing the possibility of a project turning up in the week
                new_project = Project()
                new_project = new_project.create()
                self.print_details(new_project)
                projects_in_queue.append(new_project)
                projects_in_queue = self.sort_queue(projects_in_queue)

            if len(projects_in_queue) > 0:  # If project are waiting to be addressed
                for i in projects_in_queue:
                    if available_employees > i[1]:
                        projects_in_queue.remove(i)
                        available_employees -= i[1]
                        projects_in_working.append(i)
                for i in projects_in_queue:  # Handling Project Sensitivity
                    if i[2] == 0:
                        projects_in_queue.remove(i)
                        incomplete_projects += 1
                    else:
                        i[2] -= 1

        incomplete_projects += len(projects_in_queue)  # Projects in queue are considered incomplete
        projects_in_progress = len(projects_in_working)

        return [completed_projects, incomplete_projects, projects_in_progress]

    @staticmethod
    def sort_queue(qlist):
        """
        The function is used to sort projects waiting in queue according to their priority
        :param qlist: Takes the projects in queue list
        :return: Returns a list sorted on the basis of the projects' priorities

        >>> Simulation.sort_queue([[5, 6, 3, 1], [8, 7, 12, 2], [13, 4, 3, 4], [5, 6, 3, 5], [12, 3, 5, 3]])
        [[5, 6, 3, 1], [8, 7, 12, 2], [12, 3, 5, 3], [13, 4, 3, 4], [5, 6, 3, 5]]
        """
        for i in range(1, len(qlist)):
            j = i - 1
            nxt_element = qlist[i]
            while (qlist[j][3] > nxt_element[3]) and (j >= 0):
                qlist[j + 1] = qlist[j]
                j = j - 1
            qlist[j + 1] = nxt_element
        return qlist

    def print_details(self, project):
        print("Simulating project of duration {0} weeks, consisting of {1} team members. It cannot be extended beyond\
 {2} weeks and it has a priority of {3}.".format(project[0], project[1], project[2], project[3]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    summary_df = pd.DataFrame(columns=['Completed', 'Incomplete', 'In Progress'])
    number_of_simulations = 500
    for i in range(number_of_simulations):
        s = Simulation()  # Simulating 500 years
        yearwise_stats = s.simulate_year()
        summary_df = summary_df.append({'Completed': yearwise_stats[0],'Incomplete': yearwise_stats[1], \
                        'In Progress': yearwise_stats[2]}, ignore_index=True)  # Year-wise stats appended to a DataFrame
    print("\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    averages = summary_df.mean()
    print(summary_df)
    print("\nOn an average:\n")
    print(averages)

    # Scatter plot of the performance statistics
    colors = ("green", "red", "yellow")
    x = (summary_df['Completed'], summary_df['Incomplete'], summary_df['In Progress'])

    for x, color in zip(x, colors):
        plt.scatter(x, y=summary_df.index.values, c = color, alpha=0.5)
    plt.title('Project Status over 500 simulations')
    plt.xlabel('Number of projects')
    plt.ylabel('Index values')
    plt.show()