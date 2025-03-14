const express = require("express");
const axios = require("axios");
const cors = require("cors");
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static("public"));


// Đăng ký người dùng
app.post("/register", async (req, res) => {
    let response = await axios.post("http://127.0.0.1:5000/auth/register", req.body);
    res.json(response.data);
});

// Đăng nhập
app.post("/login", async (req, res) => {
    let response = await axios.post("http://127.0.0.1:5000/auth/login", req.body);
    res.json(response.data);
});

// Lấy danh sách phòng trọ
app.get("/rooms", async (req, res) => {
    let response = await axios.get("http://127.0.0.1:5000/rooms/get-rooms");
    res.json(response.data);
});

app.listen(3000, () => console.log("Frontend server running on port 3000"));

