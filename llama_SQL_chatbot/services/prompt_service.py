class PromptService:
    @staticmethod
    def build_prompt(question: str) -> str:
        schema = """
# Database Schema:

Table: registration
- si_no (int, AI, PK)
- name_ (varchar)
- cc_no (varchar)
- designation (varchar)
- date_of_joining (varchar)
- grade (varchar)
- year_passed_out (int)
- college_name (varchar)
- branch (varchar)
- qualification (varchar)
- photo (longtext)
- status_ (varchar)
- existing_cc_no (varchar)
- is_existing (varchar)

Table: examine_details
- si_no (int, AI, PK)
- topics (varchar)
- cc_no (varchar)
- actual_score (varchar)
- status_ (varchar)
- sign_by_trainee (longtext)
- sign_by_training_officer (longtext)
- Remarks (varchar)
- date (varchar)
- place (varchar)
- faculty_name (varchar)
- day_one (varchar)
- day_two (varchar)
- day_three (varchar)
- entry_date (varchar)

Table: memory_details
- memory_id (int, AI, PK)
- cc_no (varchar)
- process_name (varchar)
- process_obsevations (varchar)
- attempts (varchar)
- mistakes (varchar)
- heart_test (varchar)
- data_time (varchar)
- status_ (varchar)
- sign_trainee (longtext)
- sign_team_leader (varchar)
- remarks (varchar)
- place (varchar)
- module (varchar)
- cell (varchar)
- title_memory_process_name (varchar)

Table: attempts_cycle
- id (int, AI, PK)
- task_id (int)
- attempt_number (varchar)
- attempts_id (varchar)
- ji_demo_line_captain (varchar)
- remarks (varchar)
- date (varchar)
- place (varchar)
- bu_table (varchar)

Table: tasks_cycle
- task_id (int)
- cc_no (varchar)
- station_name (varchar)
- dct (varchar)
- status_ (varchar)
- remarks (text)
- date_ (varchar)
- attempt (varchar)
- actual_score (varchar)
- demo_line_captain (varchar)
- demo_trainee (varchar)
- cycle_achievement (varchar)
- skill_matrix (varchar)
- process_name (varchar)
- signature_by_trainee (longtext)
- signature_by_line_caption (varchar)
- signature_by_module_controller (varchar)
- created_at (timestamp)
- updated_at (timestamp)
- place (varchar)
- module (varchar)
- cell (varchar)
- title_cycle_process_name (varchar)
"""

        few_shot_examples = """
# Examples:

Q: How do I find all tasks for a specific cc_no?
A: SELECT * FROM tasks_cycle WHERE cc_no = 'your_cc_no';

Q: How do I list all examine details where status_ is 'Pass'?
A: SELECT * FROM examine_details WHERE status_ = 'Pass';

Q: How to get registration details of a person with cc_no = 'CC123'?
A: SELECT * FROM registration WHERE cc_no = 'CC123';

Q: How do I fetch memory details where mistakes are not null?
A: SELECT * FROM memory_details WHERE mistakes IS NOT NULL;

Q: How to count the number of attempts for task_id = 10?
A: SELECT COUNT(*) FROM attempts_cycle WHERE task_id = 10;

Q: List all tasks_cycle records created today.
A: SELECT * FROM tasks_cycle WHERE DATE(created_at) = CURDATE();

Q: How to find examine_details for a specific faculty_name?
A: SELECT * FROM examine_details WHERE faculty_name = 'Faculty_Name';

Q: Get all memory_details where process_name is 'Welding'.
A: SELECT * FROM memory_details WHERE process_name = 'Welding';

Q: Fetch registration records where qualification is 'Diploma'.
A: SELECT * FROM registration WHERE qualification = 'Diploma';

Q: Retrieve all tasks_cycle with status_ 'Pass' and place 'Plant A'.
A: SELECT * FROM tasks_cycle WHERE status_ = 'Pass';

Q: List attempts_cycle data where attempt_number = '2'.
A: SELECT * FROM attempts_cycle WHERE attempt_number = '2';


"""

        return f"""
You are an AI SQL generator.
Given a question, you will generate the correct MySQL query.only generete the query no explaination
Don't add table name not in prompts
Check the given question clearly and generate the sql
While giving the out frame table and give the out put in words
If they give other than related to my sql natural language question   give the output  as "I am SQL generated BOT"
{schema}

{few_shot_examples}

# Question:
{question}

# SQL Query:
"""

