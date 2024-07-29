import math


def get_distance_from_lat_lon_in_m(lat1, lon1, lat2, lon2):
    def deg2rad(deg):
        return deg * (math.pi / 180)

    R = 6371000  # 지구 반지름 (단위: m)
    dLat = deg2rad(lat2 - lat1)
    dLon = deg2rad(lon2 - lon1)
    a = (
            math.sin(dLat / 2) * math.sin(dLat / 2) +
            math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) *
            math.sin(dLon / 2) * math.sin(dLon / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # 거리 (단위: m)
    return d
