#encoding = utf-8
"""
example of d-tree
"""
from math import log
import operator
import matplotlib.pyplot as plt


def cal_entropy(dataset):
    labelCounts = {}
    for feat in dataset:
        if feat[-1] not in labelCounts:
            labelCounts[feat[-1]] = 1.0
        else:
            labelCounts[feat[-1]] += 1.0
    entropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / len(dataset)
        entropy += -prob * log(prob, 2)
    return entropy

def split_dataset(dataset, axis, value):
        retData = []
        for feat in dataset:
            if feat[axis] == value:
                reduced = feat[:axis]
                reduced.extend(feat[axis+1:])
                retData.append(reduced)
        return retData

def chooseBest(dataset):
    numFeats = len(dataset[0]) - 1
    baseEntropy = cal_entropy(dataset)
    bestInfo = 0.0; bestFeat = -1
    for i in range(numFeats):
        featList = [example[i] for example in dataset]
        uniqVals = set(featList)
        newEntropy = 0.0
        for value in uniqVals:
            subSet = split_dataset(dataset, i, value)
            prob = len(subSet) / float(len(dataset))
            newEntropy += prob * cal_entropy(subSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfo:
            infoGain = bestInfo
            bestFeat = i
    return bestFeat

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount:
            classCount[vote] = 1.0
        else:
            classCount[vote] += 1.0
    sortedclassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
    return sortedclassCount[0][0]

def createTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if len(set(classList)) == 1:
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBest(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel : {}}
    del labels[bestFeat]
    featValues = [example[bestFeat] for example in dataset]
    uniqVals = set(featValues)
    for val in uniqVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][val] = createTree(split_dataset(dataset, bestFeat, val), subLabels)
    return myTree

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    pass



