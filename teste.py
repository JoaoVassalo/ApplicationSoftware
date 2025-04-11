import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

# Criar a figura e os eixos
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Mercator()})
ax.set_extent([-60, -30, -40, 0], crs=ccrs.PlateCarree())

# Adicionar feições geográficas
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='-')
ax.add_feature(cfeature.STATES, linestyle=':')

# Criar dados fictícios de vento
lon = np.linspace(-60, -30, 10)
lat = np.linspace(-40, 0, 10)
lons, lats = np.meshgrid(lon, lat)
u = np.sin(lats * np.pi / 180)  # Componente u do vento
v = np.cos(lons * np.pi / 180)  # Componente v do vento

# Plotar vetores
ax.quiver(lons, lats, u, v, transform=ccrs.PlateCarree(), scale=30)

# Adicionar título e rótulos dos eixos
ax.set_xlabel('Longitude', fontsize=10, labelpad=10)
ax.set_ylabel('Latitude', fontsize=10, labelpad=10)
ax.set_title('Exemplo de Mapa com Vetores', fontsize=12)

# Mostrar o gráfico
plt.show()