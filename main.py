import json
import geopandas
from IPython.core.display import display, HTML
import folium
import webbrowser
import pandas as pd


def drawMapTile(center, zoom):
    return folium.Map(location=center,
                      zoom_start=zoom,
                      tiles='http://api.vworld.kr/req/wmts/1.0.0/DD1F3DD2-D6D7-383A-A9F2-B8743FA78E4D/Base/{z}/{y}/{x}.png',
                      attr='수원시'
                      )


def drawCsvFile(_map, path, name="csv"):
    # 수원시 체육시설 현황 정보
    db = pd.read_csv(path)
    print(db.head())
    folium.Cir
    for index, row in db.iterrows():
        folium.Marker([row['lon'], row['lat']],
                      name=name,
                      popup=row['광고물종류'],
                      icon=folium.Icon(icon='blue')).add_to(_map)


def drawGeoJsonFile(_map, path, name="geojson"):
    with open(path, mode='rt', encoding='utf-8') as f:
        db = json.loads(f.read())
        f.close()
    # print(db)
    folium.GeoJson(data=db,
                   name=name
                   ).add_to(_map)


def openMap(_map):
    _map.save("result.html")
    webbrowser.open("result.html", new=2)


def main():
    center = (37.27879484307593, 127.00181693369032)
    zoom = 13
    geomap = drawMapTile(center, zoom)
    # drawCsvFile(geomap, 'data/10.수원시_옥외광고물현황.csv', "수원시 옥외광고물현황")
    # drawGeoJsonFile(geomap, 'data/30.수원시_법정경계(읍면동).geojson', "법정경계")
    drawGeoJsonFile(geomap, 'data/29.수원시_법정경계(시군구).geojson', "지적도")
    openMap(geomap)


if __name__ == '__main__':
    main()
