const express = require('express');
const router = express.Router();
const fileController = require('../file.controller');

let routes = (app) => {
    router.get("/files", fileController.getListFiles);
    router.get("/files/:name", fileController.download);
  
    app.use(router);
};

module.exports = routes;
