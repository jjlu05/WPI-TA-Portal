
# Project Design Document
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
- User: The base class that stores common information for both students and instructors.
- Student: stores information specific to students.
- Faculty: stores information specific to faculty.
- Course: stores course details
- SA Position: stores details of available SA positions
- SA Application: stores details of SA application

UML Diagram: CHECK

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




UML Component: CHECK


### 2.2.2 Interfaces
Include a detailed description of the routes your application will implement.
* Brainstorm with your team members and identify all routes you need to implement
for the **completed** application.
* For each route specify its “methods”, “URL path”, and “a description of the
operation it implements”.
* You can use the following table template to list your route specifications.
* Organize this section according to your subsytem decomposition, i.e., include a
sub-section for each subsytem and list all routes for that sub-section in a table.



#### 2.2.2.1 \<User Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | | | |
|2. | | | |
|3. | | | |
|4. | | | |
|5. | | | |
|6. | | | |



#### 2.2.2.2 \<Course Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | | | |
|2. | | | |
|3. | | | |
|4. | | | |
|5. | | | |
|6. | | | |

#### 2.2.2.2 \<SA Pos Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | | | |
|2. | | | |
|3. | | | |
|4. | | | |
|5. | | | |
|6. | | | |


#### 2.2.2.2 \<Course Management SS> Routes
| | Methods | URL Path | Description |
|:--|:------------------|:-----------|:-------------|
|1. | | | |
|2. | | | |
|3. | | | |
|4. | | | |
|5. | | | |
|6. | | | |


### 2.3 User Interface Design
Provide a list of the page templates you plan to create and supplement your
description with UI sketches or screenshots. Make sure to mention which user-
stories in your “Requirements and Use Cases" document will utilize these interfaces
for user interaction.



# 3. References
Cite your references here.
For the papers you cite give the authors, the title of the article, the journal
name, journal volume number, date of publication and inclusive page numbers. Giving
only the URL for the journal is not appropriate.
For the websites, give the title, author (if applicable) and the website URL.


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)
* You will first submit a draft version of this document:
* "Project 3 : Project Design Document - draft" (5pts).
* We will provide feedback on your document and you will revise and update it.
* "Project 5 : Project Design Document - final" (80pts)
Below is the grading rubric that we will use to evaluate the final version of your
document.
|**MaxPoints**| **Design** |
|:---------:|:---------------------------------------------------------------------
----|
| | Are all parts of the document in agreement with the product
requirements? |
| 8 | Is the architecture of the system ([2.2.1 Overview](#221-overview))
described well, with the major components and their interfaces?
| 8 | Is the database model (i.e., [2.1 Database Model](#21-database-model))
explained well with sufficient detail? Do the team clearly explain the purpose of
each table included in the model?|
| | Is the document making good use of semi-formal notation (i.e., UML
diagrams)? Does the document provide a clear UML class diagram visualizing the DB
model of the system? |
| 18 | Is the UML class diagram complete? Does it include all classes
(tables) and does it clearly mark the PK and FKs for each table? Does it clearly
show the associations between them? Are the multiplicities of the associations
shown correctly? ([2.1 Database Model](#21-database-model)) |
| 25 | Are all major interfaces (i.e., the routes) listed? Are the routes
explained in sufficient detail? ([2.2.2 Interfaces](#222-interfaces)) |
| 13 | Is the view and the user interfaces explained well? Did the team
provide the screenshots of the interfaces they built so far. ([2.3 User Interface
Design](#23-user-interface-design)) |
| | **Clarity** |
| | Is the solution at a fairly consistent and appropriate level of
detail? Is the solution clear enough to be turned over to an independent group for
implementation and still be understood? |
| 5 | Is the document carefully written, without typos and grammatical
errors? |
| 3 | Is the document well formatted? (Make sure to check your document on
GitHub. You will loose points if there are formatting issues in your document. )
|
| | |
| 80 | **Total** |
| | |
