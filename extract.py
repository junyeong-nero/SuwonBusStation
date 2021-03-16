import pandas as pd
import json
import domain.station as st
import domain.square as sq

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


def extract_people():
    f = open('data/17.수원시_인구정보(고령)_격자.geojson', mode='rt', encoding='utf-8')
    old = json.loads(f.read())
    old_features = old['features']  # list
    res = []
    for grid in old_features:
        p = sq.Square(grid['geometry']['coordinates'][0][0])
        p.size = grid['properties']['val']
        p.gid = grid['properties']['gid']
        if p.size is not None:
            res.append(p)
    return res


def extract_building():
    f = open('data/27.수원시_도로명주소(건물).geojson', mode='rt', encoding='utf-8')
    old = json.loads(f.read())
    old_features = old['features']  # list
    for grid in old_features:
        building_type = grid['properties']['BDTYP_CD']
        if building_type == '13000' or building_type == '13100' or building_type == '13200':
            print(grid['properties']['BULD_NM'])


def main():

    extract_building()
    # print_stations()
    extract_people()


if __name__ == '__main__':
    main()
