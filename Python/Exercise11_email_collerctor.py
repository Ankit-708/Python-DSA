import re
str = """
. MADHYA PRADESH – BHOPAL
1. ACROPOLIS ITR
COLLEGE ADDRESS	COLLEGE CONTACT DETAILS
VILLAGE SIKANDRABAD RATIBAD
BHOPAL
MADHYA PRADESH
Pincode: 462044
College Short Code:ACROPO	Contact Nos: 07552896521
Email Id… : info@acropolis.ac.in
Fax No……:
Nodal Officer Name: SHUBHENDRA GUPTA
Nodal Officer Mobile No:
Nodal Officer Email Id:
2. AGNOS COLLEGE OF TECHNOLOGY
COLLEGE ADDRESS	COLLEGE CONTACT DETAILS
NEAR RGPV CAMPUS, AIRPORT BYPASS ROAD, GONDERMAU, GANDHINAGAR, BHOPAL
BHOPAL
MADHYA PRADESH
College Short Code:AGNOS	Contact Nos:
Email Id… :
Fax No……:
Nodal Officer Name:
Nodal Officer Mobile No:
Nodal Officer Email Id:
3. ALL SAINTS’ COLLEGE OF ENGINEERING
COLLEGE ADDRESS	COLLEGE CONTACT DETAILS
NEW PIPALNAIR, NEARGANDHI NAGAR-462031
BHOPAL
MADHYA PRADESH
College Short Code:ASCE	Contact Nos:
Email Id… :
Fax No……:
Nodal Officer Name:
Nodal Officer Mobile No:
Nodal Officer Email Id:
4. ALL SAINTS’ COLLEGE OF TECHNOLOGY
COLLEGE ADDRESS	COLLEGE CONTACT DETAILS
NH 12 GANDHI NAGAR BHOPAL
BHOPAL
MADHYA PRADESH
College Short Code:ASCT	Contact Nos:
Email Id… :
Fax No……:
Nodal Officer Name: Aizaz
Nodal Officer Mobile No: 9039338829
Nodal Officer Email Id: aizaztirmizi@hotmail.com"""

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)

