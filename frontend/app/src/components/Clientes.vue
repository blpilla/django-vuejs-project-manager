<template>
  <div class="container">
    <h1>Clientes</h1>
    <form @submit.prevent="saveCliente">
      <label for="newCliente">Nome do Cliente</label>
      <input id="newCliente" v-model="newCliente" placeholder="Nome do Cliente">
      <span v-if="errors.newCliente" class="error">{{ errors.newCliente }}</span>
      <button type="submit">{{ editingCliente ? 'Atualizar Cliente' : 'Adicionar Cliente' }}</button>
    </form>
    <ul>
      <li v-for="cliente in clientes" :key="cliente.id">
        {{ cliente.nome }}
        <div>
          <button @click="editCliente(cliente)">Editar</button>
          <button @click="deleteCliente(cliente.id)">Excluir</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import api from '../api';

export default {
  data() {
    return {
      clientes: [],
      newCliente: '',
      editingCliente: null,
      errors: {},
    };
  },
  created() {
    const token = localStorage.getItem('token');
    if (!token) {
      this.$router.push('/login');
    } else {
      this.fetchClientes();
    }
  },
  methods: {
    fetchClientes() {
      api.getClientes()
        .then(response => {
          this.clientes = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    validateForm() {
      this.errors = {};
      if (!this.newCliente) {
        this.errors.newCliente = 'Nome do Cliente é obrigatório.';
      }
      return Object.keys(this.errors).length === 0;
    },
    saveCliente() {
      if (this.validateForm()) {
        if (this.editingCliente) {
          this.updateCliente();
        } else {
          this.addCliente();
        }
      }
    },
    addCliente() {
      api.addCliente({ nome: this.newCliente })
        .then(() => {
          this.newCliente = '';
          this.fetchClientes();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    editCliente(cliente) {
      this.editingCliente = cliente;
      this.newCliente = cliente.nome;
    },
    updateCliente() {
      api.updateCliente(this.editingCliente.id, { nome: this.newCliente })
        .then(() => {
          this.newCliente = '';
          this.editingCliente = null;
          this.fetchClientes();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    deleteCliente(id) {
      api.deleteCliente(id)
        .then(() => {
          this.fetchClientes();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
