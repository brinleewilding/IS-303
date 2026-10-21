from fortnitebot import ForniteBot

bot1 = ForniteBot()
bot2 = ForniteBot()
bot3 = ForniteBot()


bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.health)
print(bot2.health)
print(bot3.health)

