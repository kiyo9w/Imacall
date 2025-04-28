# Sprint 3: Admin Portal Foundation & Community Feedback

**Sprint Duration:** 2 Weeks (Monday, Apr 14th, 2025 - Friday, Apr 25th, 2025)

**Deadline Formats:**
* **End of Week 1:** Friday, Apr 18th
* **Mid Week 2:** Wednesday, Apr 23rd
* **End of Week 2:** Friday, Apr 25th

---

## Objective
Implement foundational Admin Portal features (User Management, basic Reporting/Config UI), integrate user feedback mechanisms (Ratings/Reviews), establish interaction history lists, and begin core BA documentation and diagramming. Prepare backend/database for these V2 features.

---

## Key Milestones
* **Mid-Sprint Review:** End of Week 1 to demo initial Admin User Management UI/Backend, basic endpoints for ratings, and draft Use Case diagrams.
* **Final Sprint Review:** End of Week 2, confirming functional Ratings/Reviews submission, basic Admin User Management, Interaction History list view, System Config UI/Backend basics, and initial BA documentation/diagrams.

---

## Team Tasks & Deliverables

### Minh (Designer, Front End)
* **Admin User Management UI Implementation**
    * **Task:** Develop React components for the Admin User Management screen (Module 6) based on mockups, including displaying a list of users and potentially a detail view placeholder. Connect to backend endpoints.
    * **Deadline:** End of Week 1 (List View). Full component by End of Week 2.
    * **End Goal:** A functional UI for admins to view registered users.
* **Admin Reporting & Config UI (Basic Placeholders)**
    * **Task:** Create basic UI components/placeholders for the Admin Reporting dashboard (Module 10) and System Configuration screen (Module 9) based on mockups.
    * **Deadline:** Mid Week 2.
    * **End Goal:** Initial UI structure for admin reporting and configuration sections.
* **Ratings & Reviews UI (Submission)**
    * **Task:** Implement UI elements (e.g., star rating input, text area) within the chat/character profile to allow users to submit ratings and reviews (Module 2.5). Connect to backend endpoints.
    * **Deadline:** End of Week 2.
    * **End Goal:** Interface for users to provide feedback on characters.

### Duy (Backend, API, & Integration)
* **Admin User Management Backend (Full CRUD)**
    * **Task:** Develop Node.js Express endpoints (Module 6 & 12) for full CRUD operations on users (View list, View details, potentially Edit status/role - basic implementation). Ensure proper authorization checks.
    * **Deadline:** End of Week 1 (Read operations). Full CRUD by End of Week 2.
    * **End Goal:** Secure backend support for managing users via the Admin Portal.
* **Interaction History Backend (Basic List)**
    * **Task:** Create endpoints to retrieve a list of past interaction sessions (Module 14) for a user (metadata only, e.g., character ID, timestamp, session ID).
    * **Deadline:** Mid Week 2.
    * **End Goal:** API to fetch the user's conversation history list.
* **Ratings & Reviews Backend (Submission)**
    * **Task:** Develop endpoints to receive and store user ratings and reviews (Module 13) associated with a character and user.
    * **Deadline:** End of Week 2.
    * **End Goal:** Backend capability to store user feedback.
* **BA Documentation: Use Cases**
    * **Task:** Draft detailed Use Cases for core V1 features: User Registration, User Login, Character Submission, Admin Character Validation.
    * **Deadline:** End of Week 2.
    * **End Goal:** Formal Use Case descriptions for key initial functionalities.

### Mui (Database, Data Management, & Backend Support)
* **Database Schema Updates (V2 - History, Ratings, Admin)**
    * **Task:** Extend the database schema (Module 18) for interaction history metadata, user ratings/reviews, and any fields needed for admin user management (e.g., user roles, status).
    * **Deadline:** End of Week 1 (Draft Schema). Final implementation by Mid Week 2.
    * **End Goal:** Database structure capable of supporting V2 features (History, Ratings, Admin).
* **Data Access Implementation (V2 - History, Ratings, Admin)**
    * **Task:** Implement SQL queries or ORM methods for CRUD operations related to interaction history metadata, ratings/reviews, and admin user management (Module 13, 14, 6).
    * **Deadline:** End of Week 2.
    * **End Goal:** Data access layer updated for new V2 entities.
* **System Configuration Backend/UI (Basic)**
    * **Task:** Implement basic backend/UI (Module 9) for viewing/editing essential system settings (e.g., placeholder for API keys, site name).
    * **Deadline:** End of Week 2.
    * **End Goal:** Foundational backend/UI for system configuration by admins.
* **Diagram Design: Use Case Diagram**
    * **Task:** Create a Use Case Diagram illustrating the main actors (User, Admin) and their interactions with the system based on the Use Cases drafted by Duy.
    * **Deadline:** End of Week 2.
    * **End Goal:** Visual overview of system functionality and user interactions.

### Trung (Project Manager, Integration & Testing)
* **Admin Portal Development Coordination**
    * **Task:** Coordinate frontend (Minh) and backend (Duy, Mui) efforts for the Admin Portal features. Ensure API integration works smoothly.
    * **Deadline:** Ongoing, functional flow by End of Week 2.
    * **End Goal:** Successful integration of initial Admin Portal components.
* **Admin Portal UI Mockups (Reporting & Config)**
    * **Task:** Create basic wireframes/mockups for the Admin Reporting Dashboard and System Configuration screen (Modules 10, 9).
    * **Deadline:** End of Week 1.
    * **End Goal:** Clear UI direction for admin reporting and config views.
* **Testing Strategy (V2 Features - Ratings, History List, Admin)**
    * **Task:** Define test cases for Rating/Review submission, Interaction History list view, and Admin User Management (View List/Details).
    * **Deadline:** Mid Week 2.
    * **End Goal:** Test plan covering new V2 functionality.
* **Sprint Review & Planning**
    * **Task:** Organize sprint review meeting, demo completed features, review diagrams/docs, gather feedback, and plan Sprint 4.
    * **Deadline:** End of Week 2.