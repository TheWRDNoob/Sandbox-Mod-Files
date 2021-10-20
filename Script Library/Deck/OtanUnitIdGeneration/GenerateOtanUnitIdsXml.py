"""
This is a simple Python script to help write the OtanUnitIds xml file. It expects a text file with all the ClassNameForDebug strings for every unit, which you can get by using powercrystals' Table Exporter.
"""

import pandas as pd

total_string = ''
df = pd.read_csv('TUniteDescriptor.csv')
last_idx=0
for idx, unit in enumerate(df['ClassNameForDebug']):
    if unit.startswith('Building_'):
        last_idx+=1
        total_string += f"""\
            <change property="OtanUnitIds" operation="append" type="map">
                <map>
                    <key type="UInt32">{idx+1}</key>
                    <value type="ObjectReference">
                        <reference table="TUniteDescriptor">
                            <matchconditions>
                                <matchcondition type="property" property="ClassNameForDebug">{unit}</matchcondition>
                            </matchconditions>
                        </reference>
                    </value>
                </map>
            </change>\n"""
df = pd.read_csv('TUniteAuSolDescriptor.csv')
for idx, unit in enumerate(df['ClassNameForDebug'], last_idx):
    total_string += f"""\
            <change property="OtanUnitIds" operation="append" type="map">
                <map>
                    <key type="UInt32">{idx+1}</key>
                    <value type="ObjectReference">
                        <reference table="TUniteAuSolDescriptor">
                            <matchconditions>
                                <matchcondition type="property" property="ClassNameForDebug">{unit}</matchcondition>
                            </matchconditions>
                        </reference>
                    </value>
                </map>
            </change>\n"""

with open('OtanUnitIdChanges.txt', 'w+') as out:
    out.write(total_string)
