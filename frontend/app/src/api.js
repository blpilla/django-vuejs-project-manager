import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default {
  getClientes() {
    return apiClient.get('clientes/');
  },
  addCliente(cliente) {
    return apiClient.post('clientes/', cliente);
  },
  updateCliente(id, cliente) {
    return apiClient.put(`clientes/${id}/`, cliente);
  },
  deleteCliente(id) {
    return apiClient.delete(`clientes/${id}/`);
  },
  getProjetos() {
    return apiClient.get('projetos/');
  },
  addProjeto(projeto) {
    return apiClient.post('projetos/', projeto);
  },
  updateProjeto(id, projeto) {
    return apiClient.put(`projetos/${id}/`, projeto);
  },
  deleteProjeto(id) {
    return apiClient.delete(`projetos/${id}/`);
  },
  getAtividades() {
    return apiClient.get('atividades/');
  },
  addAtividade(atividade) {
    return apiClient.post('atividades/', atividade);
  },
  updateAtividade(id, atividade) {
    return apiClient.put(`atividades/${id}/`, atividade);
  },
  deleteAtividade(id) {
    return apiClient.delete(`atividades/${id}/`);
  },
  login(credentials) {
    return apiClient.post('token/', credentials);
  }
};
