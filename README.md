# 590PR Final_Project

# Title: Project Outsourcing Planning using Monte Carlo Simulation

## Team Member(s):
Pranali Mane
Saurav Yadav

# Monte Carlo Simulation Scenario & Purpose:
Outsourcing is a business practice in which services or job functions are farmed out to a third party. In information technology, an outsourcing initiative with a technology provider can involve a range of operations, from the entirety of the IT function to discrete, easily defined components, such as disaster recovery, network services, software development or QA testing. A lot of companies believe in outsourcing because of the several benefits it provides.

The project is divided into 2 scenarios:
Scenario 1: Fixed employees
  This scenario is useful for organizations that want to estimate the number of projects they can complete within a year, based on certain independent variables/resources. We have used Monte Carlo simulation for estimating the average number of projects a software development company will have to outsource every year, assuming employees work only on a single project at a time.
  
Scenario 2: Fixed projects
  If a company wants to estimate the human resources it will need for a year, this scenario is useful.
  
## Simulation's variables of uncertainty
1) Project Duration - The duration of the project is randomly distributed between 12 - 20 weeks.  
2) Size of the team - Number of team members in each team is randomly distributed between 3 - 7 members.
3) Sensitivity of the project - This variable defines how early the client wants to get started off with the project. It is randomly distributed between 2 - 12 weeks.
4) Priority - Priority of the project, useful while choosing a project out of the queue.

## Hypotheses or hypothesis of your simulation
The simulation does not have a hypothesis, but some of the assumptions that it considers are:
1) One employee will work only on one project at a time
2) Scenario 1 considers 30 employees
3) Scenario 2 considers 50 completed projects as the goal
4) Projects in queue are considered incomplete

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
Initially, while working on Scenario 2 - Fixed Projects, because of the way the program was made, we encountered a problem of a lot of employees being idle in the initial weeks of the year. In order to overcome this problem, we considered incomplete projects from the previous year, which the employees could work on upon the beginning of the new year.

The purpose of the simulation is to help organizations understand their capabilities with existing resources, and gives an idea about the amount of resources it needs to achieve ceratin goals. It'll also help them work upon their resource utilization. 

## Instructions on how to use the program:
The usage is pretty simple as there is no dataset or any other external sources involved.
Download the 2 python (.py) files and run them using any environment.

## All Sources Used:
 https://www.cio.com/article/2439495/outsourcing/outsourcing-outsourcing-definition-and-solutions.html
 https://www.jstor.org/stable/4143844?read-now=1&seq=1#page_scan_tab_contents
