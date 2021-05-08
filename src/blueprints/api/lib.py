def get_all_nodes(nodes):
    result = []

    for node in nodes:
        try:
            data_nodes = node.find_all("td")
            total_cases = int(data_nodes[2].contents[0].replace(",", ""))
            total_recovered = int(data_nodes[6].contents[0].replace(",", ""))
            population = int(data_nodes[14].contents[0].replace(",", ""))
            temp = {
                "country_name": data_nodes[1].find("a").contents[0],
                "total_cases": total_cases,
                "active_cases": int(data_nodes[8].contents[0].replace(",", "")),
                "total_deaths": int(data_nodes[4].contents[0].replace(",", "")),
                "recovery_rate": round((total_recovered * 100.0) / total_cases, 2),
                "infected_population_percentage": round((total_cases * 100.0) / population, 2)
            }
            result.append(temp)
        except Exception as e:
            print(e)
            continue
    
    return result
