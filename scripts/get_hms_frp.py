import geopandas
import pytz
from datetime import datetime
import os
import shutil
import wget

def get_frp_fn_url(dt):
    tt = dt.timetuple()
    month = str(tt.tm_mon).zfill(2)
    day = str(tt.tm_mday).zfill(2)
    yr = str(tt.tm_year)
    fn = 'hms_fire{}{}{}.zip'.format(yr, month, day)
    url = 'https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Fire_Points/Shapefile/{}/{}/{}'.format(yr, month, fn)
    return fn, url

def get_frp(dt, frp_dir):
    fn, url = get_frp_fn_url(dt)
    frp_shape_fn = frp_dir + fn
    print(frp_shape_fn)
    if os.path.exists(frp_shape_fn):
        print("{} already exists".format(fn))
    else:
        print('DOWNLOADING frp: {}'.format(fn))
        filename = wget.download(url, out=frp_dir)
        shutil.unpack_archive(filename, frp_dir)
    frp = geopandas.read_file(frp_shape_fn)
    return frp
dt_str = '2023/04/04 14:50'
dt = pytz.utc.localize(datetime.strptime(dt_str, '%Y/%m/%d %H:%M'))
print(dt)
get_frp(dt, "/home/rey/projects/GOES_FRP/frp_shapefiles/")
