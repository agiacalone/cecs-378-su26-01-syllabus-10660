---
serial: 736AFD06
---

<!--
═══════════════════════════════════════════════════════════════════════════
  CECS SYLLABUS TEMPLATE  ·  reusing this for a new term?
  Edit ONLY the two marked blocks below:
    1.  COURSE INFORMATION table   (search: "TERM VARIABLES — COURSE")
    2.  TENTATIVE SCHEDULE table   (search: "TERM VARIABLES — SCHEDULE")
  Then update the five vars at the top of gen_output.sh and run it.
  Everything else is term-invariant boilerplate.
  Styling lives in syllabus.css (Swiss/grid theme, screen + print).
═══════════════════════════════════════════════════════════════════════════
-->

# Introduction to Computer Security Principles

> CECS 378 · Section 01 · Summer 2026

A first course in the fundamentals of cryptography and information and computer security — basic concepts, theories, and protocols, from symmetric encryption through buffer overflows.

**Jump to:**
[Course Info](#course-information) ·
[Description](#course-description) ·
[Materials](#required-materials) ·
[Grading](#grading--assessment) ·
[Schedule](#tentative-schedule) ·
[GitHub & Software](#github--software) ·
[Policies](#course-policies) ·
[Resources](#student-resources--accommodations)

## Course Information

<!-- ▼▼▼ TERM VARIABLES — COURSE · edit this table each term ▼▼▼ -->

| Field | Detail |
|------|--------|
| **Course** | CECS 378 — Introduction to Computer Security Principles |
| **Section** | 01 (Class Number 10660) |
| **Term** | Summer 2026 |
| **Meets** | Mon / Wed · 8:00 AM – 12:00 PM |
| **Room** | ECS-407 |
| **Format** | Lecture 2 hrs · Laboratory 3 hrs · Letter grade (A–F) |
| **Instructor** | Anthony Giacalone |
| **Email** | anthony.giacalone@csulb.edu |
| **Office** | ECS-501 |
| **Office Hours** | By appointment |

<!-- ▲▲▲ END TERM VARIABLES — COURSE ▲▲▲ -->

## Course Description

**Prerequisites:** CECS 229 and CECS 274 or CECS 275, all with a grade of C or better.

An introduction to the fundamentals of cryptography and information and computer security. Basic concepts, theories and protocols in computer security: basic cryptography, software security, operating system security, database security, network security, human factors, social engineering, digital forensics, privacy and anonymity.

**By the conclusion of this course, students will be able to:**

- Understand the meaning and risks of computer security
- Apply problem-solving skills to recognize and solve security problems
- Understand, recognize, and know how to avoid the main security vulnerabilities
- Make ethical decisions with respect to computer security and user privacy
- Know how to design and analyze a secure computer system in general
- Have a solid understanding of current, topical issues in computer security

## Required Materials

> [!NOTE]
> **Textbook —** *[Computer Security: Principles and Practice](https://www.amazon.com/Computer-Security-Principles-Practice-4th/dp/0134794109)*, 4th edition. William Stallings and Lawrie Brown, 2017.

You are responsible for finding and installing any software needed to complete the programming assignments. While not strictly required, **I highly recommend installing a Linux operating system on your computer or running a Linux virtual machine.** This course can be completed in its entirety using free, open-source software.

## Grading & Assessment

| Component | Weight | | Grade | Scale |
|-----------|:-----:|---|:-----:|:-----:|
| Homework and Labs | 35% | | **A** | ≥ 90% |
| Exam One | 20% | | **B** | 80 – 89% |
| Exam Two | 20% | | **C** | 70 – 79% |
| Final Exam | 25% | | **D** | 60 – 69% |
| **Total** | **100%** | | **F** | < 60% |

### Exams

Students will take **two midterm exams** during the term, with a **final exam** administered at the conclusion. There may be some writing on the quizzes and exams.

> [!IMPORTANT]
> There are **no makeups** for any quiz or exam. During in-class exams or quizzes there are **no bathroom breaks** — please use the restroom beforehand. A student who leaves the classroom before the exam concludes forfeits the remainder of their exam.

## Tentative Schedule

<!-- ▼▼▼ TERM VARIABLES — SCHEDULE · edit this table each term ▼▼▼ -->

| Date | Subject |
|------|---------|
| **May 27** (W) | Intro to Computer Security (Ch 1) |
| **Jun 1** (M) | Symmetric and Asymmetric Encryption (Ch 2, 20, 21) |
| **Jun 3** (W) | Encryption, continued |
| **Jun 8** (M) | 🅰 **First Exam** · Malicious Software (Ch 6) |
| **Jun 10** (W) | Malware, continued |
| **Jun 15** (M) | Denial of Service Attacks (Ch 7) |
| **Jun 17** (W) | Database and Cloud Security (Ch 5) |
| **Jun 22** (M) | 🅱 **Second Exam** · Buffer Overflow (Ch 10) |
| **Jun 24** (W) | Buffer Overflow, continued |
| **Jun 29** (M) | User Authentication and Access Control (Ch 3, 4) |
| **Jul 1** (W) | Case Studies · 🅵 **Final Exam** |

<!-- ▲▲▲ END TERM VARIABLES — SCHEDULE ▲▲▲ -->

> [!NOTE]
> The schedule is tentative and may shift. All material presented in class is fair game for exams and homework.

## GitHub & Software

### Linking Your GitHub Account

All labs are distributed via **GitHub Classroom**. When you accept the first lab assignment, GitHub Classroom will prompt you to select your **student identifier** from a class roster — choose the entry matching your **CSULB Student ID** (the 9-digit number from MyCSULB). This one-time selection links your GitHub username to your enrollment record for the rest of the term.

> [!TIP]
> You do **not** need to fill out any separate form. The Classroom roster handles the binding automatically.

## Course Policies

### Attendance

Attendance is **mandatory** — all material presented during class is fair game for exam questions or homework. Students are responsible for notifying the instructor about any extended leave of absence. There are no makeups for assignments, quizzes, or exams missed due to an unexcused absence.

### Class Rules

Homework and lab assignments will be assigned approximately every other week, and will mostly involve written work and coding.

- Homework and lab assignments are due on the date and time indicated on [GitHub Classroom](http://classroom.github.com).
- Homework may include writing code, doing research, essay writing, debugging programs, and other disciplines.
- Lab assignments will be coding projects designed to practice the concepts discussed in lecture.
- You are welcome to work on assignments at home, but assistance is provided only during class time or office hours.
- Labs are graded on correct answers to required deliverables and/or the completeness of the assignment. Incomplete assignments may receive partial or no credit at the instructor's discretion.
- You are expected to read the assigned textbook selections **before** each lecture so we can discuss the topics in class.
- **All source code submitted must be adequately commented to receive credit.** Source code that is not commented with the student's own comments *will not receive any credit*.

> [!WARNING]
> **Late assignments** are subject to a minimum **10% grade reduction per day** late. I do not accept homework submissions via email, fax, or any means other than the deliverable requirements listed on the assignment specification.

### Grading Philosophy

Programming and systems assignments in this course are evaluated as demonstrations of understanding, not as checklists of features. While rubrics may be provided to outline major expectations, they are descriptive rather than contractual and do not guarantee credit for partial or surface-level compliance. A working program, the presence of files, or matching output alone does not imply mastery. Credit is awarded based on the overall quality, correctness, completeness, and clarity of the work, including evidence of individual reasoning and design decisions appropriate to the concepts being taught. As in professional engineering practice, submissions that are incomplete, inconsistent, or fail to demonstrate sufficient understanding may receive partial or no credit at the instructor's discretion.

### Academic Honesty

> [!CAUTION]
> There is **zero tolerance** for cheating, plagiarism, or any other violation of Academic Integrity Policy. **Unless explicitly allowed by the assignment, sharing code with your peers is considered cheating.**

Work that you submit is assumed to be original unless your source material is documented appropriately, using proper citation. Using the ideas or words of another person — even a peer or a website — as if it were your own is plagiarism. Any individual or group caught cheating on homework, lab assignments, or any exam/quiz will be subject to the full extent of academic actions allowed under University regulations. At a minimum, any student caught violating Academic Integrity Policy will receive no credit for the work concerned and one lower letter grade. To learn more, visit [Academic Integrity Regarding Cheating and Plagiarism](https://www.csulb.edu/academic-senate/policy-academic-integrity-regarding-cheating-and-plagiarism).

### Ethical Use of Artificial Intelligence (Large Language Models)

Students are encouraged to explore and utilize Artificial Intelligence (AI) tools to enhance their learning experience. However, the use of AI must align with the principles of academic integrity and ethical conduct. AI tools may be used for tasks such as brainstorming, editing, or coding assistance, provided their use is transparently disclosed and does not misrepresent the student's own understanding or effort. Unauthorized use of AI to complete assignments, plagiarize content, or generate work without proper attribution is prohibited and will be treated as a violation of academic integrity policies. If you are uncertain about whether a particular use of AI is permitted, please consult the instructor before proceeding.

### Withdrawal Policy

Students may request a withdrawal from the instructor as long as the request meets University requirements and no more than one of the assigned midterm exams has been given to the class. Requests for withdrawal involving extenuating circumstances will be evaluated on a case-by-case basis at the discretion of the instructor.

## Student Resources & Accommodations

<details>
<summary><strong>COE Tutoring · Disability Accommodations · Basic Needs</strong> — click to expand</summary>

### COE Tutoring Services

The College of Engineering Tutoring Center offers free tutoring for many lower- and upper-division engineering courses in MAE, CECS, CECEM, CHE, and EE. Tutors are available Monday through Friday during the fall and spring semesters, 9:00 AM – 6:00 PM, in EN2-300. [Detailed tutoring schedules](http://web.csulb.edu/colleges/coe/views/essc/academic_success/engineering_tutor.shtml).

### Accommodations for Disability

Students with a disability or medical restriction requesting a classroom accommodation should contact the **Bob Murphy Access Center (BMAC)** at 562-985-5401, or visit SCC room 110 during 8:00 AM – 5:00 PM weekday hours. BMAC will work with the student to identify a reasonable accommodation in partnership with appropriate academic offices and medical providers. **We encourage students to reach out to BMAC as soon as possible.**

### Accommodations for Food and Housing

Any student facing academic or personal challenges due to difficulty affording groceries/food and/or lacking a safe and stable living environment is urged to contact the **CSULB Student Emergency Intervention & Wellness Program**. [Resources are listed here](http://www.csulb.edu/basicneeds). Students can also email supportingstudents@csulb.edu or call 562-985-2038. If comfortable, students may reach out to the professor, who may be able to identify additional resources.

</details>

*Syllabus version 736AFD06 · 2026-06-09*
