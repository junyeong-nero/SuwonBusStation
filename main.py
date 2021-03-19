import json5
import webbrowser
import folium
import pandas as pd
import extract


def draw_tile(center, zoom):
    return folium.Map(location=center,
                      zoom_start=zoom,
                      tiles='http://api.vworld.kr/req/wmts/1.0.0/DD1F3DD2-D6D7-383A-A9F2-B8743FA78E4D/Base/{z}/{y}/{x}.png',
                      attr='수원시'
                      )


def draw_station(_map, station):
    # print("draw_station : {}".format(station))
    folium.Circle(location=station.coord,
                  radius=5,
                  color="#1e88e5",
                  fill_color="#1e88e5",
                  popup=station.__dict__).add_to(_map)


def draw_csv(_map, path, name="csv"):
    # 수원시 체육시설 현황 정보
    db = pd.read_csv(path)
    print(db.head())
    for index, row in db.iterrows():
        folium.Marker([row['lon'], row['lat']],
                      name=name,
                      popup=row['광고물종류'],
                      icon=folium.Icon(icon='blue')).add_to(_map)


def draw_geojson(_map, path, name="geojson"):
    with open(path, mode='rt', encoding='utf-8') as f:
        db = json5.loads(f.read())
        f.close()
    # print(db)
    folium.GeoJson(data=db,
                   name=name).add_to(_map)


def draw_multipolygon(_map, poly, pop="", color="#FF6347"):
    folium.Polygon(locations=poly,
                   color=color,
                   fill_color=color,
                   popup=pop).add_to(_map)


def open_map(_map):
    _map.save("result.html")
    webbrowser.open("result.html", new=2)


def main():
    center = (37.27879484307593, 127.00181693369032)
    zoom = 15
    geomap = draw_tile(center, zoom)
    # drawCsvFile(geomap, 'data/10.수원시_옥외광고물현황.csv', "수원시 옥외광고물현황")
    # draw_geojson(geomap, 'data/30.수원시_법정경계(읍면동).geojson', "법정경계")
    # draw_geojson(geomap, 'data/29.수원시_법정경계(시군구).geojson', "지적도")

    stations = extract.extract_bus()

    # 의료시설들
    medical_types = ['07000', '07101', '07102', '07103', '07104', '07105', '07106', '07107', '07999']
    medical_buildings = extract.extract_building(medical_types)
    for building in medical_buildings:
        # print(building.name)
        # draw_multipolygon(_map=geomap,
        #                   poly=building.coord,
        #                   pop=building.name,
        #                   color="#4caf50")  # green
        folium.Circle(location=building.coord[0],
                      radius=100,  # 100m 짜리 원
                      color="#4caf50",
                      fill_color="#4caf50").add_to(geomap)

        for station in stations:
            if building.into(station, 100):  # building의 100미터 안에 정거장이 있다면 10점 추가
                station.point += 10

    # 공장들
    factory_types = ['13000', '13100', '13200']
    factory_buildings = extract.extract_building(factory_types)
    for building in factory_buildings:
        # print(building.name)
        draw_multipolygon(_map=geomap,
                          poly=building.coord,
                          pop=building.name)  # red

    # 학교, 학원, 도서관
    study_types = ['08003', '08005', '08101', '08102', '08103', '08104', '08105', '08106']
    study_buildings = extract.extract_building(study_types)
    for building in study_buildings:
        print(building.name)
        draw_multipolygon(_map=geomap,
                          poly=building.coord,
                          pop=building.name,
                          color="#ffeb3b")  # yellow

    # # 인구정보 그리기
    # old = extract.extract_people('data/17.수원시_인구정보(고령)_격자.geojson')
    # working = extract.extract_people('data/18.수원시_인구정보(생산가능)_격자.geojson')
    # teenager = extract.extract_people('data/19.수원시_인구정보(유소년)_격자.geojson')
    # for s in stations:
    #     for p in old:
    #         if p.into(s):
    #             s.people_old += p.value
    #             draw_multipolygon(_map=geomap,
    #                               poly=p.coord,
    #                               pop=p.gid,
    #                               color="#78909c")
    #             break
    #
    #     for p in working:
    #         if p.into(s):
    #             s.people_work += p.value
    #             draw_multipolygon(_map=geomap,
    #                               poly=p.coord,
    #                               pop=p.gid,
    #                               color="#78909c")
    #             break
    #
    #     for p in teenager:
    #         if p.into(s):
    #             s.people_teen += p.value
    #             draw_multipolygon(_map=geomap,
    #                               poly=p.coord,
    #                               pop=p.gid,
    #
    #                               color="#78909c")
    #             break

    for s in stations:
        draw_station(geomap, s)

    open_map(geomap)


if __name__ == '__main__':
    main()
