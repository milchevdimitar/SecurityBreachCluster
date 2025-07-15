from readable_https_model import ReadableHttpsModel
from unreadable_https_model import UnreadableHttpsModel

class HttpsSecurityInterface:
    def __init__(self):
        self.readable_model = ReadableHttpsModel()
        self.unreadable_model = UnreadableHttpsModel()

    def analyze_readable(self, features, label=None):
        score = self.readable_model.predict(features)
        if label is not None:
            self.readable_model.update(features, label)
        return score

    def analyze_unreadable(self, features, label=None):
        score = self.unreadable_model.predict(features)
        if label is not None:
            self.unreadable_model.update(features, label)
        return score


if __name__ == "__main__":
    interface = HttpsSecurityInterface()

    #Primer READBL
    features_r = [0.1]*12
    label_r = 0  #SAFE
    score_r = interface.analyze_readable(features_r, label_r)
    print(f"Readable prediction score: {score_r:.3f}")

    #Primer UNREADBL
    features_u = [0.2]*8
    label_u = 1  #NSAFE
    score_u = interface.analyze_unreadable(features_u, label_u)
    print(f"Unreadable prediction score: {score_u:.3f}")
