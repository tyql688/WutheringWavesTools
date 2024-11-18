from typing import Union


class WeaponAbstract(object):
    name = None
    id = None
    type = None

    def __init__(
            self,
            weapon_id: Union[str, int],
            weapon_level: int,
            weapon_breach: Union[int, None] = None,
            weapon_reson_level: Union[int, None] = 1
    ):
        self.weapon_id = weapon_id
        self.weapon_level = weapon_level
        self.weapon_breach = weapon_breach
        self.weapon_reson_level = weapon_reson_level
        self.weapon_detail: None

    def damage(self):
        """造成伤害"""
        pass

    def attack_damage(self):
        """造成普攻伤害"""
        pass

    def hit_damage(self):
        """造成重击伤害"""
        pass

    def skill_damage(self):
        """造成共鸣技能伤害"""
        pass

    def liberation_damage(self):
        """造成共鸣解放伤害"""
        pass

    def cast_attack(self):
        """施放普攻"""
        pass

    def cast_hit(self):
        """施放重击"""
        pass

    def cast_skill(self):
        """施放共鸣技能"""
        pass

    def cast_liberation(self):
        """施放共鸣解放"""
        pass

    def cast_dodge_counter(self):
        """施放闪避反击"""
        pass

    def cast_variation(self):
        """施放变奏技能"""
        pass

    def skill_create_healing(self):
        """共鸣技能造成治疗"""
        pass
