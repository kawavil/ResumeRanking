from spacy.pipeline import EntityRuler
from spacy import displacy
import jsonlines

# Create list with entity labels from jsonl file
with jsonlines.open('skills_set.json') as f:
    created_entities = [line['label'].upper() for line in f.iter()]


def add_newruler_to_pipeline(skill_pattern_path):
    """Reads in all created patterns from a JSONL file and adds it to the pipeline after PARSER and before NER"""

    new_ruler = EntityRuler(nlp).from_disk(skill_pattern_path)
    nlp.add_pipe(new_ruler, after='parser')


def visualize_entity_ruler(entity_list, doc):
    '''Visualize the Skill entities of a doc'''

    options = {"ents": entity_list}
    displacy.render(doc, style='ent', options=options)


visualize_entity_ruler(created_entities, doc)