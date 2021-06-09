from math import sqrt



from application.models import Job

# Load values from database to create dataset
def create_dataset( users_data ):
    # Array which is used to hold values of ids which will be queried later
    IDs = [1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #Creating the empty dataset
    dataset = []
    # Iterating through the records in the database to find the required data
    for id in IDs:
        # Collecting values of locations, posts, industry, company_name , as the four values for component 4
        locations = Job.query.filter_by(id=id).order_by(Job.location).first()
        posts = Job.query.filter_by(id=id).order_by(Job.post).first()
        industry = Job.query.filter_by(id=id).order_by(Job.industry).first()
        company_name = Job.query.filter_by(id=id).order_by(Job.company_name).first()
        #Adding the queried data to the dataset array
        dataset.append([posts.post,industry.industry, company_name.company_name ,locations.location])
    #appeneding the users value onto the end of the dataset
    dataset.append([users_data, None, None, None])
    #returning the new dataset
    return dataset

# Convert string values to unique integers in order to get the values mapped
def string_into_integer(dataset, index):

    class_val = [row[index] for row in dataset]
    q = set(class_val)
    dataset_in_numbers = dict()
    for i, value in enumerate(q):
        dataset_in_numbers[value] = i
    for row in dataset:
        row[index] = dataset_in_numbers[row[index]]
    return dataset_in_numbers

#finding the keys to the dictionary d
def integer_to_string(d, value):
    keys = [k for k, v in d.items() if v == value]
    return keys


# Finding  max and min values for each array within the dataset
def dataset_values(dataset):
    max_min_val = list()
    for i in range(len(dataset[0])):
        col_val = [row[i] for row in dataset]
        val_min = min(col_val)
        val_max = max(col_val)
        max_min_val.append([val_min, val_max])
    return max_min_val


# this function calculates the distance between two vectors and within knn model is known as the Euclidean distance
def vector_distance(vector1, vector2):
    #Setting the distance from the two vectors
    distance_from_vectors = 0.0
    #Iterating through vector len(vector1) - 1 so there is no out of range error
    for i in range(len(vector1) - 1):
        distance_from_vectors += (vector1[i] - vector2[i]) ** 2
    return sqrt(distance_from_vectors)


# Locating closest neighbors to a given value
def find_n(train_set, test_val, num_n):
    distances_from_n = list()
    for train_row in train_set:
        dist = vector_distance(test_val, train_row)
        distances_from_n.append((train_row, dist))
    distances_from_n.sort(key=lambda tup: tup[1])
    neighbors_list = list()
    for i in range(num_n-1):
        neighbors_list.append(distances_from_n[i][0])
    return neighbors_list

# Making a prediction with neighbors and a given value
def predict(train_set, user_value, num_n):
    n = find_n(train_set, user_value, num_n)
    new_values = [row[-1] for row in n]
    prediction = max(set(new_values), key=new_values.count)
    return prediction

#Function to remove characters out of a string, making the value easier when outputting
def read_string_for_array(array):
    sliced = array[2:]
    sliced = sliced[:-2]
    return sliced
