
def write_header(out):
    out.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    out.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:wpml=\"http://www.dji.com/wpmz/1.0.3\">\n")


def template_missionConfig(out):
    out.write("  <wpml:createTime>1689275209252</wpml:createTime>\n")
    out.write("  <wpml:updateTime>1689275578182</wpml:updateTime>\n")
    out.write("  <wpml:missionConfig>\n")
    out.write("   <wpml:flyToWaylineMode>safely</wpml:flyToWaylineMode>\n")
    out.write("   <wpml:finishAction>goHome</wpml:finishAction>\n")
    out.write("   <wpml:exitOnRCLost>executeLostAction</wpml:exitOnRCLost>\n")
    out.write("   <wpml:executeRCLostAction>goBack</wpml:executeRCLostAction>\n")
    out.write("   <wpml:takeOffSecurityHeight>15.2401847839355</wpml:takeOffSecurityHeight>\n")
    out.write("   <wpml:globalTransitionalSpeed>15</wpml:globalTransitionalSpeed>\n")
    out.write("   <wpml:droneInfo>\n")
    out.write("    <wpml:droneEnumValue>60</wpml:droneEnumValue>\n")
    out.write("    <wpml:droneSubEnumValue>0</wpml:droneSubEnumValue>\n")
    out.write("   </wpml:droneInfo>\n")
    out.write("   <wpml:payloadInfo>\n")
    out.write("    <wpml:payloadEnumValue>50</wpml:payloadEnumValue>\n")
    out.write("    <wpml:payloadSubEnumValue>0</wpml:payloadSubEnumValue>\n")
    out.write("    <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("   </wpml:payloadInfo>\n")
    out.write("  </wpml:missionConfig>\n")


def template_header(out, flight_altitude):
    out.write("    <wpml:templateType>waypoint</wpml:templateType>\n")
    out.write("    <wpml:templateId>0</wpml:templateId>\n")
    out.write("    <wpml:waylineCoordinateSysParam>\n")
    out.write("      <wpml:coordinateMode>WGS84</wpml:coordinateMode>\n")
    out.write("      <wpml:heightMode>relativeToStartPoint</wpml:heightMode>\n")
    out.write("      <wpml:positioningType>GPS</wpml:positioningType>\n")
    out.write("    </wpml:waylineCoordinateSysParam>\n")
    out.write("    <wpml:autoFlightSpeed>5</wpml:autoFlightSpeed>\n")
    out.write("    <wpml:globalHeight>" + str(flight_altitude/3.28) + " </wpml:globalHeight>\n")
    out.write("    <wpml:caliFlightEnable>0</wpml:caliFlightEnable>\n")
    out.write("    <wpml:gimbalPitchMode>usePointSetting</wpml:gimbalPitchMode>\n")
    out.write("    <wpml:globalWaypointHeadingParam>\n")
    out.write("      <wpml:waypointHeadingMode>manually</wpml:waypointHeadingMode>\n")
    out.write("      <wpml:waypointHeadingAngle>0</wpml:waypointHeadingAngle>\n")
    out.write("      <wpml:waypointPoiPoint>0.000000,0.000000,0.000000</wpml:waypointPoiPoint>\n")
    out.write("      <wpml:waypointHeadingPoiIndex>0</wpml:waypointHeadingPoiIndex>\n")
    out.write("    </wpml:globalWaypointHeadingParam>\n")
    out.write("    <wpml:globalWaypointTurnMode>toPointAndStopWithDiscontinuityCurvature</wpml:globalWaypointTurnMode>\n")
    out.write("    <wpml:globalUseStraightLine>1</wpml:globalUseStraightLine>\n")



def template_actiongroup(out, groupId, startIndex, endIndex, action):
    out.write("        <wpml:actionGroup>\n")
    out.write("          <wpml:actionGroupId>" + str(groupId) + "</wpml:actionGroupId>\n")
    out.write("          <wpml:actionGroupStartIndex>" + str(startIndex) + "</wpml:actionGroupStartIndex>\n")
    out.write("          <wpml:actionGroupEndIndex>" + str(endIndex) + "</wpml:actionGroupEndIndex>\n")
    out.write("          <wpml:actionGroupMode>sequence</wpml:actionGroupMode>\n")
    out.write("          <wpml:actionTrigger>\n")
    out.write("             <wpml:actionTriggerType>reachPoint</wpml:actionTriggerType>\n")
    out.write("            </wpml:actionTrigger>\n")
    out.write("            <wpml:action>\n")
    out.write("              <wpml:actionId>0</wpml:actionId>\n")
    out.write("              <wpml:actionActuatorFunc>" + action + "</wpml:actionActuatorFunc>\n")
    out.write("              <wpml:actionActuatorFuncParam>\n")
    out.write("                <wpml:fileSuffix>WP1</wpml:fileSuffix>\n")
    out.write("                <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("                <wpml:useGlobalPayloadLensIndex>0</wpml:useGlobalPayloadLensIndex>\n")
    out.write("              </wpml:actionActuatorFuncParam>\n")
    out.write("            </wpml:action>\n")
    out.write("          </wpml:actionGroup>\n")


def template_placemarks(out, coords):
    lastPointIndex = len(coords)-1
    for i in range(0, len(coords)):
        out.write("        <Placemark>\n")
        out.write("          <Point>\n")
        out.write("            <coordinates>\n")
        out.write("              " + coords[i]['x'] + "," + coords[i]['y'] + "\n")
        out.write("            </coordinates>\n")
        out.write("          </Point>\n")
        out.write("          <wpml:index>" + str(i) + "</wpml:index>\n")
        out.write("          <wpml:ellipsoidHeight>9.14411067962646</wpml:ellipsoidHeight>\n")
        out.write("          <wpml:height>9.14411067962646</wpml:height>\n")
        out.write("          <wpml:useGlobalHeight>1</wpml:useGlobalHeight>\n")
        out.write("          <wpml:useGlobalSpeed>1</wpml:useGlobalSpeed>\n")
        out.write("          <wpml:useGlobalHeadingParam>1</wpml:useGlobalHeadingParam>\n")
        out.write("          <wpml:useGlobalTurnParam>1</wpml:useGlobalTurnParam>\n")
        out.write("          <wpml:gimbalPitchAngle>-90</wpml:gimbalPitchAngle>\n")
        out.write("          <wpml:useStraightLine>0</wpml:useStraightLine>\n")
        if(i == 0):
            template_actiongroup(out,0,0,0,'startRecord')
        if(i == lastPointIndex):
            template_actiongroup(out,1,lastPointIndex,lastPointIndex,'stopRecord')
        out.write("        </Placemark>\n")


def template_payloadParam(out):
    out.write("        <wpml:payloadParam>\n")
    out.write("          <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("        </wpml:payloadParam>\n")



def write_footer(out):
    out.write("    </Folder>\n")
    out.write("  </Document>\n")
    out.write("</kml>\n")

