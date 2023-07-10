import axios from "axios";

axios.defaults.baseURL = import.meta.env.DEV ? "http://localhost:8000/api" : "/api"

class PasteService {
    create = (data) => axios.post("/create", {data}).then(({data}) => data)
    get = (key) => axios.get(`/get`, {params: {key}}).then(({data}) => data)
}

const pasteService = new PasteService();

export default pasteService;
