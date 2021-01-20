import folium

with open('data.txt') as file:
    gpsData = str(file.read()).split('\n')


maindict = {}
lat = []
long = []
count = []

lnum = 0
for line in gpsData:
    
    if 'latitude' not in str(line) and line != '':
        line = line.split(',')
        
            
        
        
        if int(line[2]) > 0:
            maindict[lnum] = float(line[0]), float(line[1]), int(line[2])
            lat.append(float(line[0]))
            long.append(float(line[1]))
            count.append(int(line[2]))
    lnum += 1

# Dictionary is my approach. Slightly more effecient.




m = folium.Map(location=[float(lat[0]), float(long[0])])

for i in maindict:
    f = maindict[i]
    folium.Marker([float(f[0]), float(f[1])], popup='{} pieces of litter detected.'.format(f[2])).add_to(m)
    print('Marker {} has been added to the map'.format(i))

#for i in range(len(lat)):
#    folium.Marker([float(lat[i]),float(long[i])],popup='{} pieces of litter detected'.format(count[i]))

m.save('data.html')
