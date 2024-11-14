
# Project Design Document - draft
## SA Connect: "Streamlining the Student Assistant Recruitment Process"
--------
Prepared by:
* `Harleen Kaur`,`BME and RBE`
* `Julian Kreis`,`CS`
* `Jed Geoghegan`,`CS & DS`
* `Jacob Lu`,`IMGD & CS`
---
**Course** : CS 3733 - Software Engineering
**Instructor**: Sakire Arslan Ay
---
## Table of Contents
- [1. Introduction](#1-introduction)
- [2. Software Design](#2-software-design)
- [2.1 Database Model](#21-model)
- [2.2 Subsystems and Interfaces](#22-subsystems-and-interfaces)
- [2.2.1 Overview](#221-overview)
- [2.2.2 Interfaces](#222-interfaces)
- [2.3 User Interface Design](#23-view-and-user-interface-design)
- [3. References](#3-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)
<a name="revision-history"> </a>
### Document Revision History
| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2024-11-15 |Initial draft | 1.0 |
| | | | |


# 1. Introduction
Explain the purpose of this document. If this is a revision of an earlier document,
please make sure to summarize what changes have been made during the revision (keep
this discussion brief).

This document describes the design of the Student Assistant Recruitment System for the WPI Computer Science Department. The purpose of this system is to manage student assistant (SA) applications, position creation, and assignment to students. This document provides a detailed software design including the database model, subsystem architectures, and user interface designs. This is the first revision, and we plan to add more specific details and examples in future drafts.



# 2. Software Design
(**Note**: For all subsections of Section-2: You should describe the design for the
end product (completed application) - not only your iteration1 version. You will
revise this document and add more details later.)

## 2.1 Database Model
Provide a list of your tables (i.e., SQL Alchemy classes) in your database model
and briefly explain the role of each table.
Provide a UML diagram of your database model showing the associations and
relationships among tables.


Classes
- User: The base class that stores common information for both students and instructors
- Student: stores information specific to students
- Faculty: stores information specific to faculty
- Course Offering: stores course offering details
- Course Experience: stores data about a student's previous experience in a course
- SA Position: stores details of available SA positions
- SA Application: stores details of SA applications

UML Diagram:
<kbd>
      <img src="images/UML_Database_Diagram_Draft.png"  border="2">
</kbd>

## 2.2 Subsystems and Interfaces
### 2.2.1 Overview
Describe the high-level architecture of your software: i.e., the major subsystems
and how they fit together. Provide a UML component diagram that illustrates the
architecture of your software. Briefly mention the role of each subsystem in your
architectural design. Please refer to the "System Level Design" lectures in Week 4.

Major subsystems:
- User Management Subsystem: ensures that both students and faculty can securely log in, access their profiles, and perform actions based on their role (student or faculty)

- Course Management Subsystem: responsible for managing course details, including course names, sections, and terms. It ensures that SA positions are linked to the correct course and course section.

- SA Position Management Subsystem: responsible for managing the creation, modification, and removal of student assistant (SA) positions. Faculty members can create SA positions by associating them with specific courses and defining the number of positions available.

- SA Application Management Subsystem: responsible for managing the student application process for SA positions. It enables students to apply for positions, track their application statuses, and withdraw applications.

UML Component:
<kbd>
      <img src="images/UML_Component_Diagram_Draft.png"  border="2">
</kbd>


### 2.2.2 Interfaces
Include a detailed description of the routes your application will implement.
* Brainstorm with your team members and identify all routes you need to implement
for the **completed** application.
* For each route specify its “methods”, “URL path”, and “a description of the
operation it implements”.
* You can use the following table template to list your route specifications.
* Organize this section according to your subsytem decomposition, i.e., include a
=======


#### 2.2.2.1 \<User Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | POST | /users/student/register/ | registers a new user |
|2. | POST | /users/student/login/ | authenticates and logs in user |
|3. | GET | /users/student/logout	| ends a user session |
|4. | GET | /users/student/profile | retrieves the profile information of the logged-in user |
|5. | POST | /users/student/editprofile| edits a student's profile |
|6. | POST | /users/faculty/register/ | registers a new user |
|7. | POST | /users/faculty/login/ | authenticates and logs in user |
|8. | GET | /users/faculty/logout	| ends a user session |
|9. | GET | /users/faculty/profile | retrieves the profile information of the logged-in user |
|10. | POST | /users/faculty/editprofile| edits a faculty's profile |



#### 2.2.2.2 \<Course Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | POST | /course/create |creates a new course |
|2. | POST | /course/<course_id>/edit|edit an existing course |


#### 2.2.2.3 \<SA Pos Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. |POST | user/faculty/courses/create SA positions | create SA positions|
|2. |POST | user/faculty/courses/edit SA positions |edit SA positon |
|3. |GET | user/faculty/positions|displays list of all SA positions created|
|4. | GET | user/student/courses/applications/recommendations	| retrieves a list of recommended positions for the student based on interest |
|5. | GET | user/faculty/courses/applications/recommendations for faculty	| retrieves a list of recommended positions for each course for faculty member |


#### 2.2.2.4 \<Applications Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | GET | /applications | retrieves a list of all applications submitted by the logged-in user |
|2. | POST | /applications/submit | submits a new application for a course, position, or opportunity |
|3. | GET | /applications/{application_id} | retrieves details of a specific application for a course, position, or opportunity |
|4. | GET | /applications/status/{applicationId} | retrieves the status of a specific application |
|5. | POST | /applications/withdraw/{applicationId}	| withdraws a specfic application for a specified SA position |


### 2.3 User Interface Design
Provide a list of the page templates you plan to create and supplement your
description with UI sketches or screenshots. Make sure to mention which user-
stories in your “Requirements and Use Cases" document will utilize these interfaces
for user interaction.

Page Tempates: 
- Staff: Main page shows courses they've created, can open dropdown under each course that shows applicants and applicant info. Each course also has an edit button to go to an edit course form Create course page Edit course form

- Student: Main page shows courses they can apply to, including a separate relevant courses section Separate page to view application status

- Both: Login Page Profile creation page Edit Profile (Student will need more info)

![image](https://github.com/user-attachments/assets/184c8986-2c77-49bd-9888-7bc69108fb76)



# 3. References
Cite your references here.
For the papers you cite give the authors, the title of the article, the journal
name, journal volume number, date of publication and inclusive page numbers. Giving
only the URL for the journal is not appropriate.
For the websites, give the title, author (if applicable) and the website URL.
