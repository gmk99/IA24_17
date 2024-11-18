def parse_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {}
    section = None

    for line in lines:
        line = line.strip()  # Remover espaços em branco extras
        print(f"Processing line: {line}")  # Debug: Verificar cada linha

        # Ignorar delimitadores e comentários
        if line.startswith('************************************************************************') or not line:
            continue

        # Identificar a seção atual
        if line == "#General Information":
            section = "general_info"
            data[section] = {}
        elif line == "#Projects summary":
            section = "projects_summary"
            data[section] = []
        elif line == "#Precedence relations":
            section = "precedence_relations"
            data[section] = []
        elif line == "#Duration and resources":
            section = "duration_and_resources"
            data[section] = []
        elif line == "#Resource availability":
            section = "resource_availability"
            data[section] = {}
        elif section == "general_info":
            # Processar informações gerais
            if ':' in line:  # Apenas processar linhas com chave: valor
                key, value = line.split(":", 1)
                data[section][key.strip()] = value.strip()
        elif section == "projects_summary":
            # Ignorar cabeçalho
            if line.startswith("pronr."):
                continue
            parts = line.split()
            data[section].append({
                "project_number": int(parts[0]),
                "jobs": int(parts[1]),
                "release_date": int(parts[2]),
                "due_date": int(parts[3]),
                "tardiness_cost": int(parts[4]),
                "mpm_time": int(parts[5])
            })
        elif section == "precedence_relations":
            # Ignorar cabeçalho
            if line.startswith("#jobnr."):
                continue
            parts = line.split()
            data[section].append({
                "job": int(parts[0]),
                "modes": int(parts[1]),
                "successors": [int(x) for x in parts[3:]]
            })
        elif section == "duration_and_resources":
            # Ignorar cabeçalho
            if line.startswith("#jobnr."):
                continue
            parts = line.split()
            data[section].append({
                "job": int(parts[0]),
                "mode": int(parts[1]),
                "duration": int(parts[2]),
                "resources": [int(x) for x in parts[3:]]
            })
        elif section == "resource_availability":
            # Ignorar cabeçalho
            if line.startswith("#resource"):
                continue
            resource, qty = line.split()
            data[section][resource] = int(qty)

    return data

# Caminho do arquivo
file_path = r"C:\Users\maroc\OneDrive\Ambiente de Trabalho\IA24_17\IA24_17_Folder\dataset_10.txt"



# Executar o parser
parsed_data = parse_dataset(file_path)
print(parsed_data)