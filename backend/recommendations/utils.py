import numpy as np
from scipy.stats import wasserstein_distance

def get_scores(profile, movies):
    scores = []
    for movie in movies:
        item = {}

        item["id"] = movie.movie_id
        item["genres"] = [eval(movie.symbolic_movie_genres['categories']), eval(movie.symbolic_movie_genres['histogram'])]
        item["actors"] = [eval(movie.symbolic_actors['categories']), eval(movie.symbolic_actors['histogram'])] 
        item["synopsis"] = [eval(movie.symbolic_synopsis['categories']), eval(movie.symbolic_synopsis['histogram'])]
        item["director"] = [[movie.symbolic_director['categories']], [float(movie.symbolic_director['histogram'])]]
        
        score = [] 
        scalling_factors = []

        for feature in item.keys():
            if feature != 'id':
                profile_user = profile[feature]
                categories = {pair[1]:pair[0] for pair in enumerate(set(profile_user[0]).union(item[feature][0]))}
                
                scalling_factors.append(len(set(profile_user[0]).union(item[feature][0])))
                
                u_values = [categories[category] for category in profile_user[0]]
                u_weights = [profile_user[1][profile_user[0].index(category)] for category in profile_user[0]]
                
                v_values = [categories[category] for category in item[feature][0]]
                v_weights = [item[feature][1][item[feature][0].index(category)] for category in item[feature][0]]
                
                score.append(wasserstein_distance(u_values=u_values, v_values=v_values , u_weights=u_weights, v_weights=v_weights ))

        scalling_factors = np.array([min(scalling_factors)/factor for factor in scalling_factors]) 

        scores.append((movie,(np.array(score)*scalling_factors).sum()/len(item.keys())))
    scores = sorted(scores, key=lambda tup: tup[1])
    scores = [movie[0] for movie in scores]
    return scores