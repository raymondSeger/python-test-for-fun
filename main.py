from string import Template

# Coordinates: 37.24N, -115.81W
print( 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W') )

#a, b, c
print( '{0}, {1}, {2}'.format('a', 'b', 'c') )

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}

print(*coord) #latitude longitude

print( 'Coordinates: {latitude}, {longitude}'.format(**coord) )


s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao')) #tim likes kung pao