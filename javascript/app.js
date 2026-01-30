import express from 'express';
const app = express();
const port = 3000;


let people = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Doe' }
];


app.get("/people", (req, res) => {
    res.json(people);
});


app.listen(port, () => {
  console.log(`javascript webapi example listening on http://localhost:${port}`);
});
