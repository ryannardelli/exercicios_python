metro = int(input('Uma distância em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f"""A medida {metro}m corresponde a
{km}km
{hm}hm
{dam}dam
{dm}dm
{cm}cm
{mm}mm
""")