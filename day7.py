import re
q1_dict = {}
q2_dict = {}
q2_answer = 0
those_who_contain = set()
those_who_dont_contain = set()


def populate_q1_dictionary(rules):
    matching_pattern_main_bag = "([ a-z]+) bags contain"
    matching_pattern_other_bags = "([0-9]+) ([ a-z]+) bag"
    for rule in rules:
        main_bag = re.findall(matching_pattern_main_bag, rule)
        other_bags = re.findall(matching_pattern_other_bags, rule)
        if not other_bags:
            q1_dict[main_bag[0]] = None
            continue
        q1_dict[main_bag[0]] = {}
        for other in other_bags:
            q1_dict[main_bag[0]][other[1]] = int(other[0])


def contains_target(this_color, target_color='shiny gold'):
    if this_color in those_who_contain:
        return True
    elif this_color in those_who_dont_contain:
        return False
    elif not q1_dict[this_color]:
        return False
    elif target_color in q1_dict[this_color]:
        return True
    for color, count in q1_dict[this_color].items():
        if contains_target(color):
            return True


def day7q1(target_color='shiny gold'):
    answer = 0
    for main, others in q1_dict.items():
        if contains_target(main):
            answer += 1
            those_who_contain.add(main)
            continue
        if not others:
            those_who_dont_contain.add(main)
            continue
        for color, count in others.items():
            if contains_target(color):
                answer += 1
                those_who_contain.add(color)
                those_who_contain.add(main)
                continue
            else:
                those_who_dont_contain.add(color)
        those_who_dont_contain.add(main)


def day7q2(current_color='shiny gold', current_count=0):
    if not q1_dict[current_color]:
        return current_count
    new_count = 0
    for color, count in q1_dict[current_color].items():
        new_count += day7q2(color, count)
    q2_dict[current_color] = current_count + (current_count * new_count)
    return q2_dict[current_color]


all_rules = [line.rstrip('\n') for line in open('input.txt')]
populate_q1_dictionary(all_rules)
day7q1()
# Print Q1 answer
print(len(those_who_contain))

day7q2()
q2_answer = 0
for color, _ in q1_dict['shiny gold'].items():
    q2_answer += q2_dict[color]
# Print Q2 answer
print(q2_answer)
