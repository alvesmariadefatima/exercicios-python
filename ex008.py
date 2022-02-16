medida = float(input('Uma distância em quilômetros: '))
medida = float(input('Uma distância em hectômetro: '))
medida = float(input('Uma distância em decâmetro: '))
medida = float(input('Uma distância em metros: '))
medida = float(input('Uma distância em decímetros: '))
medida = float(input('Uma distância em centímetros: '))
medida = float(input('Uma distância em milímetros: '))
km = medida * 10
hm = medida * 10
dam = medida * 10
m = medida * 10
dm = medida * 10
cm = medida * 10
mm = medida *100

print('A medida de {} km corresponde a {} hm e {} dam'.format(medida, km, hm,dam))
print('A medida de {}m corresponde a {:.1f} cm e {:.1f} mm'.format(medida, cm, mm))
