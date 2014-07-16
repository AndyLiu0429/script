#encoding = utf-8
"""
example of naive-bayes
"""
from numpy import *
def localDataSet():
    postingList = [], # define word lists here
    classVec = [],
    return postingList, classVec

def createVocaList(dataset):
    vocaSet = set([])
    for document in dataset:
        vocaSet = vocaSet | set(document)
    return list(vocaSet)

def setofWords2Vec(vocalList, inputSet):
    returnVec = [0] * len(vocalList)
    for word in inputSet:
        if word in vocalList:
            returnVec[vocalList.index(word)] = 1
        else:
            pass
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = len(trainMatrix[0]); p1Denom = len(trainMatrix[0])
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classify(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0