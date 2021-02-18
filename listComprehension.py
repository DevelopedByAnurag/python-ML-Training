movie_and_ratings={"Interstellar":9,"Dark Knight":8,"Iron Man":10,"Avengers":10}
l=[]
for movie in movie_and_ratings:
    if movie_and_ratings[movie]> 9:
        l.append(movie)

        pass
    pass
print(l)
#list Comprehension
print([movie for movie in movie_and_ratings if movie_and_ratings[movie] > 9])

