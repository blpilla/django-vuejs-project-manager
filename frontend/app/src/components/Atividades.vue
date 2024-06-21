<template>
  <div class="container">
    <h1>Atividades</h1>
    <form @submit.prevent="saveAtividade">
      <label for="newAtividade">Nome da Atividade</label>
      <input id="newAtividade" v-model="newAtividade" placeholder="Nome da Atividade">
      <span v-if="errors.newAtividade" class="error">{{ errors.newAtividade }}</span>
      
      <label for="selectedProjeto">Projeto</label>
      <select id="selectedProjeto" v-model="selectedProjeto">
        <option v-for="projeto in projetos" :key="projeto.id" :value="projeto.id">{{ projeto.nome }}</option>
      </select>
      <span v-if="errors.selectedProjeto" class="error">{{ errors.selectedProjeto }}</span>
      
      <label for="selectedStatus">Status</label>
      <select id="selectedStatus" v-model="selectedStatus">
        <option value="Pendente">Pendente</option>
        <option value="Em Andamento">Em Andamento</option>
        <option value="Concluída">Concluída</option>
      </select>
      
      <button type="submit">{{ editingAtividade ? 'Atualizar Atividade' : 'Adicionar Atividade' }}</button>
    </form>
    <ul>
      <li v-for="atividade in atividades" :key="atividade.id">
        {{ atividade.nome }} - Projeto: {{ atividade.projeto_nome }} - Status: {{ atividade.status }}
        <div>
          <button @click="editAtividade(atividade)">Editar</button>
          <button @click="deleteAtividade(atividade.id)">Excluir</button>
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
      atividades: [],
      projetos: [],
      newAtividade: '',
      selectedProjeto: null,
      selectedStatus: 'Pendente', // Valor padrão
      editingAtividade: null,
      errors: {},
    };
  },
  created() {
    const token = localStorage.getItem('token');
    if (!token) {
      this.$router.push('/login');
    } else {
      this.fetchAtividades();
      this.fetchProjetos();
    }
  },
  methods: {
    fetchAtividades() {
      api.getAtividades()
        .then(response => {
          this.atividades = response.data.map(atividade => ({
            ...atividade,
            projeto_nome: atividade.projeto.nome
          }));
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    fetchProjetos() {
      api.getProjetos()
        .then(response => {
          this.projetos = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    validateForm() {
      this.errors = {};
      if (!this.newAtividade) {
        this.errors.newAtividade = 'Nome da Atividade é obrigatório.';
      }
      if (!this.selectedProjeto) {
        this.errors.selectedProjeto = 'Projeto é obrigatório.';
      }
      return Object.keys(this.errors).length === 0;
    },
    saveAtividade() {
      if (this.validateForm()) {
        if (this.editingAtividade) {
          this.updateAtividade();
        } else {
          this.addAtividade();
        }
      }
    },
    addAtividade() {
      const data = { nome: this.newAtividade, projeto: this.selectedProjeto, status: this.selectedStatus };
      api.addAtividade(data)
        .then(() => {
          this.newAtividade = '';
          this.selectedProjeto = null;
          this.selectedStatus = 'Pendente'; // Reset para valor padrão
          this.fetchAtividades();
        })
        .catch(error => {
          console.error('There was an error!', error.response ? error.response.data : error);
        });
    },
    editAtividade(atividade) {
      this.editingAtividade = atividade;
      this.newAtividade = atividade.nome;
      this.selectedProjeto = atividade.projeto.id;
      this.selectedStatus = atividade.status;
    },
    updateAtividade() {
      api.updateAtividade(this.editingAtividade.id, { nome: this.newAtividade, projeto: this.selectedProjeto, status: this.selectedStatus })
        .then(() => {
          this.newAtividade = '';
          this.selectedProjeto = null;
          this.selectedStatus = 'Pendente'; // Reset para valor padrão
          this.editingAtividade = null;
          this.fetchAtividades();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    deleteAtividade(id) {
      api.deleteAtividade(id)
        .then(() => {
          this.fetchAtividades();
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
