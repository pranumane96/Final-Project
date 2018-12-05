import random

class Project:
    def __init__(self):
        project_duration = self.project_duration()
        team_size = self.team()
        proj_sensitivity = self.sensitivity()
        priority = self.priority()
        return list(project_duration, team_size, proj_sensitivity, priority)

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
        proj_priority = random.randint(1, 6)
        return proj_priority

class Simulation:

    def __init__(self):
        self.simulate_a_year()
        return

    def simulate_a_year(self):
        completed_projects = 0
        incomplete_projects = 0
        projects_in_progress = 0
        total_weeks = 50
        available_employees = 30
        projects_in_working = []
        projects_in_queue = []

        for week in range(total_weeks):
            if len(projects_in_working >0):
                for every in projects_in_working:
                        every[0] = every[0] - 1
                        if every[0] == 0:
                            projects_in_working.remove(every)
                            completed_projects += 1

            if random.randint(0, 2):
                new_project = Project()
                projects_in_queue.append(new_project)
                projects_in_queue = Simulation.sort_queue(projects_in_queue)

            if len(projects_in_queue)>0:
                flag = 1
                while flag:
                    for i in projects_in_queue:
                        if available_employees > i[1]:
                            projects_in_queue.remove(i)
                            available_employees -= i[1]
                            projects_in_working.append(i)
                        if available_employees < 3:
                            flag = 0
                            break
                for i in projects_in_queue:
                    if i[2] == 0:
                        projects_in_queue.remove(i)
                        incomplete_projects +=1
                    else:
                        i[2] -= 1

    def sort_queue(self,qlist):
        for i in range(1, len(qlist)):
            j = i - 1
            nxt_element = qlist[i]
            while (qlist[j][3] > nxt_element[3]) and (j >= 0):
                qlist[j + 1] = qlist[j]
                j = j - 1
            qlist[j + 1] = nxt_element
        return qlist

    def check_availability(self):
        return bool


if __name__ == '__main__':
    a_list = []
    number_of_simulations = 100
    for i in range(number_of_simulations):
        a = Simulation()
        a_list.append(a)
