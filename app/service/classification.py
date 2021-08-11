from app.repository.classification import classify as get_classification


def classify(capture):
    classification = get_classification(capture['path'])
    capture['classification_score'] = classification['score']
    return capture