# Sprint 4: V2 Polish, Reporting & V3 Foundations

**Sprint Duration:** 2 Weeks (Monday, Apr 28th, 2025 - Friday, May 9th, 2025)

**Deadline Formats:**
* **End of Week 1:** Friday, May 2nd
* **Mid Week 2:** Wednesday, May 7th
* **End of Week 2:** Friday, May 9th

---

## Objective
Refine V2 features (Admin Portal, Ratings display), implement basic admin reporting data flow and content moderation hooks. Lay the groundwork for V3 by implementing backend/database structures for detailed character personalities and preparing related BA documentation/diagrams.

---

## Key Milestones
* **Mid-Sprint Review:** End of Week 1 to demo polished Admin UI, display of ratings, basic admin reporting UI connected to backend, and draft V3 personality schema/API design. Review Activity diagrams.
* **Final Sprint Review:** End of Week 2, confirming stable V2 Admin features, basic reporting, content moderation hooks, initial backend setup for V3 personality, completed BA sections/diagrams for V1/V2, and readiness for V3 feature implementation.

---

## Team Tasks & Deliverables

### Minh (Designer, Front End)
* **Admin Portal UI Polish**
    * **Task:** Refine the Admin User Management, Reporting, and Config UIs based on feedback. Ensure consistent layout and responsiveness.
    * **Deadline:** End of Week 1.
    * **End Goal:** A polished and usable initial version of the Admin Portal.
* **Interaction History UI (Detailed View - Placeholder)**
    * **Task:** Implement the UI component for viewing detailed logs of a past interaction (Module 2.4). Connect to backend endpoint for text chat logs.
    * **Deadline:** Mid Week 2.
    * **End Goal:** UI displaying detailed text chat logs.
* **Ratings & Reviews UI (Display)**
    * **Task:** Implement UI components to display the average rating and potentially recent reviews on the Character Profile page (Module 2.5). Connect to backend endpoint.
    * **Deadline:** End of Week 2.
    * **End Goal:** Users can see existing feedback on characters.
* **V3 Character Form UI (Detailed Personality)**
    * **Task:** Implement the React components for the detailed personality fields in the Character Submission Form (Module 3.1) based on designs. Connect to backend API endpoints.
    * **Deadline:** End of Week 2.
    * **End Goal:** UI ready for users to input detailed personality traits.

### Duy (Backend, API, & Integration)
* **Interaction History Backend (Detailed Logs - Text Chat)**
    * **Task:** Enhance backend (Module 14) to store and retrieve full turn-by-turn logs for text chats. Implement endpoint to fetch detailed logs for a specific session.
    * **Deadline:** End of Week 1.
    * **End Goal:** API to retrieve detailed history for text chats.
* **Admin Reporting Backend (Basic Data)**
    * **Task:** Develop backend endpoints (Module 10) to provide basic analytics data (e.g., total users, total characters, interaction counts). Calculate and store `popularity_score` (Module 13) based on interactions/ratings.
    * **Deadline:** Mid Week 2.
    * **End Goal:** Basic reporting data available via API for the admin portal.
* **V3 Character Personality Backend (Initial)**
    * **Task:** Implement backend logic and API endpoints (Module 13) to store and retrieve the new detailed personality fields for characters.
    * **Deadline:** End of Week 2.
    * **End Goal:** Backend ready to manage advanced character personality data.
* **BA Documentation: Functional Requirements (V1/V2)**
    * **Task:** Write detailed functional requirement specifications based on the Use Cases for V1 and V2 features implemented so far (Auth, Char Submit/Validate, Chat, Ratings, History List, Admin User Mgmt).
    * **Deadline:** End of Week 2.
    * **End Goal:** Formal functional requirements document covering V1/V2 scope.

### Mui (Database, Data Management, & Backend Support)
* **Database Schema Updates (V3 - Personality)**
    * **Task:** Design and implement database schema changes (Module 18) to accommodate detailed personality fields.
    * **Deadline:** End of Week 1 (Design). Implementation by Mid Week 2.
    * **End Goal:** Database structure ready for V3 advanced character personality.
* **Content Moderation Setup**
    * **Task:** Integrate basic content moderation checks (Module 23) for user inputs (chat, reviews, character submissions) using a chosen library or service. Implement logging for flagged content.
    * **Deadline:** Mid Week 2.
    * **End Goal:** Basic filtering mechanism for inappropriate content.
* **Admin Reporting UI Implementation**
    * **Task:** Implement the Admin Reporting UI components (Module 10) to display the basic analytics data provided by the backend.
    * **Deadline:** End of Week 2.
    * **End Goal:** Admin dashboard showing key usage metrics.
* **Diagram Design: Activity Diagrams**
    * **Task:** Create Activity Diagrams for key processes like 'User Submits Character', 'Admin Validates Character', and 'User Rates Character'.
    * **Deadline:** End of Week 2.
    * **End Goal:** Visual workflow diagrams for core processes.

### Trung (Project Manager, Integration & Testing)
* **V2 Feature Testing (Admin, Reporting, Moderation)**
    * **Task:** Oversee and participate in thorough testing of Admin Portal features, reporting data accuracy, and content moderation triggers. Log bugs and prioritize fixes.
    * **Deadline:** Ongoing throughout the sprint.
    * **End Goal:** Stable and well-tested V2 feature set including Admin functions.
* **V3 Design Review (Personality Implementation)**
    * **Task:** Review the implementation plan for storing and retrieving detailed personality data. Ensure frontend and backend align.
    * **Deadline:** End of Week 1.
    * **End Goal:** Team alignment on the V3 personality feature implementation.
* **CI/CD Pipeline Enhancements**
    * **Task:** Update CI/CD pipeline (Module 24) to include tests for Admin API endpoints and potentially basic UI interaction tests if feasible.
    * **Deadline:** End of Week 2.
    * **End Goal:** More robust automated testing pipeline covering Admin features.
* **Sprint Review & Planning**
    * **Task:** Organize sprint review, demo V2 polish and V3 foundations, review BA docs/diagrams, gather feedback, and plan Sprint 5.
    * **Deadline:** End of Week 2.
