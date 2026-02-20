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

# World's Trend - Context (Level 0)
diag0, root0 = create_diagram("Level 0 - Context")
add_process(root0, "p0", "0.0\nWorld's Trend\nOrder System", 350, 250)
add_entity(root0, "e1", "Customer", 50, 280)
add_entity(root0, "e2", "Inventory Control\nDepartment", 650, 100)
add_entity(root0, "e3", "Warehouse", 650, 280)
add_entity(root0, "e4", "Accounting\nDepartment", 650, 450)

add_flow(root0, "f1", "e1", "p0", "Customer Order")
add_flow(root0, "f2", "p0", "e1", "Shipping Statement\n& Goods")
add_flow(root0, "f3", "p0", "e1", "Billing Statement")
add_flow(root0, "f4", "p0", "e2", "Out of Stock Notice")
add_flow(root0, "f5", "p0", "e3", "Picking Slip")
add_flow(root0, "f6", "e3", "p0", "Goods")
add_flow(root0, "f7", "p0", "e4", "Accounts Receivable\nReport")
mxfile.append(diag0)

# World's Trend - Level 1
diag1, root1 = create_diagram("Level 1")
add_entity(root1, "l1_e1", "Customer", 50, 250)
add_entity(root1, "l1_e2", "Inventory Control", 650, 50)
add_entity(root1, "l1_e3", "Warehouse", 650, 250)
add_entity(root1, "l1_e4", "Accounting", 650, 450)

add_process(root1, "l1_p1", "1.0\nProcess Order", 250, 50)
add_process(root1, "l1_p2", "2.0\nShip Order", 250, 250)
add_process(root1, "l1_p3", "3.0\nGenerate Billing", 250, 450)

add_datastore(root1, "l1_d1", "D1 Item Master", 450, 50)
add_datastore(root1, "l1_d2", "D2 Customer Master", 450, 450)

add_flow(root1, "l1_f1", "l1_e1", "l1_p1", "Order")
add_flow(root1, "l1_f2", "l1_p1", "l1_d1", "Update Item")
add_flow(root1, "l1_f3", "l1_p1", "l1_d2", "Update/New Cust")
add_flow(root1, "l1_f4", "l1_p1", "l1_e2", "Out of Stock")
add_flow(root1, "l1_f5", "l1_p1", "l1_p2", "Picking Slip &\nShipping Stmt")
add_flow(root1, "l1_f6", "l1_p2", "l1_e3", "Picking Slip")
add_flow(root1, "l1_f7", "l1_e3", "l1_p2", "Goods")
add_flow(root1, "l1_f8", "l1_d2", "l1_p2", "Address")
add_flow(root1, "l1_f9", "l1_p2", "l1_e1", "Goods & Stmt")
add_flow(root1, "l1_f10", "l1_d2", "l1_p3", "Cust Data")
add_flow(root1, "l1_f11", "l1_p3", "l1_e1", "Billing Stmt")
add_flow(root1, "l1_f12", "l1_p3", "l1_e4", "A/R Report")
mxfile.append(diag1)

# World's Trend - Level 2 (Process 1)
diag2, root2 = create_diagram("Level 2 (Process 1)")
add_entity(root2, "l2_e1", "Customer", 50, 250)
add_entity(root2, "l2_e2", "Inventory Control", 650, 100)

add_process(root2, "l2_p1", "1.1\nReceive Order", 250, 100)
add_process(root2, "l2_p2", "1.2\nUpdate Inventory", 450, 100)
add_process(root2, "l2_p3", "1.3\nUpdate Customer", 250, 400)
add_process(root2, "l2_p4", "1.4\nPrepare Shipping\nDocs", 450, 400)

add_datastore(root2, "l2_d1", "D1 Item Master", 450, 250)
add_datastore(root2, "l2_d2", "D2 Customer Master", 250, 250)

add_flow(root2, "l2_f1", "l2_e1", "l2_p1", "Order")
add_flow(root2, "l2_f2", "l2_p1", "l2_p2", "Item Details")
add_flow(root2, "l2_f3", "l2_p1", "l2_p3", "Cust Details")
add_flow(root2, "l2_f4", "l2_p2", "l2_d1", "Update Stock")
add_flow(root2, "l2_f5", "l2_p2", "l2_e2", "Out of Stock")
add_flow(root2, "l2_f6", "l2_p3", "l2_d2", "Update/Create")
add_flow(root2, "l2_f7", "l2_p1", "l2_p4", "Order Details")
add_flow(root2, "l2_f8", "l2_p4", "l2_p4", "To Process 2.0") # Placeholder for flow to next process
mxfile.append(diag2)

# World's Trend - Level 2 (Process 2)
diag3, root3 = create_diagram("Level 2 (Process 2)")
add_entity(root3, "l3_e1", "Customer", 50, 250)
add_entity(root3, "l3_e3", "Warehouse", 650, 100)

add_process(root3, "l3_p1", "2.1\nSend Picking Slip", 250, 100)
add_process(root3, "l3_p2", "2.2\nMatch Goods &\nStatement", 450, 100)
add_process(root3, "l3_p3", "2.3\nGet Address", 450, 250)
add_process(root3, "l3_p4", "2.4\nShip to Customer", 250, 400)

add_datastore(root3, "l3_d2", "D2 Customer Master", 650, 250)

add_flow(root3, "l3_f1", "l3_p1", "l3_e3", "Picking Slip")
add_flow(root3, "l3_f2", "l3_e3", "l3_p2", "Goods")
add_flow(root3, "l3_f3", "l3_p2", "l3_p3", "Matched Order")
add_flow(root3, "l3_f4", "l3_d2", "l3_p3", "Address")
add_flow(root3, "l3_f5", "l3_p3", "l3_p4", "Ready to Ship")
add_flow(root3, "l3_f6", "l3_p4", "l3_e1", "Goods & Stmt")
mxfile.append(diag3)

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="\t", level=0)
tree.write("worlds-trend-new-dfd.drawio", encoding="utf-8", xml_declaration=True)
