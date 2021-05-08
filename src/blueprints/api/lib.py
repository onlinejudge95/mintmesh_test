def get_all_nodes(nodes):
    result = []

    for node in nodes:
        data_nodes = node.find_all("td")
        try:
            country_name = data_nodes[1].find("a").contents[0]
            total_cases = int(data_nodes[2].contents[0].replace(",", "").strip())
            active_cases = int(data_nodes[8].contents[0].replace(",", "").strip())
            total_deaths = int(data_nodes[4].contents[0].replace(",", "").strip())
            total_recovered = int(data_nodes[6].contents[0].replace(",", "").strip())
            population = int(data_nodes[14].find("a").contents[0].replace(",", "").strip())
            temp = {
                "country_name": country_name,
                "total_cases": total_cases,
                "active_cases": active_cases,
                "total_deaths": total_deaths,
                "recovery_rate": round((total_recovered * 100.0) / total_cases, 2),
                "infected_population_percentage": round((total_cases * 100.0) / population, 2)
            }
            result.append(temp)
        except Exception as e:
            print(e)

    return result
