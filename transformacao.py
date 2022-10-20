import pandas as pd

df = pd.read_csv('corruption_data.csv')

# Criação de dataframes temporários vazios

df21 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df20 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df19 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df18 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df17 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df16 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df15 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df14 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df13 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})
df12 = pd.DataFrame({
    "region_name": [],
    "year": [],
    "index": []
})


# Lista dos dataframes acima

frames = [df21, df20, df19, df18, df17, df16, df15, df14, df13, df12]

# Inserção de dados nos dataframes vazios

for i1 in df.columns[1:]:
    frames[list(df.columns[1:]).index(i1)][["region_name", "index"]] = df[["region_name", i1]].copy()
    frames[list(df.columns[1:]).index(i1)]["year"] = int(i1)

# Concatenação dos dataframes com os dados inseridos.

new_df = pd.concat(objs=frames, axis=0, join="outer", ignore_index=True)

# Retirando os espaços em branco da coluna com os nomes dos países.

new_df["region_name"] = new_df["region_name"].str.strip()

# Ordenando a tabela

new_df.sort_values(by=["year", "region_name"], ascending=[True, True], inplace=True)

new_df.reset_index(drop=True)

# Leitura da tabela de códigos regionais.

df_iso = pd.read_csv("regional_codes_iso3166.csv")

# Atribuição do código regional da ISO-3166 à tabela utilizando uma junção entre as tabelas new_df e df_iso.

new_df = new_df.merge(
    right=df_iso[["name", "alpha-3"]],
    how="left",
    left_on="region_name",
    right_on="name"
).drop(columns=["name"]).rename(columns={"alpha-3": "id"})

# Leitura da tabela de ajustes (precisei fazer ajustes manuais nos códigos dos países, o nome do País é escrito de forma diferente em casa tabela.)

ajuste_df = pd.read_csv('ajuste_df')

# Transformação do DataFrame de ajuste em um dicionário para ser utilizado como base das atribuições necessárias de id's.

dados_ajuste = {}

for ind, col in ajuste_df.iterrows():
    dados_ajuste[col["region_name"]] = col["id"]

# Atribuição ao new_df (DataFrame) dos id's faltantes.

for ind, col in new_df.iterrows():
    if col["region_name"] in dados_ajuste.keys():
        new_df.loc[ind, "id"] = dados_ajuste[col["region_name"]]

# Verificação de preenchimento da coluna de id.

new_df[new_df["id"].isnull()].count() # retorno 0

# Exportando para um novo arquivo que será utilizado como base da análise.

new_df.to_csv('new_corruption_data', index=False, index_label=False, encoding='utf-8')
