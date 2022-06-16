from sklearn.metrics.pairwise import cosine_similarity
from bertopic import BERTopic

class ModelNotTrainedException(Exception):

    pass



class JuridIQ():


    def __init__(self, model="pretrained"):

        if model == "pretrained":
            self.model = load_model()
            self.trained = True
        else:
            self.model = BERTopic(language="multilingual", calculate_probabilities = True, verbose = True)
            self.trained = False


    def train_model(self, articles):

        self.model.fit_transform(articles)
        self.trained = True


    def save_model(self, model = None, model_name="pretrained"):

        if model is None:
            self.model.save(model_name)

        else:
            model.save()


    def get_topics(self, articles):

        if self.trained is False:
            self.train_model(articles)

        return self.model.transform(articles)[1]

    def get_topic(self, article):

        if self.trained is False:
            raise ModelNotTrainedException("Attempting to predict topic using an untrained model")

        return self.model.transform(article)
    
    def get_keyword_topic(self, keyword):

        if self.trained is False:
            raise ModelNotTrainedException("Attempting to predict topic using an untrained model")

        return self.model.find_topics(keyword, top_n=50)

                   
                   
def load_model(model="pretrained"):

        return BERTopic.load(model)


def is_similar(first_list, second_list, threshold=0.85):

    return cosine_similarity([first_list, second_list])[0][1] >= threshold


def get_similar(list_to_check, list_to_check_against, threshold = 0.85):

    output = []
    for index in range(len(list_to_check_against)):
        if is_similar(list_to_check_against[index], list_to_check, threshold):
            output.append(index)

    return output
