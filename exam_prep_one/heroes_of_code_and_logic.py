n = int(input())
heroes_party = {}
for z in range (0,n):
    new_hero = input().split()
    name = new_hero[0]
    hp = int(new_hero[1])
    mp = int(new_hero[2])
    if name not in heroes_party:
        heroes_party[name] = {"HP":hp, "MP":mp}

def hero_action(command, party:dict):
    action = command.split(" - ")
    activity = action[0]
    hero = action[1]
    power = int(action[2])
    if len(action) == 4:
        spell_or_attacker_name = action[3]
    if activity == "CastSpell":
        if  party[hero]["MP"] >= power:
            party[hero]["MP"] -= power
            new_mp = party[hero]["MP"]
            return f"{hero} has successfully cast {spell_or_attacker_name} and now has {new_mp} MP!"
        else:
            return f"{hero} does not have enough MP to cast {spell_or_attacker_name}!"
    elif activity == "TakeDamage":
        party[hero]["HP"] -= power
        if party[hero]["HP"] <= 0:
            del party[hero]
            return f"{hero} has been killed by {spell_or_attacker_name}!"
        else:
            new_hp =party[hero]["HP"]
            return f"{hero} was hit for {power} HP by {spell_or_attacker_name} and now has {new_hp} HP left!"
    elif activity == "Recharge":
        if party[hero]["MP"] + power > 200:
            power = 200 - party[hero]["MP"]
            party[hero]["MP"] = 200
        else:
            party[hero]["MP"] += power
        return f"{hero} recharged for {power} MP!"
    elif activity == "Heal":
        if party[hero]["HP"] + power > 100:
            power = 100 - party[hero]["HP"]
            party[hero]["HP"] = 100
        else:
            party[hero]["HP"] += power
        return f"{hero} healed for {power} HP!"

command = input()
while command != "End":
    result = hero_action(command, heroes_party)
    print(result)
    command = input()
dict_name_hp = {}
for k,v in heroes_party.items():
    if k not in dict_name_hp:
        dict_name_hp[k] = heroes_party[k]["HP"]
sorted_party = dict(sorted(dict_name_hp.items(), key=lambda kv:(-kv[1], kv[0])))
for k,v in sorted_party.items():
    print(k)
    hp = sorted_party[k]
    mp= heroes_party[k]["MP"]
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")