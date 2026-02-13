# SPRINT 0: PLANNING (SETUP)

### 1. Product Vision (1–2 Sentences)

The vision of this prototype is to build an automated Data Engineering ETL
pipeline that extracts raw dataset files, cleans and transforms the data, 
and loads the processed data into a structured database with automated testing and CI/CD integration.
The solution will demonstrate iterative Agile development and DevOps practices 
through version control, automated testing, and continuous integration.



### 2. Product Backlog (User Stories)

(All written in proper Agile format: As a [user], I want [feature], so that [value])

- User Story 1

    As a data engineer, I want to ingest a raw CSV dataset so that the pipeline can process real-world data.

- User Story 2

    As a data engineer, I want to clean and transform the dataset so that the data becomes accurate and usable for analysis.

- User Story 3

    As a data engineer, I want to load the processed data into a database so that it can be stored and queried efficiently.

- User Story 4

    As a developer, I want automated tests for the pipeline so that I can ensure data quality and pipeline reliability.

- User Story 5

    As a DevOps practitioner, I want a CI/CD pipeline configured so that tests run automatically on every commit.

- User Story 6

    As a user, I want logging in the pipeline so that errors and processing steps can be monitored.



### 3. Refined Backlog (Acceptance Criteria, Priority & Estimates)
(Using Agile best practice: Priority + Story Points)

#### Priority Order: High → Medium → Low

##### User Story 1: Data Ingestion Pipeline

Acceptance Criteria:

- The system can read a raw CSV dataset successfully

- The dataset is loaded without errors

- File path handling is configurable

Priority: High
Story Points: 3


##### User Story 2: Data Cleaning & Transformation

Acceptance Criteria:

- Missing values are handled (removed or filled)

- Column formats are standardized

- Duplicate records are removed

- Clean dataset is saved as a new file

Priority: High
Story Points: 5


##### User Story 3: Load Data into Database (ETL Completion)

Acceptance Criteria:

- Clean data is stored in PostgreSQL

- Table is created automatically if it does not exist

- Data can be queried successfully from the database

Priority: High
Story Points: 5


##### User Story 4: Automated Testing (Data Validation Tests)

Acceptance Criteria:

- Unit tests exist for pipeline functions

- Tests validate data ingestion and transformation

- All tests pass in local environment

Priority: Medium
Story Points: 3


##### User Story 5: CI/CD Pipeline Configuration (DevOps)

Acceptance Criteria:

- GitHub Actions workflow file (main.yml) is created

- Pipeline runs automatically on push

- Tests execute successfully in CI environment

- Failed tests stop the pipeline

Priority: Medium
Story Points: 5


##### User Story 6: Pipeline Logging & Monitoring

Acceptance Criteria:

- Logs show extraction, transformation, and loading steps

- Errors are recorded in log file

- Logs are readable and structured

Priority: Low
Story Points: 2



### 4. Definition of Done (DoD) – Agile + DevOps Standard

A user story will be considered “Done” only when:

- Code is implemented and pushed to GitHub repository

- Feature meets all acceptance criteria

- Unit tests are written and passing

- CI/CD pipeline runs successfully without errors

- Code follows clean structure and documentation standards

- No critical bugs remain

- Commit history shows incremental development (not one big commit)

- Relevant logs or outputs are generated for verification



### 5. Sprint 1 Plan (Selected Stories)
Sprint Goal:

Deliver a basic working ETL pipeline with data ingestion and transformation.

Selected User Stories for Sprint 1 (2–3 Stories)

- User Story 1 – Data Ingestion Pipeline (3 SP)

- User Story 2 – Data Cleaning & Transformation (5 SP)

- User Story 4 – Automated Testing (3 SP)

Total Story Points: 11 SP (Reasonable for a small prototype sprint)