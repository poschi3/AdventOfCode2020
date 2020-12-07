#!/usr/bin/env python3

import re

class ContainingRule:
    exp = re.compile(r'(\d+) (.*) bag')

    def __init__(self, rule):
        m = ContainingRule.exp.match(rule.strip())
        self.count = int(m.group(1))
        self.type = m.group(2)
    
    def __repr__(self):
        return str(self.count) + " " + self.type

class BagRule:
    def __init__(self, rule):
        self.name, rest = rule.strip().split(" bags contain ")
        if rest == "no other bags.":
            self.contains = []
            return
        self.contains = [ContainingRule(x) for x in rest.split(",")]
    
    def __repr__(self):
        return self.name + ": " + str(self.contains)

contained_by_rules = {}
contains_rules = {}

with open('input.txt') as file:
    for rule in file.readlines():
        bag = BagRule(rule)
        contains_rules[bag.name] = bag
        for containingRule in bag.contains:
            if containingRule.type not in contained_by_rules:
                contained_by_rules[containingRule.type] = []
            contained_by_rules[containingRule.type].append(bag)

def can_contain():
    open_list = ["shiny gold"]
    results = []

    while len(open_list) > 0:
        search = open_list.pop(0)
        if search not in results:
            results.append(search)
        if search in contained_by_rules:
            for bag in contained_by_rules[search]:
                open_list.append(bag.name)
    return len(results)-1

def contains(bagname):
    sum = 1
    bag = contains_rules[bagname]
    for sub_bag in bag.contains:
        sum += sub_bag.count * contains(sub_bag.type)
    return sum

print(can_contain())
print(contains("shiny gold")-1)
