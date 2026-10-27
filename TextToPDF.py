# Fixing the encoding issue by ensuring all text is compatible with the output PDF format
from fpdf import FPDF

# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Amazon Business Intelligence Engineer Interview Questions & Answers", ln=True, align='C')

# Line break
pdf.ln(10)

# Set font for questions and answers
pdf.set_font('Arial', '', 12)

# Define the list of questions and answers
# It seems like we encountered an issue with non-ASCII characters (like smart quotes or special symbols).
# We will replace the problematic characters with standard ones to avoid encoding issues in the PDF.

# Rewriting the list of questions and answers with regular quotes and characters.
questions_and_answers_fixed = [
    ("1. What experience do you have in designing and implementing scalable data structures for analytics and reporting?", 
     "Answer:\n- Explain your experience with designing data models and structures that support high-volume, high-performance data processing for reporting purposes.\n- Mention specific tools you’ve used (e.g., AWS Redshift, Amazon S3, SparkSQL) and highlight any performance optimization strategies you’ve implemented to handle large datasets.\n- Example: 'In my previous role, I optimized Redshift clusters by implementing partitioning and indexing strategies, which improved query performance by 30%.'"),
    
    ("2. How do you ensure the performance and scalability of ETL pipelines?", 
     "Answer:\n- Discuss your approach to designing scalable ETL pipelines. Highlight how you handle data ingestion, transformation, and loading processes to ensure smooth operations even with large datasets.\n- Mention tools like AWS Glue, PySpark, and Python for automation, and any performance tuning practices you apply, such as batch processing, partitioning, and parallelization.\n- Example: 'To ensure scalability, I implement partitioning in SparkSQL to split large datasets into manageable chunks.'"),
    
    ("3. What is your experience with SQL and data modeling? Can you explain a scenario where you optimized a data model for better reporting performance?", 
     "Answer:\n- Talk about your experience with designing relational and non-relational databases and how you optimize schema for reporting efficiency.\n- Discuss normalization/denormalization, indexing, and query optimization techniques.\n- Example: 'I optimized a data model by denormalizing tables for reporting purposes, reducing the need for complex joins and improving query performance by 40%. I also used indexing strategies to speed up frequent queries.'"),
    
    ("4. Can you walk us through an ETL process you built using SQL, Python, or Spark?", 
     "Answer:\n- Walk the interviewer through a specific ETL pipeline you built. Describe the stages (data extraction, transformation, and loading) and the technologies you used.\n- Example: 'In a recent project, I built an ETL pipeline using AWS Glue to extract data from S3, transform it with PySpark to clean and aggregate the data, and then load it into Amazon Redshift for reporting.'"),
    
    ("5. How do you handle data integrity and reliability when migrating large datasets?", 
     "Answer:\n- Explain how you ensure that data remains accurate and consistent during migration. Discuss the steps you take for data validation, error handling, and retry mechanisms.\n- Example: 'During the migration of a legacy banking system to AWS, I ensured data integrity by implementing checksum comparisons, handling missing data, and setting up retries for failed jobs.'"),
    
    ("6. How would you handle a situation where business customers have unclear requirements for reporting solutions?", 
     "Answer:\n- Describe how you would work with business stakeholders to clarify their requirements. Emphasize communication and your ability to break down business needs into technical specifications.\n- Example: 'I would set up workshops with stakeholders to understand the high-level goals, break down their needs into smaller use cases, and iteratively design and deliver reporting solutions.'"),
    
    ("7. Can you give an example of a time when you had to improve an ongoing reporting process? How did you approach it?", 
     "Answer:\n- Talk about a time when you improved a reporting process by automating or simplifying it, which ultimately increased efficiency.\n- Example: 'I automated the data extraction process for weekly reports by developing a scheduled ETL job using AWS Glue. This saved the team 10 hours of manual work each week.'"),
    
    ("8. How do you collaborate with product managers, analysts, and other teams to implement data-driven solutions?", 
     "Answer:\n- Explain your experience working in cross-functional teams. Emphasize your communication skills and how you ensure alignment between technical and business teams.\n- Example: 'I regularly collaborate with product managers to understand the requirements and translate them into data solutions. For instance, in a project to build a recommendation system, I worked with data scientists to ensure the data pipelines were optimized for machine learning.'"),
    
    ("9. What experience do you have with big data technologies like Hadoop, Hive, or Spark?", 
     "Answer:\n- Discuss your experience with big data technologies, particularly how you’ve used them to process and analyze large datasets.\n- Example: 'I have worked extensively with Apache Spark for data transformation and aggregation tasks. I used SparkSQL to process large datasets efficiently in a distributed environment.'"),
    
    ("10. How do you prioritize tasks and manage tight deadlines in a fast-paced environment?", 
     "Answer:\n- Describe your approach to time management, prioritizing critical tasks, and handling high-pressure situations. Mention how you break down tasks and meet deadlines.\n- Example: 'In my current role, I use agile methodologies to manage my workload, breaking tasks into sprints and ensuring I meet deadlines by working collaboratively with cross-functional teams.'"),
]

# Write each question and answer to the PDF
for q_and_a in questions_and_answers_fixed:
    pdf.multi_cell(0, 10, txt=q_and_a[0], align='L')
    pdf.multi_cell(0, 10, txt=q_and_a[1], align='L')
    pdf.ln(5)

# Save the PDF
file_path = 'C:/Users/THAKU/Downloads/Amazon_Business_Intelligence_Engineer_Interview_Questions_and_Answers1.pdf'
pdf.output(file_path, 'F')

file_path
