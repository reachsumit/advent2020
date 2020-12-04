required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def day4q1(passports):
    answer = 0
    for passport in passports:
        present_keys = set()
        for pair in passport.split():
            present_keys.add(pair.split(":")[0])
        if required_fields.issubset(present_keys):
            answer += 1
    return answer


def day4q2(passports):
    answer = 0
    for passport in passports:
        present_keys = set()
        passed_validation = True
        for pair in passport.split():
            k, v = pair.split(":")
            present_keys.add(k)
            if k == 'byr' and (len(v) != 4 or int(v) < 1920 or int(v) > 2002):
                passed_validation = False
                break
            if k == 'iyr' and (len(v) != 4 or int(v) < 2010 or int(v) > 2020):
                passed_validation = False
                break
            if k == 'eyr' and (len(v) != 4 or int(v) < 2020 or int(v) > 2030):
                passed_validation = False
                break
            if k == 'hgt' and (v[-2:] not in ['cm', 'in']) or ((v.endswith('cm') and (int(v[:-2]) < 150 or int(v[:-2]) > 193)) or (v.endswith('in') and (int(v[:-2]) < 59 or int(v[:-2]) > 76))):
                passed_validation = False
                break
            if k == 'hcl' and (len(v) != 7 or v[0] != '#' or not set('0123456789abcdef').issuperset(v[1:])):
                passed_validation = False
                break
            if k == 'ecl' and v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                passed_validation = False
                break
            if k == 'pid' and (len(v) != 9 or not v.isdigit()):
                passed_validation = False
                break

        if passed_validation and required_fields.issubset(present_keys):
            answer += 1
    return answer


with open('input.txt') as thefile:
    content = thefile.read()
all_passports = content.split("\n\n")

print(day4q1(all_passports))
print(day4q2(all_passports))
