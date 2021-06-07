import warnings
warnings.filterwarnings('ignore')
from spacy.pipeline import EntityRuler
from spacy import displacy
import jsonlines
import nl_core_news_sm
import os

nlp = nl_core_news_sm.load()
PROJECT_DIR = os.path.dirname(os.getcwd()) + '/'

skill_pattern_path = "./skills_set.jsonl"
# Create list with entity labels from jsonl file
print(skill_pattern_path)
with jsonlines.open('skills_set.jsonl') as f:
    created_entities = [line['label'].upper() for line in f.iter()]
    print(*created_entities)


def add_newruler_to_pipeline(skill_pattern_path):
    """Reads in all created patterns from a JSONL file and adds it to the pipeline after PARSER and before NER"""

    new_ruler = EntityRuler(nlp).from_disk(skill_pattern_path)
    nlp.add_pipe(new_ruler) # , after='parser'


def visualize_entity_ruler(entity_list, doc):
    """Visualize the Skill entities of a doc"""

    options = {"ents": entity_list}
    displacy.render(doc, style='ent', options=options)


doc = """Do you want your software skills to contribute meaningfully into finding technology driven solutions for various businesses and alongside grow your career, then read on. Our client provides data-based process optimization and analytics solutions to businesses worldwide. Their innovative algorithms and customized IT solutions cater to complex problems related to every field or industry, through tools that are non standard and are backed-up by extensive research. They serve startups as well as large, medium and small enterprises, a majority of their clients being industry leaders. With registered offices in India, USA and UAE, their projects support various sectors and functions like logistics, IT, Retail, Ecommerce, Healthcare industry among others, across Asia, America and Europe. The founder holds a Master’s degree from IIT and a PhD in Operations Research from USA, with rich experience in Optimization and Analytics for various industries. His team of top scientists and pedagogy experts are focusing on innovative revenue generation ideas with minimum operational costs. As a Data Scientist, you will apply expertise in machine-learning, data mining and statistical methods to design, prototype, and build the next-generation analytics engines and services. What you will do: Conducting advanced statistical analysis to provide actionable insights, identify trends, and measure performance Performing data exploration, cleaning, preparation and feature engineering; in addition to executing tasks such as building a POC, validation/ AB testing Collaborating with data engineers &amp; architects to implement and deploy scalable solutions Communicating results to diverse audiences with effective writing and visualizations Identifying and executing on high impact projects, triage external requests, and ensure timely completion for the results to be useful Providing thought leadership by researching best practices, conducting experiments, and collaborating with industry leaders What you need to have: 2-4 year experience in machine learning algorithms, predictive analytics, demand forecasting in real-world projects Strong statistical background in descriptive and inferential statistics, regression, forecasting techniques. Strong Programming background in Python (including packages like Tensorflow), R, D3.js , Tableau, Spark, SQL, MongoDB. Preferred exposure to Optimization &amp; Meta-heuristic algorithm and related applications Background in a highly quantitative field like Data Science, Computer Science, Statistics, Applied Mathematics,Operations Research, Industrial Engineering, or similar fields. Should have 2-4 years of experience in Data Science algorithm design and implementation, data analysis in different applied problems. DS Mandatory skills : Python, R, SQL, Deep learning, predictive analysis, applied statistics"""
add_newruler_to_pipeline(skill_pattern_path)
visualize_entity_ruler(created_entities, nlp(doc))
