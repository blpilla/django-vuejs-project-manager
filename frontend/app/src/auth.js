import api from './api';

export async function login(username, password) {
  const response = await api.post('token/', { username, password });
  return response.data;
}
