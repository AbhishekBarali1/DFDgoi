import xml.etree.ElementTree as ET

def create_diagram(name):
    diagram = ET.Element("diagram", name=name, id=name)
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="1000", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
    root = ET.SubElement(mxGraphModel, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    return diagram, root

def add_entity(root, id, value, x, y, width=120, height=60):
    cell = ET.SubElement(root, "mxCell", id=id, value=value, style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(width), height=str(height), **{"as": "geometry"})

def add_process(root, id, value, x, y, width=120, height=120):
    cell = ET.SubElement(root, "mxCell", id=id, value=value, style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#d5e8d4;strokeColor=#82b366;", vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(width), height=str(height), **{"as": "geometry"})

def add_datastore(root, id, value, x, y, width=120, height=60):
    cell = ET.SubElement(root, "mxCell", id=id, value=value, style="shape=partialRectangle;whiteSpace=wrap;html=1;left=0;right=0;fillColor=#ffe6cc;strokeColor=#d79b00;", vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(width), height=str(height), **{"as": "geometry"})

def add_flow(root, id, source, target, value=""):
    cell = ET.SubElement(root, "mxCell", id=id, value=value, style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;", edge="1", parent="1", source=source, target=target)
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

mxfile = ET.Element("mxfile", version="21.6.8", type="device")

# Student Enrollment - Context (Level 0)
diag0, root0 = create_diagram("Level 0 - Context")
add_process(root0, "p0", "0.0\nStudent Enrollment\nSystem", 350, 250)
add_entity(root0, "e1", "Student", 50, 280)
add_entity(root0, "e2", "Professor", 650, 150)
add_entity(root0, "e3", "Registration Office", 650, 400)

add_flow(root0, "f1", "e1", "p0", "Course Selections")
add_flow(root0, "f2", "p0", "e1", "Schedule/Details")
add_flow(root0, "f3", "e2", "p0", "Login Info")
add_flow(root0, "f4", "p0", "e2", "Class Roster")
add_flow(root0, "f5", "e3", "p0", "Approval/Rejection")
add_flow(root0, "f6", "p0", "e3", "Pending Registrations")
mxfile.append(diag0)

# Student Enrollment - Level 1
diag1, root1 = create_diagram("Level 1")
add_entity(root1, "l1_e1", "Student", 50, 250)
add_entity(root1, "l1_e2", "Professor", 650, 100)
add_entity(root1, "l1_e3", "Registration Office", 650, 400)

add_process(root1, "l1_p1", "1.0\nManage Courses", 250, 100)
add_process(root1, "l1_p2", "2.0\nManage Registration", 250, 250)
add_process(root1, "l1_p3", "3.0\nManage Schedules\n& Rosters", 450, 250)

add_datastore(root1, "l1_d1", "D1 Student DB", 450, 400)
add_datastore(root1, "l1_d2", "D2 Course DB", 450, 100)

add_flow(root1, "l1_f1", "l1_e1", "l1_p1", "Search Query")
add_flow(root1, "l1_f2", "l1_p1", "l1_e1", "Course Details")
add_flow(root1, "l1_f3", "l1_e1", "l1_p2", "Course Selections")
add_flow(root1, "l1_f4", "l1_p2", "l1_e3", "Pending Reg")
add_flow(root1, "l1_f5", "l1_e3", "l1_p2", "Approval")
add_flow(root1, "l1_f6", "l1_p2", "l1_d1", "Update Records")
add_flow(root1, "l1_f7", "l1_p1", "l1_d2", "Query")
add_flow(root1, "l1_f8", "l1_d2", "l1_p1", "Results")
add_flow(root1, "l1_f9", "l1_d1", "l1_p3", "Student Data")
add_flow(root1, "l1_f10", "l1_d2", "l1_p3", "Course Data")
add_flow(root1, "l1_f11", "l1_p3", "l1_e1", "Schedule")
add_flow(root1, "l1_f12", "l1_p3", "l1_e2", "Class Roster")
mxfile.append(diag1)

# Student Enrollment - Level 2 (Process 2)
diag2, root2 = create_diagram("Level 2 (Process 2)")
add_entity(root2, "l2_e1", "Student", 50, 100)
add_entity(root2, "l2_e3", "Registration Office", 650, 250)

add_process(root2, "l2_p1", "2.1\nSubmit Selections", 250, 100)
add_process(root2, "l2_p2", "2.2\nReview & Approve", 450, 250)
add_process(root2, "l2_p3", "2.3\nUpdate Records", 250, 400)

add_datastore(root2, "l2_d1", "D1 Student DB", 450, 400)
add_datastore(root2, "l2_d2", "D2 Course DB", 450, 100)

add_flow(root2, "l2_f1", "l2_e1", "l2_p1", "Selections")
add_flow(root2, "l2_f2", "l2_p1", "l2_p2", "Pending Reg")
add_flow(root2, "l2_f3", "l2_p2", "l2_e3", "Pending Reg")
add_flow(root2, "l2_f4", "l2_e3", "l2_p2", "Approval")
add_flow(root2, "l2_f5", "l2_p2", "l2_p3", "Approved Reg")
add_flow(root2, "l2_f6", "l2_p3", "l2_d1", "Update")
add_flow(root2, "l2_f7", "l2_d2", "l2_p2", "Course Info")
mxfile.append(diag2)

# Student Enrollment - Level 3 (Process 2.2)
diag3, root3 = create_diagram("Level 3 (Process 2.2)")
add_process(root3, "l3_p1", "2.2.1\nRetrieve Pending", 250, 100)
add_process(root3, "l3_p2", "2.2.2\nEvaluate Reg", 250, 250)
add_process(root3, "l3_p3", "2.2.3\nRecord Status", 250, 400)

add_entity(root3, "l3_e3", "Registration Office", 650, 250)
add_datastore(root3, "l3_d2", "D2 Course DB", 50, 280)

add_flow(root3, "l3_f1", "l3_p1", "l3_p2", "Pending Reg")
add_flow(root3, "l3_f2", "l3_d2", "l3_p2", "Prereqs/Capacity")
add_flow(root3, "l3_f3", "l3_p2", "l3_e3", "Evaluation")
add_flow(root3, "l3_f4", "l3_e3", "l3_p3", "Decision")
add_flow(root3, "l3_f5", "l3_p3", "l3_p1", "Next Reg")
mxfile.append(diag3)

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="\t", level=0)
tree.write("student-enrollment-dfd.drawio", encoding="utf-8", xml_declaration=True)
