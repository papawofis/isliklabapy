#00.dist
from calc import get_distances

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = get_distances(sites)
print(distances)
