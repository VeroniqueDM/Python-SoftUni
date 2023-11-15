from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):

    def test_instance_attributes(self):
        hero = Hero('ivanqza', 80, 100, 25)
        self.assertEqual('ivanqza', hero.username)
        self.assertEqual(80, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(25, hero.damage)

    def test_raise_when_hero_fights_himself(self):
        hero = Hero('ivanqza', 80, 100, 25)
        with self.assertRaises(Exception) as ex:
            hero.battle(hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))


    def test_raise_when_hero_fights_without_health(self):
        hero = Hero('ivanqza', 80, 0, 25)
        enemy_hero = Hero('cepeto', 70, 90, 15)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_raise_when_hero_fights_with_negative_health(self):
        hero = Hero('ivanqza', 80, -1, 25)
        enemy_hero = Hero('cepeto', 70, 90, 15)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))


    def test_raise_exception_when_hero_fights_enemy_without_health(self):
        hero = Hero('ivanqza', 80, 100, 25)
        enemy_hero = Hero('cepeto', 70, 0, 15)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight cepeto. He needs to rest", str(ex.exception))


    def test_attr_decrease_at_battle_loss(self):
        hero = Hero('ivanqza', 5, 100, 12)
        enemy_hero = Hero('cepeto', 3, 90, 10)
        self.assertEqual("You lose", hero.battle(enemy_hero))
        self.assertEqual(70, hero.health)
        self.assertEqual(35, enemy_hero.health)
        self.assertEqual(4,enemy_hero.level)
        self.assertEqual(15, enemy_hero.damage)

    def test_attr_decrease_at_battle_win(self):
        hero = Hero('ivanqza', 5, 100, 20)
        enemy_hero = Hero('cepeto', 3, 90, 10)
        self.assertEqual("You win", hero.battle(enemy_hero))

        self.assertEqual(75, hero.health)
        self.assertEqual(6, hero.level)
        self.assertEqual(25, hero.damage)
        self.assertEqual(-10, enemy_hero.health)



    def test_battle_ends_in_draw(self):
        hero = Hero('ivanqza', 10, 100, 12)
        enemy_hero = Hero('cepeto', 11, 90, 10)
        self.assertEqual( 'Draw', hero.battle(enemy_hero))



    def test_string_method(self):
        hero = Hero('ivanqza', 10, 100, 12)
        self.assertEqual(
            f"Hero ivanqza: 10 lvl\nHealth: 100\nDamage: 12\n",
            str(hero)
        )



if __name__ == "__main__":
    main()