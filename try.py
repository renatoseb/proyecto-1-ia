import random 
from bokeh.plotting import figure, output_file, show

POINTS_COLOURS = ['turquoise', 'lime', 'dodgerblue', 'fuchsia', 'lightcoral', 'navajowhite']
CLUSTERS_COLOURS = ['teal', 'green', 'blue', 'purple', 'red', 'goldenrod']

SIZE_COORD = 10         # size of coordinate to graphic
MIN_LIMIT = 1           # minimum limit of coordinates
MAX_LIMIT = 40          # maximum limit of coordinates
NUM_COORDS = 150        # number of coordinates to clustering
NUM_CLUSTERS = 4        # number of clusters to clustering

# generate base coords
def generate_coords(num_coords, mn, mx):
    coords = []
    for i in range(num_coords):
        coords.append((int(random.uniform(mn, mx)), int(random.uniform(mn, mx))))
    return coords 

# generate graph in bokeh
def generate_graph(coords, loop, clusters, centers):

    output_file(f"dispersion {loop}.html")
    x_coords = [c[0] for c in coords]
    y_coords = [c[1] for c in coords]
    p = figure(title=f"Dataset {loop}", x_range=(MIN_LIMIT-1, MAX_LIMIT+1), y_range=(MIN_LIMIT-1, MAX_LIMIT+1))

    if loop>1:      # clusters

        asterisk_x = [c[0] for c in centers]
        asterisk_y = [c[1] for c in centers]

        
        for i in range(len(clusters)):
            clusters_x = [c[0] for c in clusters[i]]
            clusters_y = [c[1] for c in clusters[i]]

            p.scatter(clusters_x, clusters_y , color=CLUSTERS_COLOURS[i], alpha=.5, size=SIZE_COORD)
            p.asterisk(asterisk_x[i], asterisk_y[i], color=CLUSTERS_COLOURS[i], size=SIZE_COORD+2)
            
    else:    
        p.scatter(x_coords, y_coords, color="black", alpha=.5, size=SIZE_COORD)

    return p

# generate first random centers of clusters
def generate_random_centers(num_clusters, mn, mx):
    c = []
    for i in range(4):
        c.append((int(random.uniform(mn, mx)), int(random.uniform(mn, mx))))
    return c

# calculate euclidean distance
def euclidean_distance(coord1, coord2):
    return ((coord1[0]-coord2[0])*2 + (coord1[1]-coord2[1])*2)*0.5

# generate list of clusters
def k_means(centers, coords):
    clusters = []
    for i in range(len(centers)):
        clusters.append([])
    
    for c in coords:
        distances = []
        for i in range(len(centers)):
            d = euclidean_distance(c, centers[i])
            distances.append(d)
            
        md = min(distances)
        idx = distances.index(md)

        clusters[idx].append(c)
    return clusters
    
# update centers
def update_centers(clusters):
    c = []
    for i in range(len(clusters)):
        x_clus = [c[0] for c in clusters[i]]
        y_clus = [c[1] for c in clusters[i]]
        
        x_new_center = sum(x_clus)/len(x_clus)
        y_new_center = sum(y_clus)/len(y_clus)
        
        c.append((x_new_center, y_new_center))
    return c

# comparate clusters
def comparate_clusters(previous_cluster, actual_cluster):
    for i in range(len(previous_cluster)):
        if previous_cluster[i][0] != actual_cluster[i][0] or previous_cluster[i][1] != actual_cluster[i][1]:
            return "distintos"
    
    return "iguales"



l = 1

# generate coordinates
coords = []
coords = generate_coords(NUM_COORDS, MIN_LIMIT, MAX_LIMIT)
print("\n\tCoordinates Generated:\n",coords)

# plot coordinates
plot = generate_graph(coords, l, None, None)
show(plot)
l+=1

# generate 1st random centers
centers = generate_random_centers(NUM_CLUSTERS, MIN_LIMIT, MAX_LIMIT)
print("\n\tRandom Centers:\n",centers)

# 1st K-Means
## generate clusters
clusters = k_means(centers, coords)  
print("\n\tRandom Clusters:\n", clusters)

## plot clusters
plot = generate_graph(coords, l, clusters, centers)
show(plot)

p_cluster = []
for i in range(2, 10):
    centers = update_centers(clusters)
    clusters = k_means(centers, coords)

    plot = generate_graph(coords, i, clusters, centers)        
    show(plot) 

    if comparate_clusters(p_cluster, clusters)=="iguales" and i>2:
        break
    else: 
        p_cluster = clusters