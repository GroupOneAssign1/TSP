# Travelling Salesman Problem (TSP) Project

## Project Overview
This project aims to solve the TSP using three different methods:
- Brute Force -Exact Algo
- Branch and Bound-Exact Algo
- Ant Colony Optimization--Heuristic Algo(still work in progress)

  also note to mention other methods, e.g
Dynamic Programming
Nearest Neighbour
Genetic Algorithm

Each method is implemented in its own folder under `methods/`.

## Contribution Guidelines
1. Pull the latest changes from the main branch.
2. Create a new branch for your task:
   ```
   git checkout -b feature/your-feature-name
   ```
3. Work on your assigned method/module.
4. Commit your changes with descriptive messages.
5. Push your branch to GitHub.
6. Open a Pull Request (PR) to merge into main.
7. Request reviews from your team members.
8. After approvals, merge your PR.

## Team Task Division
Member 1- Intoduce TSP, why it matters e.t.c
- Member 2-3: Implement and optimize Brute Force method (`methods/brute_force/`)
- Member 3-4: Implement and optimize Branch and Bound method (`methods/branch_and_bound/`)
- Member 4: Finalize with Implementing and optimize Ant Colony Optimization method (`methods/ant_colony_optimization/`)
- Member 5-6: Visualization of the routes and Optimization
- Member 7: Conclusions and Recommendation
- Member 8-9: Slides compilation and Presentation Support
- Member 10: Project integration, testing, and documentation

## How to Run
How to Run the Program

Follow these steps to set up and execute the TSP solver on your local machine:
Prerequisites

    Python 3.x: Ensure you have Python 3.6 or newer installed. You can download it from python.org.

Setup Steps

    Clone the Repository:
    If you haven't already, clone the project repository to your local machine:
    Bash

git clone https://github.com/GroupOneAssign1/TSP.git

Navigate to the Project Directory:
Change your current directory to the cloned TSP project folder:
Bash

cd TSP

Create a Virtual Environment (Recommended):
It's best practice to create a virtual environment to manage project dependencies.
Bash

python -m venv .venv

Activate the Virtual Environment:

    On Windows:
    PowerShell

.\.venv\Scripts\activate

On macOS/Linux:
Bash

    source ./.venv/bin/activate

(You should see (.venv) at the beginning of your terminal prompt, indicating the environment is active.)

Install Dependencies (if any):
If the project relies on external Python libraries (e.g., NumPy, SciPy), they would typically be listed in a requirements.txt file. If such a file exists, install them:
Bash

    pip install -r requirements.txt

    (If no requirements.txt exists, you can skip this step, or install any necessary libraries individually, e.g., pip install numpy)

Running the Solver

Once the setup is complete, you can run the TSP solver.

    To run the main solver program:
    Bash

python tsp_solver.py

Input (if applicable):
(Add details here on how your program expects input. For example:)

    The program might prompt you to enter city coordinates or a distance matrix.
    Alternatively, it might read input from a specific file, e.g., python tsp_solver.py --input data.txt (Adjust this based on how your tsp_solver.py file actually handles input.)

Output:
(Describe what the user should expect to see as output. For example:)

    The program will output the shortest tour found, the order of cities visited, and the total distance.
    It might also display intermediate steps or a visual representation of the path.


🧾 Conclusions

1.Diverse Algorithm Implementation: The project explores multiple approaches to solving the TSP, including:

    1.Brute Force: An exact algorithm that evaluates all possible permutations to find the optimal solution.

    2.Branch and Bound: An exact algorithm that systematically considers candidate solutions and eliminates suboptimal ones based on bounds.

    3Ant Colony Optimization (ACO): A heuristic algorithm inspired by the foraging behavior of ants, currently a work in progress.

2.Modular Structure: Each algorithm is organized within its own folder under the methods/ directory, promoting clarity and ease of navigation.

3.Collaborative Development: The presence of a CONTRIBUTIONS.md file and detailed contribution guidelines indicates an emphasis on collaborative development and version control practices.

✅ Recommendations

1.Complete the ACO Implementation: Finalizing the Ant Colony Optimization algorithm would enhance the project's exploration of heuristic methods and provide a comparative analysis against exact algorithms.
arXiv

2.Incorporate Additional Algorithms: Implementing other heuristic and metaheuristic algorithms, such as:

     Dynamic Programming: To solve smaller instances of TSP efficiently.

     Nearest Neighbour: A simple heuristic that builds a tour by repeatedly visiting the nearest unvisited city.

    Genetic Algorithm: A metaheuristic inspired by the process of natural selection, useful for larger instances.


3.Performance Benchmarking: Conducting performance evaluations across different algorithms using metrics like computation time and solution quality would provide valuable insights into their efficiencies and practical applications.


## License
info? 
Any ideas, send hapa, after this...the floor is open
