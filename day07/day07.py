#!/usr/bin/env python3

import re

class ContainingRule:
    exp = re.compile(r'(\d+) (.*) bag')

    def __init__(self, rule):
        m = ContainingRule.exp.match(rule.strip())
        self.count = m.group(1)
        self.type = m.group(2)

class BagRule:
    def __init__(self, rule):
        self.name, rest = rule.strip().split(" bags contain ")
        if rest == "no other bags.":
            self.contains = []
            return
        self.contains = [ContainingRule(x) for x in rest.split(",")]

rules = {}

with open('input.txt') as file:
    for rule in file.readlines():
        bag = BagRule(rule)
        for containingRule in bag.contains:
            if containingRule.type not in rules:
                rules[containingRule.type] = []
            rules[containingRule.type].append(bag)

open_list = ["shiny gold"]
results = []

while len(open_list) > 0:
    search = open_list.pop(0)
    if search not in results:
        results.append(search)
    if search in rules:
        for bag in rules[search]:
            open_list.append(bag.name)

print(len(results)-1)
    


