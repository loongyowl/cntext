__version__ = "1.7.8"

from cntext.dictionary import SoPmi, W2VModels, co_occurrence_matrix, Glove
from cntext.similarity import jaccard_sim, minedit_sim, simple_sim, cosine_sim
from cntext.stats import load_pkl_dict, dict_pkl_list, term_freq, readability, sentiment, sentiment_by_valence, sentiment_by_weight
from cntext.mind import Text2Mind





