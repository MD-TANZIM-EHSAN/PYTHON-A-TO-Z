#TUPLE()- immutable

masala_spices = ("cardamom","colves","cinnamon")
(spice1,spice2,spice3)=masala_spices
print(spice1)
print(spice2)
print(spice3)

ginger_ratio,cardamom =2,1
print(ginger_ratio,":",cardamom)
ginger_ratio,cardamom=cardamom,ginger_ratio
print(ginger_ratio,cardamom)

#memebership
print(f"IS ginger available ? {"ginger" in masala_spices }")
print(f"IS cinnamon available ? {"cinnamon" in masala_spices }")
