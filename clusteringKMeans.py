import numpy as np
from sklearn.cluster import KMeans

from sentenceTransformerEncoder import encodeSentence

n_clusters = 20


def Kmeans(df, testmessage):
    # print("Entered K Means")
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    print("Started Clustering the Train information")
    df["predictions"] = clusterer.fit_predict(np.vstack(df["Encoded"]))
    print("Test Message Provided: " + testmessage.text)
    testmessage = encodeSentence(str(testmessage.text))
    print("Encoded the Test message")
    predicted_label = clusterer.predict(testmessage)
    print("Predicted the Test message")
    # print(predicted_label)
    # print(df.shape)
    df_Train_filtered = df[df["predictions"] == predicted_label[0]]
    # print(df_Train_filtered.shape)
    # print(df_Train_filtered.to_excel("Clustered.xlsx", engine="xlsxwriter"))
    if df_Train_filtered.to_excel("Clustered.xlsx", engine="xlsxwriter") is None:
        print(
            "Semantically similar sentences to the sample text from Train Data saved in Clustered.xlsx"
        )
        return ["Saved similar sentences in Clustered.xlsx successfully"]
    return ["Please check error logs"]
