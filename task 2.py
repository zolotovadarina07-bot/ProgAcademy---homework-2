floors = 9
apts_per_floor = 4
entrances = 4
apts_per_entrances = floors * apts_per_floor
total_apts = entrances * apts_per_entrances
flat = int(input('Enter a flat number: '))
if flat < 1 or flat > total_apts:
    print('Flat number is out of range')
else:
    entrance = (flat - 1) // apts_per_entrances + 1
    flat_number = (flat - 1) % apts_per_entrances
    floor = (flat_number // apts_per_floor) + 1
    print('Flat number:', flat,', in', entrance,'entrance',', on', floor, 'floor.')


