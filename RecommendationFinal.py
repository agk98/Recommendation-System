import codecs
from math import sqrt
users={"Angelica":{"Blues Traveler":3.5,"Broken Bells":2.0,
                   "Norah Jones":4.5,"Phoenix":5.0,
                   "Slightly Stoopid":1.5,
                   "The Strokes":2.5,"Vampire Weekend":2.0},
       "Bill":     {"Blues Traveler":2.0,"Broken Bells":3.5,
                    "Deadmau5":4.0,"Phoenix":2.0,
                    "Slightly Stoopid":3.5, "Vampire Weekend":3.0},
       "Chan":      {"Blues Traveler":5.0,"Broken Bells":1.0,
                     "Deadmau5" : 1.0, "Norah Jones": 3.0,
                     "Phoenix": 5, "Slightly Stoopid": 1.0},
       "Dan":        {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                     "Deadmau5": 4.5, "Phoenix": 3.0,
                     "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                     "Vampire Weekend": 2.0},
       "Hailey":    {"Broken Bells": 4.0, "Deadmau5": 1.0,
                     "Norah Jones": 4.0, "The Strokes": 4.0,
                     "Vampire Weekend": 1.0},
       "Jordyn":    {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
                     "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                     "The Strokes": 4.0, "Vampire Weekend": 4.0},
       "Sam":       {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                     "Norah Jones": 3.0, "Phoenix": 5.0,
                     "Slightly Stoopid": 4.0, "The Strokes": 5.0},
       "Veronica":  {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                     "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                     "The Strokes": 3.0}}

class recommender:
    def init(self, data, k=1, metric="pearson", n=5):
        """Initializing recommender to dictionary containing all data
        k is the k value for k nearest neighbor
        n is maximum number of recommendations to make"""
        self.k=k
        self.n=n
        self.username2.id={}
        self.userid2name={}
        self.productid2name={}
        self.metric=metric
        if self.metric=='pearson':
            self.fn=self.pearson
        if type(data)._name_ == 'dict':
            self.data=data
    def convertProductID2name(self, id):
        """given product ID number, return product name"""
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id
    def userRatings(self, id, n):
        """Return n top ratings for user with id"""
        print('Ratings for '+self.userid2name[id])
        ratings=self.data[id]
        print(len(ratings))
        ratings = list(ratings.items())
        ratings=[(self.convertProductID2name(k),v)
                 for (k,v) in ratings]
        # Sorting and returning
        ratings.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        ratings=ratings[:n]
        for rating in ratings:
            print("%s\t%i"%(rating[0], rating[1]))
    def loadBookDB(self, path=''):
        """load the BX book dataset. Path is where the BX files are located"""
        self.data={}
        i=0
        #Load book ratings into self.data
        f=codecs.open(path + "BC-Book_ratings.csv", 'r','utf8')
        for line in f:
            i+=1
            #Seperating line into fields
            fields =line.split(';')
            user=fields[0].strip('"')
            book = fields[1].strip('"')
            rating=int(fields[2].strip.strip('"'))
            if user in self.data:
                currentRatings=self.data[user]
            else:
                currentRatings={}
            currentRatings[book] = rating
            self.data[user]=currentRatings
        f.close()
        #
        # Loading book sinto self.productid2name
        # Bookscontains isbn, title, and author among fields
        #
        f = codecs.open(path + "BX-Books.csv", 'r', 'utf8')
        for line in f:
            i+=1
            fields=line.split(';')
            isbn=fields[0].strip('"')
            title=fields[1].strip('"')
            author=fields[2].strip().strip('"')
            title = title+ 'by' +author
            self.productid2name[isbn]=title
        f.close()
        #
        # Loading user info into both self.userid2name and self.username2id
        #
        f=codecs.open(path + "BX-Users.csv", 'r', 'utf8')
        for line in f:
            i +=1
            # seperate line into fields
            fields = line.split(';')
            userid=fields[0].strip('"')
            location=fields[1].strip('"')
            if len(fields)>3:
                age=fields[2].strip().strip('"')
            else:
                age='NULL'
            if age!='NULL':
                value=location+' (age: '+age+' )'
            else:
                value=location
            self.userid2name[userid]=value
            self.username2id[location]=userid
        f.close()
        print(i)
    def pearson(self, rating1, rating2):
        sum_xy=0
        sum_x=0
        sum_y=0
        sum_x2=0
        sum_y2=0
        n=0
        for key in rating1:
            if key in rating2:
                n+=1
                x=rating1[key]
                y=rating2[key]
                sum_xy+=x*y
                sum_x+=x
                sum_y+=y
                sum_x2+=pow(x,2)
                sum_y2+=pow(y,2)
        if n==0:
            return 0
        denominator=(sqrt(sum_x2-pow(sum_x,2)/n)*sqrt(sum_y2-pow(sum_y,2)/n))
        if denominator == 0:
            return 0
        else:
            return (sum_xy-(sum_x*sum_y)/n)/denominator
    def computeNearestNeighbor(self, username):
        """ creates a sorted list of users based on their distance to the username"""
        distances=[]
        for instance in self.data:
            if instance!=username:
                distance=self.fn(self.data[username],self.data[instance],self.data[instance])
                distances.append((instance,distance))
        distances.sort(key=lambda artistTuple: artistTuple[1], reverse= True)
        return distances
    def recommend(self, user):
        recommendations={}
        # getting list of users ordered by nearness
        nearest=self.computeNearestNeighbor(user)
        #
        # now get the ratings for the user
        #
        userRatings=self.fata[user]
        #
        #determine the total distance
        totalDistance=0.0
        for i in range(self.l):
            totalDistance+=nearest[i][1]
        # now iterate through the k nearest neighbors
        # accumalating their ratings
        for i in range(self.k):
            # compute slice of pie
            weight=nearest[i][1]/totalDistance
            # get the name of the person
            name=nearest[i][0]
            # get the ratings for this person
            neighborRatings=self.data[name]
            # get the name of the person
            # now find bands neighbor rated that user didn't
            for artist in neighborRatings:
                if not artist in userRatings:
                    recommendations[artist]=(neighborRatings[artist]*weight)
                else:
                    recommendations[artist]=(recommendations[artist]+neighborRatings[artist]*weight)
            # making a list from dictionary
            recommendations=list(recommendations.item())
            recommendations=[(self.converProductID2name(k), v)
                             for (k,v) in recommendations]
            recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
            return recommendations[:self.n]
