class EchoAbstract(object):
    name = None
    id = None

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
