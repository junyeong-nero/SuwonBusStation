import pandas as pd
import json
import json5
import domain.station as st
import domain.grid as sq
import domain.building as sb

stations = []


def print_stations():
    global stations
    for station in stations:
        print(station)


def extract_bus():
    arr = []
    db = pd.read_csv('data/1.수원시_버스정류장.csv')
    for index, row in db.iterrows():
        s = st.Station(station_id=row["정류장ID"],
                       name=row["정류장명"],
                       lon=row['lon'],
                       lat=row['lat'])
        arr.append(s)
    return arr


def extract_people(path):
    f = open(path, mode='rt', encoding='utf-8')
    old = json.loads(f.read())
    old_features = old['features']  # list
    res = []
    for grid in old_features:
        p = sq.Grid(grid['geometry']['coordinates'][0][0])
        p.value = grid['properties']['val']
        p.gid = grid['properties']['gid']
        if p.value is not None:
            res.append(p)
    return res


def extract_building(types):
    res = []
    f = open('data/27.수원시_도로명주소(건물).geojson', mode='rt', encoding='utf-8')
    old = json.loads(f.read())
    old_features = old['features']  # list
    for grid in old_features:
        building_type = grid['properties']['BDTYP_CD']
        if building_type in types:
            res.append(sb.Building(building_name=grid['properties']['BULD_NM'],
                                   building_type=building_type,
                                   coord=grid['geometry']['coordinates'][0][0]))
    return res
