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

# Online Bookstore - Context (Level 0)
diag0, root0 = create_diagram("Level 0 - Context")
add_process(root0, "p0", "0.0\nOnline Bookstore\nSystem", 350, 250)
add_entity(root0, "e1", "Customer", 50, 280)
add_entity(root0, "e2", "Admin", 350, 50)
add_entity(root0, "e3", "Payment Gateway", 650, 150)
add_entity(root0, "e4", "Shipping Service", 650, 400)

add_flow(root0, "f1", "e1", "p0", "Order/Payment Info")
add_flow(root0, "f2", "p0", "e1", "Book Info/Status")
add_flow(root0, "f3", "e2", "p0", "Updates")
add_flow(root0, "f4", "p0", "e2", "Reports")
add_flow(root0, "f5", "p0", "e3", "Payment Req")
add_flow(root0, "f6", "e3", "p0", "Payment Status")
add_flow(root0, "f7", "p0", "e4", "Shipping Details")
mxfile.append(diag0)

# Online Bookstore - Level 1
diag1, root1 = create_diagram("Level 1")
add_entity(root1, "l1_e1", "Customer", 50, 150)
add_entity(root1, "l1_e2", "Admin", 50, 450)
add_entity(root1, "l1_e3", "Payment Gateway", 650, 150)
add_entity(root1, "l1_e4", "Shipping Service", 650, 450)

add_process(root1, "l1_p1", "1.0\nManage Account", 250, 50)
add_process(root1, "l1_p2", "2.0\nBrowse Books", 250, 250)
add_process(root1, "l1_p3", "3.0\nProcess Order", 450, 250)
add_process(root1, "l1_p4", "4.0\nAdminister Website", 250, 450)

add_datastore(root1, "l1_d1", "D1 Inventory DB", 450, 50)
add_datastore(root1, "l1_d2", "D2 Customer DB", 450, 450)

add_flow(root1, "l1_f1", "l1_e1", "l1_p1", "Account Info")
add_flow(root1, "l1_f2", "l1_e1", "l1_p2", "Search Query")
add_flow(root1, "l1_f3", "l1_e1", "l1_p3", "Order Details")
add_flow(root1, "l1_f4", "l1_p3", "l1_e3", "Payment Req")
add_flow(root1, "l1_f5", "l1_e3", "l1_p3", "Payment Status")
add_flow(root1, "l1_f6", "l1_p3", "l1_e4", "Shipping Info")
add_flow(root1, "l1_f7", "l1_e2", "l1_p4", "Updates")
add_flow(root1, "l1_f8", "l1_p2", "l1_d1", "Query")
add_flow(root1, "l1_f9", "l1_d1", "l1_p2", "Results")
add_flow(root1, "l1_f10", "l1_p3", "l1_d1", "Update Stock")
add_flow(root1, "l1_f11", "l1_p1", "l1_d2", "Update")
mxfile.append(diag1)

# Online Bookstore - Level 2 (Process 3)
diag2, root2 = create_diagram("Level 2 (Process 3)")
add_entity(root2, "l2_e1", "Customer", 50, 250)
add_entity(root2, "l2_e3", "Payment Gateway", 650, 100)
add_entity(root2, "l2_e4", "Shipping Service", 650, 400)

add_process(root2, "l2_p1", "3.1\nPlace Order", 250, 100)
add_process(root2, "l2_p2", "3.2\nProcess Payment", 450, 100)
add_process(root2, "l2_p3", "3.3\nUpdate Inventory", 450, 250)
add_process(root2, "l2_p4", "3.4\nFulfill Order", 450, 400)

add_datastore(root2, "l2_d1", "D1 Inventory DB", 250, 280)
add_datastore(root2, "l2_d3", "D3 Order DB", 250, 430)

add_flow(root2, "l2_f1", "l2_e1", "l2_p1", "Cart/Checkout")
add_flow(root2, "l2_f2", "l2_p1", "l2_p2", "Payment Info")
add_flow(root2, "l2_f3", "l2_p2", "l2_e3", "Req")
add_flow(root2, "l2_f4", "l2_e3", "l2_p2", "Status")
add_flow(root2, "l2_f5", "l2_p2", "l2_p3", "Success")
add_flow(root2, "l2_f6", "l2_p3", "l2_d1", "Reduce Stock")
add_flow(root2, "l2_f7", "l2_p3", "l2_p4", "Trigger Fulfillment")
add_flow(root2, "l2_f8", "l2_p4", "l2_e4", "Shipping Details")
add_flow(root2, "l2_f9", "l2_p4", "l2_d3", "Save Order")
mxfile.append(diag2)

# Online Bookstore - Level 3 (Process 3.4)
diag3, root3 = create_diagram("Level 3 (Process 3.4)")
add_process(root3, "l3_p1", "3.4.1\nPrepare Order", 250, 100)
add_process(root3, "l3_p2", "3.4.2\nGenerate Invoice", 250, 250)
add_process(root3, "l3_p3", "3.4.3\nSend to Shipping", 250, 400)

add_datastore(root3, "l3_d3", "D3 Order DB", 50, 130)
add_entity(root3, "l3_e4", "Shipping Service", 500, 430)
add_entity(root3, "l3_e1", "Customer", 500, 280)

add_flow(root3, "l3_f1", "l3_d3", "l3_p1", "Order Details")
add_flow(root3, "l3_f2", "l3_p1", "l3_p2", "Prepared Order")
add_flow(root3, "l3_f3", "l3_p2", "l3_e1", "Invoice")
add_flow(root3, "l3_f4", "l3_p2", "l3_p3", "Order+Invoice")
add_flow(root3, "l3_f5", "l3_p3", "l3_e4", "Shipping Info")
mxfile.append(diag3)

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="\t", level=0)
tree.write("online-bookstore-dfd.drawio", encoding="utf-8", xml_declaration=True)
