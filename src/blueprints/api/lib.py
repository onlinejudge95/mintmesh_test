def get_all_nodes(nodes):
    result = []
    count = 0

    for node in nodes:
        try:
            data_nodes = node.find_all("td")
            count += 1
            country_name = data_nodes[1].find("a").contents[0]
            total_cases = int(data_nodes[2].contents[0].replace(",", ""))
            print(total_cases)
            temp = {
                "country_name": country_name,
                "total_cases": total_cases,
            }
            result.append(temp)
            if count == 10:
                break
        except Exception as e:
            print(e)
            continue
    
    return result
