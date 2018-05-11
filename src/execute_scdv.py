#! -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer,TfidfTransformer
from sklearn.feature_extraction import DictVectorizer

import pickle
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from gensim.models.keyedvectors import KeyedVectors
import logging
import time
import numpy as np

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

"""SCDVアルゴリズムで文書ベクトルを生成する。
生成した文書ベクトルを使って、作品間の類似計算までやってみる"""


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def cluster_GMM(num_clusters, word_vectors):
    logging.debug("Clustering Now...")
    # Initalize a GMM object and use it for clustering.
    clf =  GaussianMixture(n_components=num_clusters, covariance_type="tied", init_params='kmeans', max_iter=50)
    # Get cluster assignments.
    clf.fit(word_vectors)
    idx = clf.predict(word_vectors)
    logging.debug("Clustering Done...")
    # Get probabilities of cluster assignments.
    idx_proba = clf.predict_proba(word_vectors)
    # Dump cluster assignments and probability of cluster assignments.
    #pickle.dump(idx, open('../japanese-dataset/livedoor-news-corpus/model/gmm_latestclusmodel_len2alldata.pkl',"wb"))
    #logging.debug("Cluster Assignments Saved...")
    #pickle.dump(idx_proba,open( '../japanese-dataset/livedoor-news-corpus/model/gmm_prob_latestclusmodel_len2alldata.pkl',"wb"))
    #print ("Probabilities of Cluster Assignments Saved...")
    return (idx, idx_proba)


'''
def read_GMM(idx_name, idx_proba_name):
    # Loads cluster assignments and probability of cluster assignments.
    idx = pickle.load(open('../japanese-dataset/livedoor-news-corpus/model/gmm_latestclusmodel_len2alldata.pkl',"rb"))
    idx_proba = pickle.load(open( '../japanese-dataset/livedoor-news-corpus/model/gmm_prob_latestclusmodel_len2alldata.pkl',"rb"))
    print ("Cluster Model Loaded...")
    return (idx, idx_proba)'''


def get_probability_word_vectors(featurenames, word_centroid_map, num_clusters, word_idf_dict):
    # This function computes probability word-cluster vectors
    prob_wordvecs = {}
    for word in word_centroid_map:
        prob_wordvecs[word] = np.zeros( num_clusters * num_features, dtype="float32" )
        for index in range(0, num_clusters):
            try:
                prob_wordvecs[word][index*num_features:(index+1)*num_features] = model[word] * word_centroid_prob_map[word][index] * word_idf_dict[word]
            except:
                continue

    return prob_wordvecs


def create_cluster_vector_and_gwbowv(prob_wordvecs,
                                     wordlist,
                                     word_centroid_map,
                                     word_centroid_prob_map,
                                     dimension,
                                     word_idf_dict,
                                     featurenames,
                                     num_centroids,
                                     train=False):
    # This function computes SDV feature vectors.
    bag_of_centroids = np.zeros( num_centroids * dimension, dtype="float32" )
    global min_no
    global max_no

    for word in wordlist:
        try:
            temp = word_centroid_map[word]
        except:
            continue

        bag_of_centroids += prob_wordvecs[word]

    norm = np.sqrt(np.einsum('...i,...i', bag_of_centroids, bag_of_centroids))
    if(norm!=0):
        bag_of_centroids /= norm

    # To make feature vector sparse, make note of minimum and maximum values.
    if train:
        min_no += min(bag_of_centroids)
        max_no += max(bag_of_centroids)

    return bag_of_centroids


def run_scdv(word_embedding_model: KeyedVectors, num_clusters: int):
    """
    * Parameters

    """
    # Get wordvectors for all words in vocabulary.
    word_vectors = word_embedding_model.wv.syn0

    idx, idx_proba = cluster_GMM(num_clusters, word_vectors)

    # Create a Word / Index dictionary, mapping each vocabulary word to
    # a cluster number
    word_centroid_map = dict(zip(word_embedding_model.wv.index2word, idx))
    # Create a Word / Probability of cluster assignment dictionary, mapping each vocabulary word to
    # list of probabilities of cluster assignments.
    word_centroid_prob_map = dict(zip(word_embedding_model.wv.index2word, idx_proba))

    # 文書群のTF-IDF値を計算する
    DictVectorizer().fit_transform()
    tfv = TfidfVectorizer(dtype=np.float32)
    tfidfmatrix_traindata = tfv.fit_transform(traindata)
    featurenames = tfv.get_feature_names()
    idf = tfv._tfidf.idf_

    # Creating a dictionary with word mapped to its idf value
    logging.debug("Creating word-idf dictionary for Training set...")

    word_idf_dict = {}
    for pair in zip(featurenames, idf):
        word_idf_dict[pair[0]] = pair[1]


if __name__ == '__main__':
    path_default_word2vec_model = "../resources/entity_vector/entity_vector.model.bin"
    word_vectors = KeyedVectors.load_word2vec_format(path_default_word2vec_model, binary=True)

    num_features = 200  # Word vector dimensionality
    min_word_count = 20  # Minimum word count
    num_workers = 40  # Number of threads to run in parallel
    context = 10  # Context window size
    downsampling = 1e-3  # Downsample setting for frequent words
    run_scdv(word_vectors, num_clusters=60)


