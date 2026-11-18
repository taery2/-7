```mermaid
flowchart TD
A([Старт])-->B{n<0?}
B--Да-->C[0]
B--Нет-->D{n=0?}
D--Да-->E[1]
D--Нет-->F[F(n-1)+F(n-2)+F(n-3)]
```