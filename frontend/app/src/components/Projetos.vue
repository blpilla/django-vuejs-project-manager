<template>
  <div class="container">
    <h1>Projetos</h1>
    <form @submit.prevent="saveProjeto">
      <label for="newProjeto">Nome do Projeto</label>
      <input id="newProjeto" v-model="newProjeto" placeholder="Nome do Projeto">
      <span v-if="errors.newProjeto" class="error">{{ errors.newProjeto }}</span>
      
      <label for="selectedCliente">Cliente</label>
      <select id="selectedCliente" v-model="selectedCliente">
        <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">{{ cliente.nome }}</option>
      </select>
      <span v-if="errors.selectedCliente" class="error">{{ errors.selectedCliente }}</span>
      
      <label for="selectedStatus">Status</label>
      <select id="selectedStatus" v-model="selectedStatus">
        <option value="Pendente">Pendente</option>
        <option value="Em Andamento">Em Andamento</option>
        <option value="Concluída">Concluída</option>
      </select>
      
      <button type="submit">{{ editingProjeto ? 'Atualizar Projeto' : 'Adicionar Projeto' }}</button>
    </form>
    <ul>
      <li v-for="projeto in projetos" :key="projeto.id">
        {{ projeto.nome }} - Cliente: {{ projeto.cliente_nome }} - Status: {{ projeto.status }}
        <div>
          <button @click="editProjeto(projeto)">Editar</button>
          <button @click="deleteProjeto(projeto.id)">Excluir</button>
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
      projetos: [],
      clientes: [],
      newProjeto: '',
      selectedCliente: null,
      selectedStatus: 'Pendente', // Valor padrão
      editingProjeto: null,
      errors: {},
    };
  },
  created() {
    const token = localStorage.getItem('token');
    if (!token) {
      this.$router.push('/login');
    } else {
      this.fetchProjetos();
      this.fetchClientes();
    }
  },
  methods: {
    fetchProjetos() {
      api.getProjetos()
        .then(response => {
          this.projetos = response.data.map(projeto => ({
            ...projeto,
            cliente_nome: projeto.cliente.nome
          }));
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
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
      if (!this.newProjeto) {
        this.errors.newProjeto = 'Nome do Projeto é obrigatório.';
      }
      if (!this.selectedCliente) {
        this.errors.selectedCliente = 'Cliente é obrigatório.';
      }
      return Object.keys(this.errors).length === 0;
    },
    saveProjeto() {
      if (this.validateForm()) {
        if (this.editingProjeto) {
          this.updateProjeto();
        } else {
          this.addProjeto();
        }
      }
    },
    addProjeto() {
      const data = { nome: this.newProjeto, cliente: this.selectedCliente, status: this.selectedStatus };
      api.addProjeto(data)
        .then(() => {
          this.newProjeto = '';
          this.selectedCliente = null;
          this.selectedStatus = 'Pendente'; // Reset para valor padrão
          this.fetchProjetos();
        })
        .catch(error => {
          console.error('There was an error!', error.response ? error.response.data : error);
        });
    },
    editProjeto(projeto) {
      this.editingProjeto = projeto;
      this.newProjeto = projeto.nome;
      this.selectedCliente = projeto.cliente.id;
      this.selectedStatus = projeto.status;
    },
    updateProjeto() {
      api.updateProjeto(this.editingProjeto.id, { nome: this.newProjeto, cliente: this.selectedCliente, status: this.selectedStatus })
        .then(() => {
          this.newProjeto = '';
          this.selectedCliente = null;
          this.selectedStatus = 'Pendente'; // Reset para valor padrão
          this.editingProjeto = null;
          this.fetchProjetos();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    deleteProjeto(id) {
      api.deleteProjeto(id)
        .then(() => {
          this.fetchProjetos();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  },
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
