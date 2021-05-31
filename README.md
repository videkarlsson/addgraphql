# Ad(d)GraphQL

This is a small graphql service for storing and exposing ads

## Running in Docker

Start server

```
docker compose up
```

## Test queries

Open the api on [http://localhost:5000/graphql](http://localhost:5000/graphql) and try the following queries

```graphql
mutation CreateNewPinkBikeAd {
  createAd(
  subject: "A pink bike"
  body: "A old really expensive bike",
  email: "vide.karlsson@gmail.com",
  price: 30000000){
    ad {
      id
      subject
      body
      email
      price
      created_at
    }
    success
    errors
  }
}
```

```graphql
mutation CreateNewBlueBikeAd {
  createAd(
  subject: "A blue bike"
  body: "A new really cheep bike",
  email: "vide.karlsson@gmail.com",
  price: 3){
    ad {
      id
      subject
      body
      email
      price
      created_at
    }
    success
    errors
  }
}
``` 

```graphql
query AllADs {
  listAds(sortBy:{order: DESC, field: PRICE}){
    success
    errors
    ads {
      id
      subject 
      body
      created_at
      email
      price
    }
  }
}
```

```graphql
mutation DeleteAd{
  deleteAd(id: "1"){
    ad {
      id
      subject
      body
      email
      price
      created_at
    }
    success
    errors
  }
}
```