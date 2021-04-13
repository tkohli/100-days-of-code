# Min Rewards
"""
Given list of int let us call it scores of student in an exam , we have to give student rewards such that,
1. Every student should have at least one reward
2. Given student who has higher score than its next student should have more rewards and visa versa

eg. [8, 4, 2, 1, 3, 6, 7, 9, 5]
rew [4, 3, 2, 1, 2, 3, 4, 5, 1]
min rewards = 25(Ans)
"""


# O(n^2) Time complexity | O(n) Space Complexity
def minRewardsNaive(scores):
    """ We take a nested loop then see that which value is lower then assign it min rewards
        and next one nim + 1, if we go to next element then we have to change the rewards of all the previous
        possible elements"""
    rewards = [1 for _ in scores]
    for i in range(len(scores)):
        j = i-1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j]+1
        else:
            while j>= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j],rewards[j+1]+1)
                j-=1
    return sum(rewards)


# O(n) Time complexity | O(n) Space Complexity
def minRewardsBetter(scores):
    """ For a better solution we find local min points the iterate to loop and go to its left and right side
        this is just a better solution but gets tricky on its edge cases"""
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx,scores,rewards)
    return sum(rewards)


def expandFromLocalMinIdx(localMinIdx,scores,rewards):
    leftIdx = localMinIdx - 1
    while leftIdx>=0 and scores[leftIdx]>scores[leftIdx+1]:
        rewards[leftIdx] = max(rewards[leftIdx],rewards[leftIdx+1]+1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = rewards[rightIdx - 1] + 1
        rightIdx += 1


def getLocalMinIdxs(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i==0 and array[i]<array[i+1]:
            localMinIdxs.append(i)
        if i==len(array)-1 and array[i]<array[i-1]:
            localMinIdxs.append(i)
        if i==0 or i==len(array)-1:
            continue
        if array[i]<array[i+1] and array[i]<array[i-1]:
            localMinIdxs.append(i)
    return localMinIdxs


# O(n) Time complexity | O(n) Space Complexity
def minRewardsBest(scores):
    """ For best solution we once move right to array and check the conditions
        then goto left and check conditions, we take 2 individual loops
        It is a very easy to understand approach"""
    rewards = [1 for _ in scores]
    for i in range(len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i],rewards[i + 1] + 1)
    return sum(rewards)


print(minRewardsNaive([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(minRewardsBetter([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(minRewardsBest([8, 4, 2, 1, 3, 6, 7, 9, 5]))