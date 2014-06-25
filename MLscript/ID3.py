# encoding = utf-8
"""
the interpretation of decision-tree ID3,C4.5, CART algorithms
only differs at the split-index
receiving json-like dataset, e.g:
{}
"""
import math

def ID3_gain(data, attr, target_attr):
    """
    Info_gain
    """
    def entropy(data, target_attr):
        val_freq = {}
        data_entropy = 0.0

        for record in data:
            if record[target_attr] in val_freq:
                val_freq[record[target_attr]] += 1.0
            else:
                val_freq[record[target_attr]] = 1.0

        for freq in val_freq:
            data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2)

        return data_entropy

    val_freq = {}
    subset_entropy = 0.0

    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]]  = 1.0

    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy(data, target_attr) - subset_entropy)


def C45_gain(data, attr, target_attr):
    """
    info_gain/split_info
    """
    def entropy(data, target_attr):
        val_freq = {}
        data_entropy = 0.0

        for record in data:
            if record[target_attr] in val_freq:
                val_freq[record[target_attr]] += 1.0
            else:
                val_freq[record[target_attr]] = 1.0

        for freq in val_freq:
            data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2)

        return data_entropy

    val_freq = {}
    subset_entropy = 0.0
    split_info = 0.0

    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]]  = 1.0

    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)
        split_info += -val_prob * math.log(val_prob)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set and divided by the split_info with respect to the target attribute (and return it)
    return (entropy(data, target_attr) - subset_entropy) / split_info

def CART_gain(data, attr, target_attr):
    """
    Gini index
    """
    def gini(data, target_attr):
        val_freq = {}
        gini_count = 0.0

        for record in data:
            if record[target_attr] in val_freq:
                val_freq[record[target_attr]] += 1.0
            else:
                val_freq[record[target_attr]] = 1.0

        for freq in val_freq:
            gini_count += (freq / sum(val_freq.values())) ** 2

        return (1-gini_count)

    val_freq = {}
    subset_gini = 0.0

    for record in data:
        if record[attr] in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]]  = 1.0

    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_gini += val_prob * gini(data_subset, target_attr)

    # Subtract the gini_count of the chosen attribute from the gini_count of the
    # whole data set with respect to the target attribute (and return it)
    return (gini(data, target_attr) - subset_gini)

def unique(lst):
    """
    Returns a list made up of the unique values found in lst.  i.e., it
    removes the redundant values in lst.
    """
    lst = lst[:]
    unique_lst = []

    # Cycle through the list and add each value to the unique list only once.
    for item in lst:
        if unique_lst.count(item) <= 0:
            unique_lst.append(item)

    # Return the list with all redundant values removed.
    return unique_lst

def majority_value(data, target_attr):
    lst = [record[target_attr] for record in data]
    highest_freq = 0
    most_freq = None

    for val in unique(lst):
        if lst.count(val) > highest_freq:
            most_freq = val
            highest_freq = lst.count(val)

    return most_freq

def choose_attribute(data, attributes, target_attr, fitness_func=ID3_gain):
    best = (-1e999999, None)
    for attr in attributes:
        if attr == target_attr:
            continue
        gain = fitness_func(data, attr, target_attr)
        best = max(best, (gain, attr))
    return best[1]

def get_values(data, attr):
    """
    Creates a list of values in the chosen attribut for each record in data,
    prunes out all of the redundant values, and return the list.
    """
    return unique([record[attr] for record in data])

def create_decision_tree(data, attributes, target_attr, fitness_func):
    """
    Returns a new decision tree based on the examples given.
    """
    data    = data[:]
    vals    = [record[target_attr] for record in data]
    default = majority_value(data, target_attr)

    # If the dataset is empty or the attributes list is empty, return the
    # default value. When checking the attributes list for emptiness, we
    # need to subtract 1 to account for the target attribute.
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute to best classify our data
        best = choose_attribute(data, attributes, target_attr,
                                fitness_func)

        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}

        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in get_values(data, best):
            # Create a subtree for the current value under the "best" field
            subtree = create_decision_tree(
                [r for r in data if r[best] == val],
                [attr for attr in attributes if attr != best],
                target_attr,
                fitness_func)

            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree

    return tree
