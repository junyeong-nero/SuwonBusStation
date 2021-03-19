from pyproj import Transformer

transformer_5186_4326 = Transformer.from_proj(5186, 4326)
transformer_4326_5168 = Transformer.from_proj(4326, 5186)


def meter2lonlat(x, y):
    return transformer_5186_4326.transform(x, y)


def lonlat2meet(x, y):
    return transformer_4326_5168.transform(x, y)
