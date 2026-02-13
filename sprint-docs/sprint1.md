# SPRINT 1: EXECUTION DOCUMENT

## Sprint Goal

    To deliver a first working increment of the ETL data pipeline that 
    can extract and transform a dataset, supported by automated testing 
    and a basic CI/CD pipeline.



## 1. Work Delivered (Completed Backlog Items)

### Completed User Story 1: Data Ingestion Pipeline (High Priority)

Description:
    Developed transformation logic to clean and standardize the dataset.

#### What Was Delivered:

- Removal of duplicate records

- Handling of missing values

- Column formatting and data type correction

- Output of cleaned dataset file

#### Acceptance Criteria Status:

- Missing values handled ✔

- Duplicate records removed ✔

- Clean dataset generated ✔


### Completed User Story 4: Automated Testing (Medium Priority)

Description:
    Implemented unit tests to validate the ETL pipeline functions.

### What Was Delivered:

- Unit tests for data ingestion function

- Unit tests for transformation logic

- Test execution integrated into CI pipeline

### Acceptance Criteria Status:

- Tests created for core pipeline functions ✔

- Tests pass locally ✔

- Tests run automatically in CI ✔



## 2. Version Control Evidence (Git – Incremental Delivery)

To follow Agile and DevOps best practices, development was done through small, iterative commits instead of a single final commit.

Example Commit History (Iterative & Incremental)
```bash

Initial project setup and folder structure

Add raw dataset and ingestion script

Implement data cleaning and transformation logic

Refactor transformation functions for readability

Add unit tests for ETL pipeline

Fix failing test for missing values handling

Configure GitHub Actions CI pipeline

Update README and documentation
```

This commit pattern demonstrates:

- Continuous integration of features

- Incremental delivery

- No “big-bang” commit (meets Delivery Discipline rubric)



## 3. CI/CD Pipeline Setup (DevOps Practice)
CI Tool Used:

- GitHub Actions (Basic Continuous Integration Pipeline)

Pipeline Configuration (main.yml) Includes:

- Automatic trigger on push and pull requests

- Python environment setup

- Dependency installation (requirements.txt)

- Automated test execution using pytest

CI Workflow Stages:

- Checkout repository

- Set up Python environment

- Install dependencies

- Run unit tests

- Report success/failure logs

DevOps Outcome:

- Pipeline runs automatically on every commit ✔

- Failed tests stop the build ✔

- Logs provide visibility into pipeline execution ✔



## 4. Testing Implementation (Integrated with CI)
Testing Approach:

- Unit Testing

Test Coverage:

- Data ingestion function (file loading)

- Transformation logic (missing values & duplicates)

- Output validation (clean dataset generation)

Tools Used:

- Pytest (testing framework)

- GitHub Actions (automated test execution)

Evidence to Submit:

- tests/test_pipeline.py file

- Screenshot of successful test run

- CI pipeline logs showing passing tests

This fulfills:

- “Testing Evidence: Your test files and screenshots of test results”



## 5. Sprint Review (Demo / Delivery Evidence)
What Was Demonstrated in Sprint 1

- During the Sprint Review, the following working features were presented:

Functional Increment Delivered:

- Working ETL pipeline (Extract + Transform)

- Clean dataset output file

- Automated tests integrated with CI pipeline

Demo Evidence (Recommended for Submission):

- Screenshot of ETL script running successfully

- Screenshot of cleaned dataset output

- Screenshot of GitHub commit history

- Screenshot of successful CI pipeline run (green check)

Stakeholder Value Delivered:

- The system now processes raw datasets into cleaned, usable data automatically, 
providing a foundational Data Engineering pipeline ready for database loading 
and further automation in Sprint 2.



## 6. Sprint 1 Retrospective (Agile Reflection)
What Went Well

- Clear backlog and sprint planning improved task focus

- Incremental Git commits supported continuous integration

- CI/CD pipeline helped detect issues early through automated testing

- Agile approach enabled structured and manageable development

Challenges Faced

- Initial configuration of CI/CD pipeline required troubleshooting

- Writing test cases for data transformation logic took longer than expected

Improvements for Sprint 2 (At Least 2 Specific Process Improvements)

Improve Test Coverage:
- Expand unit tests to include edge cases such as corrupted datasets and schema validation to enhance pipeline reliability.

Enhance DevOps Automation:
- Extend the CI pipeline to include linting and automated data validation checks to improve code quality and monitoring.

Better Task Breakdown:
- Break user stories into smaller technical tasks to improve estimation accuracy and sprint execution speed.