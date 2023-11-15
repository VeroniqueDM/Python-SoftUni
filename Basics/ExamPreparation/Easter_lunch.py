kozunak_count = int(input())
egg_packs = int(input())
cookies_kg = int(input())
kozunak_price = kozunak_count * 3.20
eggs_price = egg_packs * 4.35
cookies_price = cookies_kg * 5.40
egg_dye = egg_packs * 12 * 0.15
total_expences = kozunak_price +eggs_price + cookies_price + egg_dye
print(f"{total_expences:.2f}")