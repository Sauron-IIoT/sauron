from app.repository.classification import classify as get_classification


def classify(capture):
    classification = get_classification(capture['path'])
    capture['prediction_label'] = classification['label']
    capture['prediction_confidence'] = classification['confidence']
    return capture