from math import sqrt
users={"Angelica":{"Blues Traveler":3.5,"Broken Bells":2.0,
                   "Norah Jones":4.5,"Phoenix":5.0,
                   "Slightly Stoopid":1.5,
                   "The Strokes":2.5,"Vampire Weekend":2.0},
       "Bill":     {"Blues Traveler":2.0,"Broken Bells":3.5,
                    "Deadmau5":4.0,"Phoenix":2.0,
                    "Slightly Stoopid":3.5, "Vampire Weekend":3.0},
       "Chan":      {"Blues Traveler":5.0,"Broken Bells":1.0,
                     "Deadmau5":1.0, "Norah Jones": 3.0,
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
def pearson(rating1, rating2):
    """Implementing Pearson formula to check for agreement """
    xy_sum=0
    x_sum=0
    y_sum=0
    x2_sum=0
    y2_sum=0
    n=0
    for key in rating1:
        if key in rating2:
            n+=1
            x = rating1[key]
            y=rating2[key]
            xy_sum+=x*y
            x_sum += x
            y_sum += y
            x2_sum += x*x
            y2_sum += y*y
    # return 0 if there are no ratings in common
    if n == 0:
        return 0
    # computing denominator
    denominator  = sqrt(x2_sum - (x_sum**2)/n) * sqrt(y2_sum-(y_sum**2)/n)
    if denominator == 0:
        return 0
    else:
        return (xy_sum - (x_sum * y_sum)/n)/denominator