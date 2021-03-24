const express = require('express');
const cors = require("cors");

const app = express();
const hostname = "172.21.11.131";
const port = 80;

global.__basedir = __dirname;

var corsOptions = {
//   origin: "http://localhost:8081"
  origin: "http://localhost:80"
};

app.use(cors(corsOptions));

const initRoutes = require('./routes')
initRoutes(app);

const server = app.listen(port, hostname, () => {
    const serverAddress = server.address();
    console.log(`server ${serverAddress.address}:${serverAddress.port} is created.`);
    // console.log(`app listening on port ${port}.`);
});
