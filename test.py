import warnings

warnings.filterwarnings('ignore')
import os
import nl_core_news_sm
from spacy.pipeline import EntityRuler
from spacy import displacy
import seaborn as sns
import matplotlib.pyplot as plt
import jsonlines
from spacy.language import Language
import en_core_web_sm
from spacy_langdetect import LanguageDetector

PROJECT_DIR = os.path.dirname(os.getcwd()) + '/'
skill_pattern_path = "./skill_patterns.jsonl"
nlp = en_core_web_sm.load()


def add_newruler_to_pipeline(skill_pattern_path):
    """Reads in all created patterns from a JSONL file and adds it to the pipeline after PARSER and before NER"""
    new_ruler = EntityRuler(nlp).from_disk(skill_pattern_path)
    nlp.create_pipe("new_ruler")


add_newruler_to_pipeline(skill_pattern_path)
