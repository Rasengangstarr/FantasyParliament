from politician import generatePoliticians
from politician import Politician
from job import Jobs
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

    def serialize_detailed(self, members):
        return {'id': self.id,
                'name': self.name,
                'stances': self.stances.serialize(),
                'members': [m.serialize() for m in members if m.party == self.id]}


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
    return (kmeans, df)


def createParties(members, numParties):
    # Get party names
    partyNames = requests.get(
        "https://story-shack-cdn-v2.glitch.me/generators/clan-name-generator?count="+str(numParties)).json()["data"]

    (kmeans, df) = findStanceCentroids(members, numParties)
    parties = []
    for i in range(0, len(members)):
        members[i].party = df.iloc[i]["party"]
        members[i].partyName = partyNames[int(members[i].party)]["name"]
    for i in range(0, numParties):
        partyMembers = [m for m in members if m.party == i]
        partyMembers[0].job = Jobs.LEADER
        partyMembers[1].job = Jobs.DEPUTY_LEADER
        partyMembers[2].job = Jobs.ELECTION_OFFICER

        parties.append(Party(i, partyNames[i]["name"], Stances(
            nature=kmeans.cluster_centers_[i][1], industry=kmeans.cluster_centers_[i][0], war=kmeans.cluster_centers_[i][2], magic=kmeans.cluster_centers_[i][3])))
    return parties
            
    
    
