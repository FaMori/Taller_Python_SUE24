library(schrute)
library(dplyr)

## Armamos conjunto de datos de episodios.
data <- theoffice |> 
  select(c(episode_name, season, imdb_rating, total_votes, air_date)) |>
  distinct()
write.csv(data, "episodios.csv", row.names = F)

## Armamos conjuntos de datos de lineas
dialogos <- theoffice |>
  select(c(episode_name, character, text))
write.csv(dialogos, "dialogos.csv", row.names = F)

##Armamos conjunto de datos creadores.
creators <- theoffice |>
  distinct(episode_name, director, writer) |>
  pivot_longer(director:writer, names_to = "role", values_to = "person") |>
  separate_rows(person, sep = ";") |>
  add_count(person) |>
  mutate(person = case_when(
    n <= 10 ~ 'Guest',
    n > 10 ~ person
  )) |>
  distinct(episode_name, person) |>
  mutate(person_value = 1) |>
  pivot_wider(
    names_from = person,
    values_from = person_value,
    values_fill = list(person_value = 0)
  )

write.csv(creators, "creadores.csv", row.names = F)


