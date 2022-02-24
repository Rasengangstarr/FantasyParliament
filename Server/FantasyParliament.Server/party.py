from politician import generatePoliticians
from politician import Politician
from stances import Stances
from sklearn.cluster import KMeans
from pandas import DataFrame
import requests


class Party:
    def __init__(self, id, name, stances):
        self.id = id
        self.name = name
        self.stances = stances
    
    def serialize(self):
            return {'id': self.id,
                    'name': self.name,
                    'stances': self.stances.serialize()}


def convertMembersToDataFrame(members):
    mps = []
    for m in members:
        mps.append({"id": m.id, "war": m.stances.war, "magic": m.stances.magic,
                   "industry": m.stances.industry, "nature": m.stances.nature})
    return DataFrame(mps)


def findStanceCentroids(members, numParties):
    df = convertMembersToDataFrame(members)
    cluster_dims = ['war', 'magic', 'industry', 'nature']
    kmeans = KMeans(n_clusters=numParties, random_state=0).fit(
        df[cluster_dims].values)
    df['party'] = kmeans.labels_
    return df


def createParties(members, numParties):
    # Get party names
    partyNames = requests.get(
        "https://story-shack-cdn-v2.glitch.me/generators/clan-name-generator?count="+str(numParties)).json()["data"]

    df = findStanceCentroids(members, numParties)
    parties = []
    for i in range(0, numParties):
        parties.append(Party(i, partyNames[i]["name"], Stances(
            nature=df.iloc[i]["nature"], industry=df.iloc[i]["industry"], war=df.iloc[i]["war"], magic=df.iloc[i]["magic"])))
    
    return parties
