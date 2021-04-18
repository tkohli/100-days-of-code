 # Count Items Matching a Rule
"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""

def countMatches(items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        ruleArr = ["type", "color", "name"]
        count = 0
        for i in items:
            if (i[ruleArr.index(ruleKey)] == ruleValue):
                count += 1
        return count
        # count = 0
        # if ruleKey=='color':
        #     for i in range(len(items)):
        #         if items[i][1] == ruleValue:
        #             count +=1
        # if ruleKey=='type':
        #     for i in range(len(items)):
        #         if items[i][0] == ruleValue:
        #             count +=1
        # if ruleKey=='name':
        #     for i in range(len(items)):
        #         if items[i][2] == ruleValue:
        #             count +=1
        return count        
    