
# Project Group Report - 2
## Team: `GitGurus`
* `Harleen Kaur`,`BME and RBE`
* `Julian Kreis`,`CS`
* `Jed Geoghegan`,`CS & DS`
* `Jacob Lu`,`IMGD & CS`
---
**Course** : CS 3733 - Software Engineering
**Instructor**: Sakire Arslan Ay
----
## 1. Iteration 2 - Summary
* Include a summary of your `Iteration-2` accomplishments.
* List the user stories completed in `Iteration-2`. Mention who worked on those
user stories.

We completed all the basic functionality required for iteration 2: 
* students can apply for positions 
* students can view positions made by the faculty user including position details 
* the faculty user can now view applications that are submitted by students
* faculty can view courses they created 
* aws is deployed for the app
* added bootstrap styling for forms and pages 
* added datetime where applicable for the application 

Completed User Stories:
* As faculty, I want to view student applications so that I can review qualifications and hire applicants - Harleen and Julian
* As a student, I want to apply to SA positions so that I can get a job. - Jacob and Julian 
* As a student, I want to view a detailed description of a position so that I can understand the requirements for each course. - Harleen
* As a student, I want to view all SA positions so that I can choose positions of interest. - Jacob and Jed 


----
## 2. Iteration 2 - Sprint Retrospective
* Include the outcome of your `Iteration-2 Scrum retrospective meetings`.
* Mention the changes the team will be doing to improve itself as a result of the
Scrum reflections.

Outcome: 
* Team worked well overall on the project 
* Team agreed that imporvements include:
    * pushing more often and sooner to share progress with others 
    * ensure merge conflicts are managed properly 
* Things that went well 
    * started working on assignment earlier 
    * Individual errors were brought to team and everyone helped to resolve issues 
    * assigned tickets in a fair manner and organized completion of work well  
    * communication was clear and ensured everyone was updated as tasks were completed 

----
## 3. Product Backlog refinement
* Have you made any changes to your `product backlog` after `Iteration-2`? If so,
please explain the changes here.

* added issues for:
    * AWS and postgres integration ([#54](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/54))
    * carding all forms ([#56](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/56))
    * adding datetime where applicable ([#57](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/57))

----
## 4. Iteration 3 - Sprint Backlog
Include a draft of your `Iteration-3 sprint backlog`.
* List the user stories you plan to complete in `Iteration-3`. Make sure to break
down the larger user stories into smaller size stories. Mention the team member(s)
who will work on each user story.
* Make sure to update the "issues" on your GitHub repo accordingly.

* User Stories:
    * As faculty, after interviewing a student, I would like to update the status of their application from “Pending” to "Assigned" so that I can hire them for the position. - Harleen 
    * As a student, I want to have "assigned" SA positions be disabled for withdrawal so I can't withdraw from "assigned" positions. - Jacob
    * As faculty, I want to assign SA positions based on student applications and qualifications, ensuring each student is only assigned to a single position. - Jed
    * As a student, I want to withdraw my application for a SA position so that I can change my decision to be a SA. - Jacob
    * As a student, I want to view the status of my applications so that I can track my SA application progress. - Harleen 
    * As a student, I want to see what SA positions match my qualifications and have these positions listed separately under "Recommended SA Positions" - Julian and Jacob

* created new task issues for upcoming sprint 
    * Github Tickets Created:
        * Implement Azure SSO for Login ([#66](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/66))
        * [Implementation] Finish up front-end edits ([#68](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/68))
        * [Implementation] Store student qualifications 
        * [Implementation] Faculty member approving/selecting student applicants for an SAship position they created
        * [Implementation] Created recommended section and algorithm
        * [Implementation] refine student profile for student application
        * [Implementation] Student can withdraw their application to a position(unless they've already been approved)
        * [Implementation] viewing status of application as a student 
        * [Implementation] faculty ability to view the qualifications of each student ([#69](https://github.com/WPI-CS3733-2024B/termproject-gitgurus/issues/69)) 
