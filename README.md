## Start lokalnego środowiska (budowanie obrazów)

```console
docker-compose -f docker-compose.yaml up -d --build
```

Można dodać lokalny wpis w /etc/hosts

```console
echo "127.0.1.1         api.example.com" >> /etc/hosts
```

Wypychanie zbudowanego obrazu do repo

```console
docker-compose push
```

## Stop lokalnego środowiska

```console
docker-compose down
```

## Stop i usunięcie volumenu bazy

```console
docker-compose down -v
```

## Przykładowe requesty

---

#### Dodawanie użytkownika

```graphql
mutation {
  createUser(input: { name: "Nazwa użytkownika" }) {
    success
    errors
    user {
      id
      name
    }
  }
}
```

#### Edycja nazwy użytkownika

```graphql
mutation {
  updateUser(input: { id: 1, name: "Inna nazwa użytkownika" }) {
    success
    errors
    user {
      id
      name
    }
  }
}
```

#### Usuwanie użytkownika

```graphql
mutation {
  deleteUser(id: 1) {
    success
    errors
  }
}
```

#### Wyświetlenie użytkownika po ID

```graphql
query {
  showUser(id: 1) {
    success
    errors
    user {
      id
      name
    }
  }
}
```

#### Wyświetlanie wszystkich użytkowników

```graphql
query {
  showUsers {
    success
    errors
    users {
      id
      name
    }
  }
}
```
