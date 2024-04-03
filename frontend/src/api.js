import axios from "axios";

// Creates a new instance of axios with a custom config
const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;
