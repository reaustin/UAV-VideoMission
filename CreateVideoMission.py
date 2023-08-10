#### creates a video mission (kml) for Matrise 300 RTK
import os, sys, shutil
import csv 
from template_func import *

### Set the file that conatins the coordinates and the output file name for the kmz
### - flight altitude is provided in feet
_coord_file = './files/WaypointsSandhillsTurf.csv'
_out_file_name = 'WaypointSandhillsTurf'
_flight_altitude = 20

### check for a folder called export, create it if it does not exsist 
###  - this is where the ./wpmz/template.kml file gets created 
_folder_base = './export/'
if not os.path.exists(os.path.join(_folder_base, 'wpmz')):
    os.makedirs(os.path.join(_folder_base, 'wpmz'))

### set the output file name with the directory path, as well as the template.kml file
_out_file = os.path.join(_folder_base, _out_file_name + '_' + str(_flight_altitude) + 'ft')
_out_template = os.path.join(_folder_base, 'wpmz/template.kml')

#### read the coordiates into a dictionary 
def read_coords(_coord_file):
    _dict = {}
    i = 0
    with open(_coord_file, mode='r') as csv_file:
        _csv_reader = csv.DictReader(csv_file)
        for r in _csv_reader:
            _dict[i] = r
            i = i+1
    return _dict

#### a simple function to write opening or closing tags
def writeline(out, strToWrite):
    out.write(strToWrite + '\n')


############# ---- MAIN ---- ###############
_csv_data = read_coords(_coord_file)


### clean up the ./export/ folder location
if os.path.isfile(_out_template):
    os.remove(_out_template)


### create a 'template file' 
template = open(_out_template, "w")

### write out the template file
write_header(template)
writeline(template,'  <Document>')
template_missionConfig(template)
writeline(template,'  <Folder>')
template_header(template, _flight_altitude)
template_placemarks(template, _csv_data)
template_payloadParam(template)
write_footer(template)

template.close()

### zip up the folder
if os.path.isfile(_out_file + '.zip'):
    os.remove(_out_file + '.zip')
if os.path.isfile(_out_file + '.kmz'):
    os.remove(_out_file + '.kmz')

### rename zip to kmz
shutil.make_archive(_out_file, 'zip', _folder_base)
os.rename(_out_file + '.zip', _out_file + ".kmz")

sys.exit()
