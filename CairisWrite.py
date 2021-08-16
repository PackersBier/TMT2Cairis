from dict2xml import dict2xml


# Convert the data from the Threat Dragon Map to a Cairis Map
def convert(model):
    sub_model = model["detail"]["diagrams"][0]["diagramJson"]["cells"]
    # Create dict over dict to later iterate over the types (type not available in all elements)
    collection = dict.fromkeys(["type", "element"])
    for cell in sub_model:
        typ = cell["type"]
        # Because Actor and Datastore are both Assets(Entities) in Cairis we put them together
        if typ == "tm.Actor" or typ == "tm.Store":
            entity = dict.fromkeys(["label", "type", "id", "x", "y", "width", "height"])
            entity["label"] = cell["name"]
            entity["id"] = cell["id"]
            # X any Y value are stored in an own dict position
            position = cell["position"]
            entity["x"] = position["x"]
            entity["y"] = position["y"]
            # Width and Height are stored in an own dict size
            size = cell["size"]
            entity["height"] = size["height"]
            entity["width"] = size["width"]
            # Because we handle two types we have to seperate
            if typ == "tm.Actor":
                entity["type"] = "entity"
                collection["type"] = "entity"
            else:
                entity["type"] = "datastore"
                collection["type"] = "datastore"
            collection["element"] = entity
            print(collection)

        elif typ == "tm.Flow":
            print(typ)
            """# 1. Create corresponding dict. with relevant information
            line = dict.fromkeys(["name", "environment", "from_name", "from_type", "to_name", "to_type"])
            # 2. Add corresponding name
            line["name"] = cell["name"]
            # 3. Because of missing information we define the environment for all lines with day
            line["environment"] = "Day"
            # 4. For lines we need a source and his Type with a Globally Unique Identifier
            for stencil in sub_model:
                line_source = cell["source"]
                if stencil["id"] == line_source["id"]:
                    line["from_name"] = stencil["name"]
                    line["from_type"] = type_convert(stencil["type"])  # Typ muss hier wohl noch angepasst werden!!!
                    break
                else:
                    pass
            # 5. As well as the target and his type
            for stencil in sub_model:
                line_target = cell["target"]
                if stencil["id"] == line_target["id"]:
                    line["to_name"] = stencil["name"]
                    line["to_type"] = stencil["type"]  # Typ muss hier wohl noch angepasst werden!!!
                    break
                else:
                    pass
            # 6. All relevant information are now included, so we can pass it to the XML-Convert
            xml_components(line)
            """

        elif typ == "tm.Boundary":
            print(typ)
            """
            boundary = dict.fromkeys(["name", "id", "x", "y", "width", "height"])
            boundary["name"] = cell["name"]
            boundary["id"] = cell["id"]
            # TODO

            collection["type"] = "trustboundary"
            collection["element"] = boundary
            """

        elif typ == "tm.Process":
            print(typ)
            """
            process = dict.fromkeys(["name", "author", "code"])
            process["name"] = cell["name"]
            # Because of missing information of the author - predefined TMT2Cairis
            process["author"] = "TMT2Cairis"
            # Because of missing information of the short Code - predefined as PCS (Process)
            process["code"] = "PCS"
            """

        elif typ == "summary":
            print(typ)
        else:
            print("Error")
    print("collection:")
    print(collection)
    createXML(collection)


# Import Data Flow dict and convert to data flow xml syntax
def createXML(collection):
    print(dict2xml(collection, "mxfile"))
    """   
    root = lxml.builder.ElementMaker()
    model = root.cairis_model
    dataflow_xml = "model("

    riskanalysis = root.riskanalysis

    for cell in cells:
        if cell["type"] ==:
            goals = root.goals
        usecase = root.usecase
        process_xml = model(goals(
            usecase(name=cell["name"],
                    author=cell["author"],
                    code=cell["code"])))
        dataflow_xml = dataflow_xml + lxml.etree.tostring(process_xml)
        break
        else: pass
    
    dataflows = root.dataflows
    
    dataflow = root.dataflow
    dataflow_xml = model(dataflows(
        dataflow(name=cell["name"],
                 environment=cell["environment"],
                 from_name=cell["from_name"],
                 from_type=cell["from_type"],
                 to_name=cell["to_name"],
                 to_type=cell["to_type"])))
    dataflow_xml = dataflow_xml + lxml.etree.tostring(dataflow_xml)
    """
