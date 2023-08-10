

def wayline_missionConfig(out):
    out.write("    <wpml:missionConfig>\n")
    out.write("    <wpml:flyToWaylineMode>safely</wpml:flyToWaylineMode>\n")
    out.write("    <wpml:finishAction>goHome</wpml:finishAction>\n")
    out.write("    <wpml:exitOnRCLost>executeLostAction</wpml:exitOnRCLost>\n")
    out.write("    <wpml:executeRCLostAction>goBack</wpml:executeRCLostAction>\n")
    out.write("    <wpml:takeOffSecurityHeight>15.0</wpml:takeOffSecurityHeight>\n")
    out.write("    <wpml:globalTransitionalSpeed>15</wpml:globalTransitionalSpeed>\n")
    out.write("    <wpml:droneInfo>\n")
    out.write("      <wpml:droneEnumValue>60</wpml:droneEnumValue>\n")
    out.write("      <wpml:droneSubEnumValue>0</wpml:droneSubEnumValue>\n")
    out.write("    </wpml:droneInfo>\n")
    out.write("    <wpml:payloadInfo>\n")
    out.write("      <wpml:payloadEnumValue>50</wpml:payloadEnumValue>\n")
    out.write("      <wpml:payloadSubEnumValue>0</wpml:payloadSubEnumValue>\n")
    out.write("      <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("    </wpml:payloadInfo>\n")
    out.write("    </wpml:missionConfig>\n")


def wayline_header(out):
    out.write("      <wpml:templateId>0</wpml:templateId>\n")
    out.write("      <wpml:executeHeightMode>relativeToStartPoint</wpml:executeHeightMode>\n")
    out.write("      <wpml:waylineId>0</wpml:waylineId>\n")
    out.write("      <wpml:distance>1000</wpml:distance>\n")
    out.write("      <wpml:duration>500</wpml:duration>\n")
    out.write("      <wpml:autoFlightSpeed>4</wpml:autoFlightSpeed>\n")



def wayline_action_startRecord(out, groupId):
    out.write("          <wpml:action>\n")
    out.write("          <wpml:actionId>" + str(groupId) + "</wpml:actionId>\n")
    out.write("          <wpml:actionActuatorFunc>startRecord</wpml:actionActuatorFunc>\n")
    out.write("          <wpml:actionActuatorFuncParam>\n")
    out.write("            <wpml:fileSuffix>WP1</wpml:fileSuffix>\n")
    out.write("            <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("            <wpml:useGlobalPayloadLensIndex>0</wpml:useGlobalPayloadLensIndex>\n")
    out.write("          </wpml:actionActuatorFuncParam>\n")
    out.write("          </wpml:action>\n")


def wayline_action_stopRecord(out, actionId):
    out.write("          <wpml:action>\n")
    out.write("          <wpml:actionId>" + str(actionId) + "</wpml:actionId>\n")
    out.write("          <wpml:actionActuatorFunc>stopRecord</wpml:actionActuatorFunc>\n")
    out.write("          <wpml:actionActuatorFuncParam>\n")
    out.write("            <wpml:fileSuffix>WP1</wpml:fileSuffix>\n")
    out.write("            <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("            <wpml:useGlobalPayloadLensIndex>0</wpml:useGlobalPayloadLensIndex>\n")
    out.write("          </wpml:actionActuatorFuncParam>\n")
    out.write("          </wpml:action>\n")


def wayline_action_gimbalRotate(out, actionId, angle):
    out.write("            <wpml:action>\n")
    out.write("              <wpml:actionId>" + str(actionId) + "</wpml:actionId>\n")
    out.write("              <wpml:actionActuatorFunc>gimbalRotate</wpml:actionActuatorFunc>\n")
    out.write("              <wpml:actionActuatorFuncParam>\n")
    out.write("                <wpml:gimbalHeadingYawBase>aircraft</wpml:gimbalHeadingYawBase>\n")
    out.write("                <wpml:gimbalRotateMode>absoluteAngle</wpml:gimbalRotateMode>\n")
    out.write("                <wpml:gimbalPitchRotateEnable>1</wpml:gimbalPitchRotateEnable>\n")
    out.write("                <wpml:gimbalPitchRotateAngle>" + str(angle) + "</wpml:gimbalPitchRotateAngle>\n")
    out.write("                <wpml:gimbalRollRotateEnable>0</wpml:gimbalRollRotateEnable>\n")
    out.write("                <wpml:gimbalRollRotateAngle>0</wpml:gimbalRollRotateAngle>\n")
    out.write("                <wpml:gimbalYawRotateEnable>0</wpml:gimbalYawRotateEnable>\n")
    out.write("                <wpml:gimbalYawRotateAngle>0</wpml:gimbalYawRotateAngle>\n")
    out.write("                <wpml:gimbalRotateTimeEnable>0</wpml:gimbalRotateTimeEnable>\n")
    out.write("                <wpml:gimbalRotateTime>10</wpml:gimbalRotateTime>\n")
    out.write("                <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("              </wpml:actionActuatorFuncParam>\n")
    out.write("            </wpml:action>\n")


def wayline_action_gimbalEvenlyRotate(out, actionId, angle):
    out.write("            <wpml:action>\n")
    out.write("            <wpml:actionId>" + str(actionId) + "</wpml:actionId>\n")
    out.write("            <wpml:actionActuatorFunc>gimbalEvenlyRotate</wpml:actionActuatorFunc>\n")
    out.write("            <wpml:actionActuatorFuncParam>\n")
    out.write("              <wpml:gimbalPitchRotateAngle>" + str(angle) + "</wpml:gimbalPitchRotateAngle>\n")
    out.write("              <wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>\n")
    out.write("            </wpml:actionActuatorFuncParam>\n")
    out.write("            </wpml:action>\n")


def wayline_actiongroup(out, groupId, startIndex, endIndex, action):
    out.write("          <wpml:actionGroup>\n")
    out.write("            <wpml:actionGroupId>" + str(groupId) + "</wpml:actionGroupId>\n")
    out.write("            <wpml:actionGroupStartIndex>" + str(startIndex) + "</wpml:actionGroupStartIndex>\n")
    out.write("            <wpml:actionGroupEndIndex>" + str(endIndex) + "</wpml:actionGroupEndIndex>\n")
    out.write("            <wpml:actionGroupMode>sequence</wpml:actionGroupMode>\n")
    out.write("            <wpml:actionTrigger>\n")
    out.write("              <wpml:actionTriggerType>reachPoint</wpml:actionTriggerType>\n")
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


def wayline_placemarks(out, coords):
    lastPointIndex = len(coords)-1
    for i in range(0, len(coords)):
        out.write("        <Placemark>\n")
        out.write("          <Point>\n")
        out.write("            <coordinates>\n")
        out.write("              " + coords[i]['x'] + "," + coords[i]['y'] + "\n")
        out.write("            </coordinates>\n")
        out.write("          </Point>\n")
        out.write("          <wpml:index>" + str(i) + "</wpml:index>\n")
        out.write("          <wpml:executeHeight>9.14411067962646</wpml:executeHeight>\n")
        out.write("          <wpml:waypointSpeed>4</wpml:waypointSpeed>\n")
        out.write("          <wpml:waypointHeadingParam>\n")
        out.write("            <wpml:waypointHeadingMode>manually</wpml:waypointHeadingMode>\n")
        out.write("            <wpml:waypointHeadingAngle>0</wpml:waypointHeadingAngle>\n")
        out.write("            <wpml:waypointPoiPoint>0.000000,0.000000,0.000000</wpml:waypointPoiPoint>\n")
        out.write("            <wpml:waypointHeadingAngleEnable>0</wpml:waypointHeadingAngleEnable>\n")
        out.write("            <wpml:waypointHeadingPoiIndex>0</wpml:waypointHeadingPoiIndex>\n")
        out.write("          </wpml:waypointHeadingParam>\n")
        out.write("          <wpml:waypointTurnParam>\n")
        out.write("            <wpml:waypointTurnMode>toPointAndStopWithDiscontinuityCurvature</wpml:waypointTurnMode>\n")
        out.write("            <wpml:waypointTurnDampingDist>0</wpml:waypointTurnDampingDist>\n")
        out.write("          </wpml:waypointTurnParam>\n")
        out.write("          <wpml:useStraightLine>1</wpml:useStraightLine>\n")
        out.write("          <wpml:actionGroup>\n")
        out.write("            <wpml:actionGroupId>" + str(i) + "</wpml:actionGroupId>\n")
        out.write("            <wpml:actionGroupStartIndex>" + str(i) + "</wpml:actionGroupStartIndex>\n")
        out.write("            <wpml:actionGroupEndIndex>" + str(i) + "</wpml:actionGroupEndIndex>\n")
        out.write("            <wpml:actionGroupMode>sequence</wpml:actionGroupMode>\n")
        out.write("          <wpml:actionTrigger>\n")
        out.write("            <wpml:actionTriggerType>reachPoint</wpml:actionTriggerType>\n")
        out.write("          </wpml:actionTrigger>\n")


        
        if(i == lastPointIndex):
            wayline_actiongroup(out,1,lastPointIndex,lastPointIndex,'stopRecord')
        out.write("          <wpml:waypointGimbalHeadingParam>\n")
        out.write("          <wpml:waypointGimbalPitchAngle>0</wpml:waypointGimbalPitchAngle>\n")
        out.write("          <wpml:waypointGimbalYawAngle>0</wpml:waypointGimbalYawAngle>\n")
        out.write("          </wpml:waypointGimbalHeadingParam>\n")
        out.write("        </Placemark>\n")
